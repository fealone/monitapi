import os
from tempfile import TemporaryDirectory
from typing import Any, Dict

from agraffe import Agraffe, Service

import click

from fastapi import Body, FastAPI, Request
from fastapi.encoders import jsonable_encoder

from . import version
from .deploy.aws_lambda import AWSLambda
from .deploy.cloud_functions import CloudFunctions
from .deploy.models import DeployConfig, DeployPlatform
from .libs.exceptions import UnsupportedDeployPlatform
from .libs.logging import get_logger
from .monitoring.monitor import watch


app = FastAPI()

logger = get_logger()


@app.get("/monitoring")
async def monitoring_with_get(request: Request) -> Dict[str, str]:
    await watch()
    return jsonable_encoder({})


@app.post("/monitoring")
async def monitoring_with_post(request: Request, body: Dict[str, Any] = Body(...)) -> Dict[str, str]:
    logger.info(body)
    await watch()
    return jsonable_encoder({})


platform = os.environ.get("PLATFORM", "local")

if platform == "local":
    entry_point = None
elif platform == "GCP":
    entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
elif platform == "AWS":
    entry_point = Agraffe.entry_point(app, Service.aws_lambda)
else:
    Exception(f"Unsupported platform of {platform}")


@click.group()
def commands() -> None:
    pass


@commands.command()
def serve() -> None:
    import uvicorn
    uvicorn.run("monitapi:app", host="0.0.0.0", port=8000, reload=True)


@commands.command()
@click.argument("path")
def monitor(path: str) -> None:
    import asyncio
    asyncio.run(watch(open(path)))


@commands.command()
@click.argument("platform")
@click.option("-f", "--file", default="targets.yaml")
@click.option("-n", "--name", default="monitapi")
@click.option("-o", "--options", default="{}")
def deploy(platform: DeployPlatform,
           file: str,
           name: str,
           options: str) -> None:
    import os
    import json
    import shutil
    import git
    if not hasattr(DeployPlatform, platform):
        raise UnsupportedDeployPlatform(platform)
    tmp_dir = TemporaryDirectory(prefix="monitapi")
    repo = git.Repo.clone_from("https://github.com/fealone/monitapi", os.path.join(tmp_dir.name, "monitapi"))
    repo.git.checkout(version.version)
    shutil.copyfile(file, os.path.join(tmp_dir.name, "monitapi/src/targets.yaml"))
    shutil.copyfile(os.path.join(tmp_dir.name, "monitapi/requirements.txt"),
                    os.path.join(tmp_dir.name, "monitapi/src/requirements.txt"))
    if platform == DeployPlatform.cloud_functions:
        cloud_functions_config = DeployConfig(name=name, options=json.loads(options))
        CloudFunctions(tmp_dir).deploy(cloud_functions_config)
    if platform == DeployPlatform.aws_lambda:
        aws_lambda_config = DeployConfig(name=name, options=json.loads(options))
        AWSLambda(tmp_dir).deploy(aws_lambda_config)
