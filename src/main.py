import asyncio
import os
from typing import Any, Dict, Generator, List

from agraffe import Agraffe, Service

from fastapi import FastAPI, Request

from libs.exceptions import IncorrectYaml
from libs.monitoring import monitor
from libs.notification import notify

from models import MonitoringTarget, NotificationMessage

import yaml

app = FastAPI()


def get_targets(targets: List[Dict[str, Any]]) -> Generator[MonitoringTarget, None, None]:
    for target in targets:
        yield MonitoringTarget(**target)


@app.get("/monitoring")
async def monitoring(request: Request) -> Dict[str, str]:
    monitors = []
    try:
        targets = get_targets(yaml.load(open("targets.yaml"), Loader=yaml.BaseLoader))
    except Exception:
        raise IncorrectYaml()
    for target in targets:
        task = asyncio.ensure_future(monitor(target))
        monitors.append(task)
    results = await asyncio.gather(*monitors)
    for result in results:
        if result.state is False:
            notify(NotificationMessage(
                expected_status_code=result.expected_status_code,
                status_code=result.status_code,
                message=result.response))
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
