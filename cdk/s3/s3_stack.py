from aws_cdk import (
    Stack,
    aws_s3,
)
from constructs import Construct


class S3DeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_s3.Bucket(
            self,
            'cdk.bucket',
            bucket_name = 'cdk.bucket'
        )