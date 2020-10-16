from tempfile import TemporaryDirectory

import click

from deploy.aws_lambda import AWSLambda
from deploy.cloud_functions import CloudFunctions
from deploy.models import DeployName

from libs.exceptions import UnsupportedDeployName


@click.group()
def commands() -> None:
    pass


@commands.command()
def serve() -> None:
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


@commands.command()
@click.argument("path")
def monitor(path: str) -> None:
    import asyncio
    from monitoring.monitor import watch
    asyncio.run(watch(open(path)))


@commands.command()
@click.argument("name")
@click.option("-f", "--file")
def deploy(name: DeployName, file: str) -> None:
    import os
    import shutil
    import git
    if not hasattr(DeployName, name):
        raise UnsupportedDeployName(name)
    tmp_dir = TemporaryDirectory(prefix="monitapi")
    git.Git(tmp_dir.name).clone("https://github.com/fealone/monitapi")
    if file:
        shutil.copyfile(file, os.path.join(tmp_dir.name, "monitapi/src/targets.yaml"))
    else:
        shutil.copyfile("targets.yaml", os.path.join(tmp_dir.name, "monitapi/src/targets.yaml"))
    if name == DeployName.cloud_functions:
        CloudFunctions(tmp_dir).deploy()
    if name == DeployName.aws_lambda:
        AWSLambda(tmp_dir).deploy()


if __name__ == "__main__":
    commands()
