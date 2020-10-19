import os
from abc import ABC, abstractmethod
from tempfile import TemporaryDirectory

from .models import DeployConfig


class Deployer(ABC):

    def __init__(self, tmp_dir: TemporaryDirectory):
        self.tmp_dir = tmp_dir

    @property
    def source_directory(self) -> str:
        return os.path.join(self.tmp_dir.name, "monitapi/src")

    @property
    def directory(self) -> str:
        return self.tmp_dir.name

    @abstractmethod
    def deploy(self, config: DeployConfig) -> None:
        ...
