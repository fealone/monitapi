import subprocess

from .deployer import Deployer
from .models import DeployConfig


class CloudFunctions(Deployer):

    def deploy(self, config: DeployConfig) -> None:
        options = " ".join([f"{key} {value}" for key, value in config.options.items()])
        cmd = (f"cd {self.source_directory} && "
               f"gcloud functions deploy {config.name} "
               "--runtime python37 "
               "--trigger-http "
               "--entry-point entry_point "
               "--set-env-vars PLATFORM=GCP ")
        cmd += options
        subprocess.run(cmd, shell=True, check=True)
