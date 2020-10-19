from .deployer import Deployer
from .models import DeployConfig


class AWSLambda(Deployer):

    def deploy(self, config: DeployConfig) -> None:
        raise Exception(("AWS Lambda is not currently supported.\r\n"
                        "However, please wait as we plan to support it in the future."))
