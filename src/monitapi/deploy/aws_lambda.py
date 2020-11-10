import os
import shutil
import subprocess

from .deployer import Deployer
from .models import DeployConfig


class AWSLambda(Deployer):

    def deploy(self, config: DeployConfig) -> None:
        options = " ".join([f"{key} {value}" for key, value in config.options.items()])
        root_path = os.path.join(self.directory, "monitapi")
        cmd = f"pip install -r {root_path}/requirements.txt -t {self.source_directory}/"
        subprocess.run(cmd, shell=True, check=True)
        shutil.make_archive(f"{root_path}/dist", "zip", root_dir=self.source_directory, base_dir="./")
        try:
            subprocess.run(f"aws lambda get-function-configuration --function-name {config.name} > /dev/null 2>&1",
                           shell=True,
                           check=True)
            cmd = ("aws lambda update-function-code "
                   f"--function-name {config.name} "
                   f"--zip-file fileb://{root_path}/dist.zip")
            subprocess.run(cmd, shell=True, check=True)
        except Exception:
            cmd = ("aws lambda create-function "
                   f"--function-name {config.name} "
                   "--runtime python3.7 "
                   "--handler main.entry_point "
                   f"--zip-file fileb://{root_path}/dist.zip "
                   "--environment 'Variables={PLATFORM=AWS}' ")
            cmd += options
            subprocess.run(cmd, shell=True, check=True)
