# async-lambda

`async-lambda` is a framework for creating `AWS Lambda` applications with built
in support for asynchronous invocation via a SQS Queue. This is useful if you
have workloads you need to split up into separate execution contexts.

`async-lambda` converts your application into a `Serverless Application Model (SAM)`
template which can be deployed with the `SAM` cli tool.

An `async-lambda` application is comprised of a `controller` object and `tasks`.

```python
import json
from async_lambda import AsyncLambdaController, ScheduledEvent, ManagedSQSEvent, config_set_name

app = AsyncLambdaController()
config_set_name("project-name")
lambda_handler = app.async_lambda_handler # This "export" is required for lambda.

@app.scheduled_task('ScheduledTask1', schedule_expression="rate(15 minutes)")
def scheduled_task_1(event: ScheduledEvent):
    app.async_invoke("AsyncTask1", payload={"foo": "bar"}) # Payload must be JSON serializable and < 2560Kb

@app.async_task('AsyncTask1')
def async_task_2(event: ManagedSQSEvent):
    print(event.payload)  #{"foo": "bar"}

```

**When the app is packaged for lambda, only the main module, and the `vendor` and `src` directories are included.**

# Tasks

The core abstraction in `async-lambda` is a `task`. Each task will result in a separate lambda function.
Tasks have a `trigger_type` which determines what event triggers them. A task is identified by its unique `task_id`.

All task decorators share common arguments for configuring the underlying lambda function:

- `memory: int = 128` Sets the memory allocation for the function.
- `timeout: int = 60` Sets the timeout for the function (max 900 seconds).
- `ephemeral_storage: int = 512` Sets the ephemeral storage allocation for the function.
- `maximum_concurrency: Optional[int] = None` Sets the maximum concurrency value for the SQS trigger for the function. (only applies to `async_task` and `sqs_task` tasks.)

## Async Task

All async tasks have a matching SQS queue which the lambda function consumes from (1 message per invocation).
All async task queues share a DLQ. Async tasks can be invoked from anywhere within the app by using the
`AsyncLambdaController.async_invoke` method. Calling this method sends a message into the queue for the given task.
The task function should have a single parameter of the `ManagedSQSEvent` type.

```python
app = AsyncLambdaController()

@app.async_task("TaskID")
def async_task(event: ManagedSQSEvent):
    event.payload # payload sent via the `async_invoke` method
    event.source_task_id # the task_id where the event originated
```

**It is quite easy to get into infinite looping situations when utilizing `async-lambda` and care should be taken.**

**INFINITE LOOP EXAMPLE**

```python
# If task_1 where to ever get invoked, then it would start an infinite loop with
# task 1 invoking task 2, task 2 invoking task 1, and repeat...

@app.async_task("Task1")
def task_1(event: ManagedSQSEvent):
    app.async_invoke("Task2", {})

@app.async_task("Task2")
def task_1(event: ManagedSQSEvent):
    app.async_invoke("Task1", {})
```

## Unmanaged SQS Task

Unmanaged SQS tasks consume from any arbitrary SQS queue (1 message per invocation).
The task function should have a single parameter of the `UnmanagedSQSEvent` type.

```python
app = AsyncLambdaController()

@app.sqs_task("TaskID", queue_arn='queue-arn')
def sqs_task(event: UnmanagedSQSEvent):
    event.body # sqs event body
```

## Scheduled Task

Scheduled tasks are triggered by an eventbridge schedule. The schedule expression can be
a [cron expression](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html)
or a [rate expression](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rate-expressions.html).
The task function should have a single parameter of the `ScheduledEvent` type.

```python
app = AsyncLambdaController()

@app.scheduled_task("TaskID", schedule_expression='rate(15 minutes)')
def scheduled_task(event: ScheduledEvent):
    ...
```

## API Task

API tasks are triggered by a Web Request. `async-lambda` creates an APIGateway endpoint matching the
`method` and `path` in the task definition. It is possible to configure a custom domain and certificate
for all API tasks within an `async-lambda` app.
The task function should have a single parameter of the `APIEvent` type.

```python
app = AsyncLambdaController()

@app.api_task("TaskID", path='/test', method='get')
def api_task(event: APIEvent):
    event.headers # request headers
    event.querystring_params # request querystring params
    event.body # request body
```

# `async-lambda` config

Configuration options can be set with the `.async_lambda/config.json` file.
The configuration options can be set at the app, stage, and task level. A configuration option set
will apply unless overridden at a more specific level (app -> stage -> task -> stage).
The override logic attempts to non-destructive so if you have a `layers` of `['layer_1']` at the app level,
and `[layer_2]` at the stage level, then the value will be `['layer_1', 'layer_2']`.

**Config file levels schema**

```
{
    # APP LEVEL
    "stages": {
        "stage_name": {
            # STAGE LEVEL
        }
    },
    "tasks": {
        "task_id": {
            # TASK LEVEL
            "stages": {
                "stage_name": {
                    # TASK STAGE LEVEL
                }
            }
        }
    }
}
```

**At any of these `levels` any of the configuration options can be set:**
With the exception of `domain_name`, `tls_version`, and `certificate_arn` which can not be set at the task level.

## `environment_variables`

```
{
    "ENV_VAR_NAME": "ENV_VAR_VALUE"
}
```

This config value will set environment variables for the function execution.
These environment variables will also be available during build time.

[The value is passed to the `Environment` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-environment)

## `policies`

```
[
    'IAM_POLICY_ARN' | STATEMENT
]
```

Use this config option to attach any arbitrary policies to the lambda functions execution role.

[The value is passed to the `Policies` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-policies), in addition to the `async-lambda` created inline policies.

## `layers`

```
[
    "LAYER_ARN"
]
```

Use this config option to add any arbitrary lambda layers to the lambda functions. Ordering matters,
and merging is done thru concatenation.

[The value is passed to the `Layers` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-layers)

## `subnet_ids`

```
[
    "SUBNET_ID
]
```

Use this config option to put the lambda function into a vpc/subnet.

The value is passed into the [`SubnetIds`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html) field of the [`VpcConfig` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-vpcconfig)

## `security_group_ids`

```
[
    "SECURITY_GROUP_ID"
]
```

Use this config option to attach a security group to the lambda function.

The value is passed into the [`SecurityGroupIds`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html) field of the [`VpcConfig` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-vpcconfig)

## `managed_queue_extras`

```
[
    {
        # Cloudformation resource
    }
]
```

Use this config option to add extra resources for managed SQS queues (`async_task` tasks.)

For example this might be used to attach alarms to these queues.

Each item in the list should be a complete cloudformation resource. `async-lambda` provides a few custom substitutions
so that you can reference the extras and the associated managed sqs resource by `LogicalId`.

- `$QUEUEID"` will be replaced with the `LogicalId` of the associated Managed SQS queue.
- `$EXTRA<index>` will be replaced with the `LogicalId` of the extra at the specified index.

## `domain_name`

**This config value can only be set at the app or stage level.**

```
"domain_name"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`DomainName`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

## `tls_version`

**This config value can only be set at the app or stage level.**

```
"tls_version"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`SecurityPolicy`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

Possible values are `TLS_1_0` and `TLS_1_2`

## `certificate_arn`

**This config value can only be set at the app or stage level.**

```
"certificate_arn"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`CertificateArn`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

# Building an `async-lambda` app

**When the app is packaged for lambda, only the main module, and the `vendor` and `src` directories are included.**

From the project root directory, utilize the `async-lambda` CLI tool to generate
a SAM template and function bundle. Optionally specify the `stage` to use `stage` specific configs.

```bash
# app.py contains the root AsyncLambdaController
async-lambda build app --stage <stage-name>
```

This will generate a SAM template `template.json` as well as an `deployment.zip` file.
This template and zip file can then be deployed or transformed into regular cloudformation
via the `sam` or `aws` cli tools.

# Known Limitations

- Lambda Configuration - not all of the lambda configuration spec is present in `async-lambda`. It is relatively trivial to add in configuration options. Make an issue if there is a feature you would like to see implemented.
- The `async_invoke` payload must be `JSON` serializable with `json.dumps`.
- It is possible to get into infinite loops quite easily. (Task A invokes Task B, Task B invokes Task A)
