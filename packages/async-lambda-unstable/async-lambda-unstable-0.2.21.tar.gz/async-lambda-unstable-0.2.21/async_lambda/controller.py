import functools
import json
import logging
import re
import time
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Optional
from uuid import uuid4

from . import env
from .build_config import get_build_config_for_stage
from .client import get_s3_client, get_sqs_client
from .models.events.api_event import APIEvent
from .models.events.managed_sqs_event import ManagedSQSEvent
from .models.events.scheduled_event import ScheduledEvent
from .models.events.unmanaged_sqs_event import UnmanagedSQSEvent
from .models.mock.mock_context import MockLambdaContext
from .models.mock.mock_event import MockSQSLambdaEvent
from .models.task import AsyncLambdaTask, TaskTriggerType

logger = logging.getLogger(__name__)


class AsyncLambdaController:
    is_sub: bool
    tasks: Dict[str, AsyncLambdaTask]
    current_task_id: Optional[str] = None
    current_invocation_id: Optional[str] = None
    parent_controller: Optional["AsyncLambdaController"] = None

    def __init__(self, is_sub: bool = False):
        self.tasks = dict()
        self.is_sub = is_sub

    def add_task(self, task: AsyncLambdaTask):
        """
        Adds a task to the async lambda controller.
        """
        if task.task_id in self.tasks:
            raise Exception(
                f"A task with the task_id {task.task_id} already exists. DUPLICATE TASK IDS"
            )
        self.tasks[task.task_id] = task

    def generate_sam_template(
        self,
        module: str,
        config_dict: dict,
        stage: Optional[str] = None,
    ) -> dict:
        """
        Generates the SAM Template for this project.
        """
        template = {
            "AWSTemplateFormatVersion": "2010-09-09",
            "Transform": "AWS::Serverless-2016-10-31",
            "Resources": {
                "AsyncLambdaPayloadBucket": {
                    "Type": "AWS::S3::Bucket",
                },
                "AsyncLambdaDLQ": {
                    "Type": "AWS::SQS::Queue",
                    "Properties": {"MessageRetentionPeriod": 1_209_600},  # 14 days
                },
            },
        }
        _task_list = list(self.tasks.values())
        has_api_tasks = False
        for task in _task_list:
            if task.trigger_type == TaskTriggerType.API_EVENT:
                has_api_tasks = True
            for logical_id, resource in task.get_sam_template(
                module, _task_list, config_dict, stage
            ).items():
                template["Resources"][logical_id] = resource

        build_config = get_build_config_for_stage(config_dict, stage)
        for extra_index, extra in enumerate(build_config.managed_queue_extras):
            template["Resources"][
                self._dlq_extra_logical_id(extra_index)
            ] = self._dlq_extras_replace_references(extra)

        if has_api_tasks:
            properties: dict = {"StageName": "prod"}
            if build_config.domain_name is not None:
                properties["Domain"] = {
                    "DomainName": build_config.domain_name,
                }
                if build_config.certificate_arn is not None:
                    properties["Domain"][
                        "CertificateArn"
                    ] = build_config.certificate_arn
                    if build_config.tls_version is not None:
                        properties["Domain"][
                            "SecurityPolicy"
                        ] = build_config.tls_version
            template["Resources"]["AsyncLambdaAPIGateway"] = {
                "Type": "AWS::Serverless::Api",
                "Properties": properties,
            }
        return template

    def _dlq_extra_logical_id(self, index: int):
        return f"AsyncLambdaDLQExtra{index}"

    def _dlq_extras_replace_references(self, extra: dict) -> dict:
        stringified_extra = json.dumps(extra)
        stringified_extra = re.sub(
            r"\$EXTRA(?P<index>[0-9]+)",
            lambda m: self._dlq_extra_logical_id(int(m.group("index"))),
            stringified_extra,
        )
        stringified_extra = stringified_extra.replace("$QUEUEID", "AsyncLambdaDLQ")

        return json.loads(stringified_extra)

    def set_current_task_id(self, task_id: str):
        """
        Set the current_task_id
        """
        self.current_task_id = task_id

    def set_current_invocation_id(self, invocation_id: str):
        """
        Set the current_invocation_id
        """
        self.current_invocation_id = invocation_id

    def handle_invocation(self, event, context, task_id: Optional[str] = None):
        """
        Direct the invocation to the task executor.
        """
        if task_id is None:
            task_id = env.get_current_task_id()
        task = self.tasks[task_id]

        if task.trigger_type == TaskTriggerType.MANAGED_SQS:
            _event = ManagedSQSEvent(event, context)
            self.set_current_invocation_id(_event.invocation_id)
        elif task.trigger_type == TaskTriggerType.UNMANAGED_SQS:
            _event = UnmanagedSQSEvent(event, context)
        elif task.trigger_type == TaskTriggerType.SCHEDULED_EVENT:
            _event = ScheduledEvent(event, context)
        elif task.trigger_type == TaskTriggerType.API_EVENT:
            _event = APIEvent(event, context)
        else:
            raise NotImplementedError(
                f"Trigger type of {task.trigger_type} is not supported."
            )
        response = task.execute(_event)
        if isinstance(_event, ManagedSQSEvent) and _event.s3_payload_key is not None:
            get_s3_client().delete_object(
                Bucket=env.get_payload_bucket(), Key=_event.s3_payload_key
            )
        return response

    def _async_invoke(
        self,
        destination_task_id: str,
        payload: Any,
        delay: Optional[int] = None,
        force_sync: bool = False,
    ):
        """
        Invoke an 'async-lambda' task asynchronously utilizing it's SQS queue
        """
        if self.parent_controller is not None:
            return self.parent_controller._async_invoke(
                destination_task_id=destination_task_id,
                payload=payload,
                delay=delay,
                force_sync=force_sync,
            )
        if destination_task_id not in self.tasks:
            raise Exception(
                f"No such task exists with the task_id {destination_task_id}"
            )
        destination_task = self.tasks[destination_task_id]
        if destination_task.trigger_type != TaskTriggerType.MANAGED_SQS:
            raise Exception(
                f"Unable to invoke task '{destination_task_id}' because it is a {destination_task.trigger_type} task"
            )
        if self.current_invocation_id is None:
            invocation_id = str(uuid4())
        else:
            invocation_id = self.current_invocation_id

        raw_sqs_body = {
            "source_task_id": self.current_task_id,
            "destination_task_id": destination_task_id,
            "invocation_id": invocation_id,
        }
        serialized_payload = json.dumps(payload)
        payload_size = len(serialized_payload.encode())
        if payload_size < 250_000:  # we need to double encode to be sure
            payload_size = len(json.dumps(serialized_payload).encode())
        logger.info(
            f"Invoking task '{destination_task.task_id}' - invocation_id '{invocation_id}' - delay {delay or 0} - size ({payload_size})"
        )
        if force_sync or env.get_force_sync_mode():
            raw_sqs_body["payload"] = serialized_payload
            if delay:
                time.sleep(delay)
            # Sync invocation with mock event/context
            mock_event = MockSQSLambdaEvent(json.dumps(raw_sqs_body))
            mock_context = MockLambdaContext(destination_task.task_id)
            return self.handle_invocation(
                mock_event, mock_context, task_id=destination_task_id
            )
        else:
            # Encode/Send payload over sqs
            if payload_size > 250_000:  # payload is bigger than max SQS size
                date_part = datetime.now(tz=timezone.utc).strftime("%Y/%m/%d")
                key = f"{date_part}/{uuid4().hex}.json"
                logger.info(f"Utilizing S3 Payload because of payload size. Key: {key}")
                raw_sqs_body["s3_payload_key"] = key
                get_s3_client().put_object(
                    Bucket=env.get_payload_bucket(), Key=key, Body=serialized_payload
                )
            else:
                raw_sqs_body["payload"] = serialized_payload
            get_sqs_client().send_message(
                QueueUrl=destination_task.get_managed_queue_url(),
                MessageBody=json.dumps(raw_sqs_body),
                DelaySeconds=delay,
            )

    def add_controller(self, controller: "AsyncLambdaController"):
        controller.parent_controller = self
        for task in controller.tasks.values():
            self.add_task(task)

    def async_invoke(
        self,
        task_id: str,
        payload: Any,
        delay: Optional[int] = 0,
        force_sync: bool = False,
    ):
        """
        Invoke an Async-Lambda task.
        """
        self._async_invoke(
            destination_task_id=task_id,
            payload=payload,
            delay=delay,
            force_sync=force_sync,
        )

    def async_lambda_handler(self, event, context):
        """
        The handler invoked by Lambda.
        """
        return self.handle_invocation(event, context, task_id=None)

    def async_task(self, task_id: str, max_receive_count: int = 1, **kwargs):
        """
        Decorate a function to register it as an async task.
        These functions can be asynchronously invoked with the `async_invoke` function
        via their `task_id`.
        """
        logger.debug(f"Registering async task '{task_id}' with the controller.")

        def _task(func: Callable[[ManagedSQSEvent], Any]):
            self.add_task(
                AsyncLambdaTask(
                    executable=func,
                    task_id=task_id,
                    trigger_type=TaskTriggerType.MANAGED_SQS,
                    trigger_config={"max_receive_count": max_receive_count},
                    **kwargs,
                )
            )

            @functools.wraps(func)
            def inner(*args, **kwargs):
                self.set_current_task_id(task_id)
                return func(*args, **kwargs)

            return inner

        return _task

    def sqs_task(self, task_id: str, queue_arn: str, **kwargs):
        """
        Decorate a function to register it as an SQS task.
        These tasks will be triggered by messages in the given queue.
        """
        logger.debug(
            f"Registering sqs task '{task_id}' arn '{queue_arn}' with the controller."
        )

        def _task(func: Callable[[UnmanagedSQSEvent], Any]):
            self.add_task(
                AsyncLambdaTask(
                    executable=func,
                    task_id=task_id,
                    trigger_type=TaskTriggerType.UNMANAGED_SQS,
                    trigger_config={"queue_arn": queue_arn},
                    **kwargs,
                )
            )

            @functools.wraps(func)
            def inner(*args, **kwargs):
                self.set_current_task_id(task_id)
                return func(*args, **kwargs)

            return inner

        return _task

    def scheduled_task(self, task_id: str, schedule_expression: str, **kwargs):
        """
        Decorate a function to register it as a scheduled task.
        These tasks will be triggered by the given schedule expression.
        """
        logger.debug(
            f"Registering scheduled task '{task_id}' with schedule '{schedule_expression}' with the controller."
        )

        def _task(func: Callable[[ScheduledEvent], Any]):
            self.add_task(
                AsyncLambdaTask(
                    executable=func,
                    task_id=task_id,
                    trigger_type=TaskTriggerType.SCHEDULED_EVENT,
                    trigger_config={"schedule_expression": schedule_expression},
                    **kwargs,
                )
            )

            @functools.wraps(func)
            def inner(*args, **kwargs):
                self.set_current_task_id(task_id)
                return func(*args, **kwargs)

            return inner

        return _task

    def api_task(self, task_id: str, path: str, method: str, **kwargs):
        """
        Decorate a function to register it as an API task.
        These tasks will be triggered by an API call.
        """
        logger.debug(
            f"Registering api task '{task_id}' with the path '{path}' and method '{method}' with the controller."
        )

        def _task(func: Callable[[APIEvent], Any]):
            self.add_task(
                AsyncLambdaTask(
                    executable=func,
                    task_id=task_id,
                    trigger_type=TaskTriggerType.API_EVENT,
                    trigger_config={"path": path, "method": method},
                    **kwargs,
                )
            )

            @functools.wraps(func)
            def inner(*args, **kwargs):
                self.set_current_task_id(task_id)
                return func(*args, **kwargs)

            return inner

        return _task
