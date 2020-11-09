import os
import shutil

from .deployer import Deployer
from .models import DeployConfig


class AWSLambda(Deployer):

    def deploy(self, config: DeployConfig) -> None:
        options = " ".join([f"{key} {value}" for key, value in config.options.items()])
        root_path = os.path.join(self.directory, "monitapi")
        cmd = f"pip install -r {root_path}/requirements.txt -t {self.source_directory}/"
        os.system(cmd)
        shutil.make_archive(f"{root_path}/dist", "zip", root_dir=self.source_directory, base_dir="./")
        cmd = ("aws lambda create-function "
               f"--function-name {config.name} "
               "--runtime python3.7 "
               "--handler main.entry_point "
               f"--zip-file fileb://{root_path}/dist.zip "
               "--environment 'Variables={PLATFORM=AWS}' ")
        cmd += options
        os.system(cmd)
