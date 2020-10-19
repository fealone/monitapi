import os

from .deployer import Deployer
from .models import DeployConfig


class CloudFunctions(Deployer):

    def deploy(self, config: DeployConfig) -> None:
        options = " ".join([f"{key} {value}" for key, value in config.options.items()])
        cmd = (f"cd {self.source_directory} && "
               f"gcloud functions deploy {config.name} "
               f"--runtime python37 "
               f"--trigger-http "
               f"--entry-point entry_point "
               f"--set-env-vars PLATFORM=GCP ")
        cmd += options
        os.system(cmd)
