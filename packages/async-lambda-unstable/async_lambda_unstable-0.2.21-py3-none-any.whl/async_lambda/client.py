from typing import Any, Optional

import boto3


class Clients:
    s3_client: Optional[Any] = None
    sqs_client: Optional[Any] = None


clients = Clients()


def get_s3_client():
    if clients.s3_client is None:
        clients.s3_client = boto3.client("s3")
    return clients.s3_client


def get_sqs_client():
    if clients.sqs_client is None:
        clients.sqs_client = boto3.client("sqs")
    return clients.sqs_client
