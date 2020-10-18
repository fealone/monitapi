from deploy.deployer import Deployer
from deploy.models import DeployAWSLambda


class AWSLambda(Deployer):

    def deploy(self, config: DeployAWSLambda) -> None:
        pass
