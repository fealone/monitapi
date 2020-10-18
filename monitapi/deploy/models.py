from enum import Enum

from pydantic import BaseModel


class DeployPlatform(str, Enum):
    cloud_functions = "cloud_functions"
    aws_lambda = "aws_lambda"


class DeployConfig(BaseModel):
    ...


class DeployCloudFunctions(DeployConfig):
    name: str
    region: str


class DeployAWSLambda(DeployConfig):
    name: str
    lambda_role: str
