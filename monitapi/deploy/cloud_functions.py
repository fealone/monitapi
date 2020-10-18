import os

from .deployer import Deployer
from .models import DeployCloudFunctions


class CloudFunctions(Deployer):

    def deploy(self, config: DeployCloudFunctions) -> None:
        cmd = (f"cd {self.source_directory} && "
               f"gcloud functions deploy {config.name} "
               f"--runtime python37 "
               f"--trigger-http "
               f"--entry-point entry_point "
               f"--region {config.region} "
               f"--set-env-vars PLATFORM=GCP")
        os.system(cmd)
