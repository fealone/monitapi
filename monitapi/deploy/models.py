from enum import Enum
from typing import Dict

from pydantic import BaseModel


class DeployPlatform(str, Enum):
    cloud_functions = "cloud_functions"
    aws_lambda = "aws_lambda"


class DeployConfig(BaseModel):
    name: str
    options: Dict[str, str]
