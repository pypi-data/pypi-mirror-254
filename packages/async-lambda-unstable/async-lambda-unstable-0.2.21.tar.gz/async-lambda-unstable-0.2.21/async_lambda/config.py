class AsyncLambdaConfig:
    name: str = "async-lambda"
    runtime: str = "python3.10"


config = AsyncLambdaConfig()


def config_set_name(name: str):
    """
    Sets the name for the project.
    """
    config.name = name


def config_set_runtime(runtime: str):
    """
    Sets the runtime for the project.
    """
    config.runtime = runtime
