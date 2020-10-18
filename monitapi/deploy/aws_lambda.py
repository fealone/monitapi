from .deployer import Deployer
from .models import DeployAWSLambda


class AWSLambda(Deployer):

    def deploy(self, config: DeployAWSLambda) -> None:
        pass
