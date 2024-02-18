import json
import re
from enum import Enum
from typing import Any, Callable, Generic, List, Optional, TypeVar, Union

from .. import env
from ..build_config import get_build_config_for_task
from ..config import config
from .events.managed_sqs_event import ManagedSQSEvent
from .events.scheduled_event import ScheduledEvent
from .events.unmanaged_sqs_event import UnmanagedSQSEvent


class TaskTriggerType(Enum):
    MANAGED_SQS = 1
    UNMANAGED_SQS = 2
    SCHEDULED_EVENT = 3
    API_EVENT = 4


EventType = TypeVar(
    "EventType", bound=Union[ManagedSQSEvent, ScheduledEvent, UnmanagedSQSEvent]
)


class AsyncLambdaTask(Generic[EventType]):
    task_id: str
    trigger_type: TaskTriggerType
    trigger_config: dict

    timeout: int
    memory: int
    ephemeral_storage: int
    maximum_concurrency: Optional[int]

    executable: Callable[[EventType], Any]

    def __init__(
        self,
        executable: Callable[[EventType], Any],
        task_id: str,
        trigger_type: TaskTriggerType,
        trigger_config: Optional[dict] = None,
        timeout: int = 60,
        memory: int = 128,
        ephemeral_storage: int = 512,
        maximum_concurrency: Optional[int] = None,
    ):
        AsyncLambdaTask.validate_task_id(task_id)
        self.executable = executable
        self.task_id = task_id
        self.trigger_type = trigger_type
        self.trigger_config = trigger_config if trigger_config is not None else dict()
        self.timeout = timeout
        self.memory = memory
        self.ephemeral_storage = ephemeral_storage
        self.maximum_concurrency = maximum_concurrency

    @staticmethod
    def validate_task_id(task_id: str):
        if not task_id.isalnum():
            raise ValueError("Task ID must contain only A-Za-z0-9")
        if len(task_id) > 32:
            raise ValueError("Task ID must be less than 32 characters long.")

    def get_managed_queue_name(self):
        """
        Returns the managed queue's name for this task.
        """
        if self.trigger_type != TaskTriggerType.MANAGED_SQS:
            raise Exception(f"The task {self.task_id} is not a managed queue task.")
        return f"{config.name}-{self.task_id}"

    def get_function_name(self):
        return f"{config.name}-{self.task_id}"

    def get_managed_queue_arn(self):
        if self.trigger_type != TaskTriggerType.MANAGED_SQS:
            raise Exception(f"The task {self.task_id} is not a managed queue task.")
        return f"arn:aws:sqs:{env.get_aws_region()}:{env.get_aws_account_id()}:{self.get_managed_queue_name()}"

    def get_managed_queue_url(self):
        if self.trigger_type != TaskTriggerType.MANAGED_SQS:
            raise Exception(f"The task {self.task_id} is not a managed queue task.")
        return f"https://sqs.{env.get_aws_region()}.amazonaws.com/{env.get_aws_account_id()}/{self.get_managed_queue_name()}"

    def get_function_logical_id(self):
        return f"{self.task_id}ALFunc"

    def get_managed_queue_logical_id(self):
        if self.trigger_type != TaskTriggerType.MANAGED_SQS:
            raise Exception(f"The task {self.task_id} is not a managed queue task.")
        return f"{self.task_id}ALQueue"

    def get_managed_queue_extra_logical_id(self, index: int):
        return f"{self.get_function_logical_id()}Extra{index}"

    def get_template_events(self):
        sqs_properties = {}
        if self.maximum_concurrency is not None:
            sqs_properties["ScalingConfig"] = {
                "MaximumConcurrency": self.maximum_concurrency
            }
        if self.trigger_type == TaskTriggerType.MANAGED_SQS:
            return {
                "ManagedSQS": {
                    "Type": "SQS",
                    "Properties": {
                        "BatchSize": 1,
                        "Enabled": True,
                        "Queue": {
                            "Fn::GetAtt": [
                                self.get_managed_queue_logical_id(),
                                "Arn",
                            ]
                        },
                        **sqs_properties,
                    },
                }
            }
        elif self.trigger_type == TaskTriggerType.UNMANAGED_SQS:
            return {
                "UnmanagedSQS": {
                    "Type": "SQS",
                    "Properties": {
                        "BatchSize": 1,
                        "Enabled": True,
                        "Queue": self.trigger_config["queue_arn"],
                        **sqs_properties,
                    },
                }
            }
        elif self.trigger_type == TaskTriggerType.SCHEDULED_EVENT:
            return {
                "ScheduledEvent": {
                    "Type": "ScheduleV2",
                    "Properties": {
                        "ScheduleExpression": self.trigger_config[
                            "schedule_expression"
                        ],
                        "Name": self.get_function_name(),
                    },
                }
            }
        elif self.trigger_type == TaskTriggerType.API_EVENT:
            return {
                "APIEvent": {
                    "Type": "Api",
                    "Properties": {
                        "Path": self.trigger_config["path"],
                        "Method": self.trigger_config["method"].lower(),
                        "RestApiId": {"Ref": "AsyncLambdaAPIGateway"},
                    },
                }
            }
        else:
            return {}

    def get_policy_sqs_resources(self):
        if self.trigger_type == TaskTriggerType.MANAGED_SQS:
            return [
                {
                    "Fn::GetAtt": [
                        self.get_managed_queue_logical_id(),
                        "Arn",
                    ]
                }
            ]
        elif self.trigger_type == TaskTriggerType.UNMANAGED_SQS:
            return [self.trigger_config["queue_arn"]]
        return []

    def get_sam_template(
        self,
        module: str,
        tasks: List["AsyncLambdaTask"],
        config_dict: dict,
        stage: Optional[str] = None,
    ) -> dict:
        build_config = get_build_config_for_task(config_dict, self.task_id, stage=stage)
        events = self.get_template_events()
        policy_sqs_resources = self.get_policy_sqs_resources()

        policy_statements = [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:DeleteObject",
                    "s3:PutObject",
                    "s3:GetObject",
                ],
                "Resource": {
                    "Fn::Join": [
                        "",
                        [
                            "arn:aws:s3:::",
                            {"Ref": "AsyncLambdaPayloadBucket"},
                            "/*",
                        ],
                    ]
                },
            },
        ]
        managed_tasks_logical_ids = [
            _task.get_managed_queue_logical_id()
            for _task in tasks
            if _task.trigger_type == TaskTriggerType.MANAGED_SQS
        ]
        if len(managed_tasks_logical_ids) > 0:
            policy_statements.append(
                {
                    "Effect": "Allow",
                    "Action": ["sqs:SendMessage"],
                    "Resource": [
                        {
                            "Fn::GetAtt": [
                                queue_logical_id,
                                "Arn",
                            ]
                        }
                        for queue_logical_id in managed_tasks_logical_ids
                    ],
                },
            )
        if len(policy_sqs_resources) > 0:
            policy_statements.append(
                {
                    "Effect": "Allow",
                    "Action": [
                        "sqs:ChangeMessageVisibility",
                        "sqs:DeleteMessage",
                        "sqs:GetQueueAttributes",
                        "sqs:GetQueueUrl",
                        "sqs:ReceiveMessage",
                    ],
                    "Resource": policy_sqs_resources,
                },
            )
        function_properties = {}
        if len(build_config.layers) > 0:
            function_properties["Layers"] = list(build_config.layers)
        if len(build_config.security_group_ids) > 0 or len(build_config.subnet_ids) > 0:
            function_properties["VpcConfig"] = {}
            if len(build_config.security_group_ids) > 0:
                function_properties["VpcConfig"]["SecurityGroupIds"] = list(
                    build_config.security_group_ids
                )
            if len(build_config.subnet_ids) > 0:
                function_properties["VpcConfig"]["SubnetIds"] = list(
                    build_config.subnet_ids
                )

        template = {
            self.get_function_logical_id(): {
                "Type": "AWS::Serverless::Function",
                "Properties": {
                    "Handler": f"{module}.lambda_handler",
                    "Runtime": config.runtime,
                    "Environment": {
                        "Variables": {
                            "ASYNC_LAMBDA_PAYLOAD_S3_BUCKET": {
                                "Ref": "AsyncLambdaPayloadBucket"
                            },
                            "ASYNC_LAMBDA_TASK_ID": self.task_id,
                            "ASYNC_LAMBDA_ACCOUNT_ID": {"Ref": "AWS::AccountId"},
                            **build_config.environment_variables,
                        }
                    },
                    "FunctionName": self.get_function_name(),
                    "CodeUri": ".async_lambda/build/deployment.zip",
                    "EphemeralStorage": {"Size": self.ephemeral_storage},
                    "MemorySize": self.memory,
                    "Timeout": self.timeout,
                    "Events": events,
                    "Policies": [
                        {"Statement": policy_statements},
                        *build_config.policies,
                    ],
                    **function_properties,
                },
            }
        }

        if self.trigger_type == TaskTriggerType.MANAGED_SQS:
            template[self.get_managed_queue_logical_id()] = {
                "Type": "AWS::SQS::Queue",
                "Properties": {
                    "QueueName": self.get_managed_queue_name(),
                    "RedrivePolicy": {
                        "deadLetterTargetArn": {
                            "Fn::GetAtt": [
                                "AsyncLambdaDLQ",
                                "Arn",
                            ]
                        },
                        "maxReceiveCount": self.trigger_config["max_receive_count"],
                    },
                    "VisibilityTimeout": self.timeout,
                },
            }
            for extra_index, extra in enumerate(build_config.managed_queue_extras):
                template[
                    self.get_managed_queue_extra_logical_id(extra_index)
                ] = self._managed_queue_extras_replace_references(extra)

        return template

    def _managed_queue_extras_replace_references(self, extra: dict) -> dict:
        stringified_extra = json.dumps(extra)
        stringified_extra = re.sub(
            r"\$EXTRA(?P<index>[0-9]+)",
            lambda m: self.get_managed_queue_extra_logical_id(int(m.group("index"))),
            stringified_extra,
        )
        stringified_extra = stringified_extra.replace(
            "$QUEUEID", self.get_managed_queue_logical_id()
        )

        return json.loads(stringified_extra)

    def execute(self, event: EventType) -> Any:
        """
        Executes the tasks function
        """
        return self.executable(event)
