import os
from typing import Dict

from agraffe import Agraffe, Service

from fastapi import FastAPI, Request

from monitoring.monitor import watch

app = FastAPI()


@app.get("/monitoring")
async def monitoring(request: Request) -> Dict[str, str]:
    await watch()
    return {}


platform = os.environ.get("PLATFORM", "local")

if platform == "local":
    pass
elif platform == "GCP":
    entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
elif platform == "AWS":
    entry_point = Agraffe.entry_point(app, Service.aws_lambda)
else:
    Exception(f"Unsupported platform of {platform}")
