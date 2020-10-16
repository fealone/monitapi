from enum import Enum


class DeployName(str, Enum):
    cloud_functions = "GCP Cloud Functions"
    aws_lambda = "AWS Lambda"
