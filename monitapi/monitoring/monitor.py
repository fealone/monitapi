import asyncio
from typing import Any, Dict, Generator, IO, List

from aiohttp import ClientSession

import yaml

from .models import MonitoringResult, MonitoringTarget
from ..libs.exceptions import IncorrectYaml
from ..notification.notification import NotificationMessage, notify


def get_targets(targets: List[Dict[str, Dict[str, Any]]]) -> Generator[MonitoringTarget, None, None]:
    for target in targets:
        yield MonitoringTarget(**target)


async def monitor(target: MonitoringTarget) -> MonitoringResult:
    state: bool
    async with ClientSession(
            read_timeout=target.timeout,
            conn_timeout=target.timeout) as session:
        method = getattr(session, target.method.lower())
        if target.body:
            req = method(
                    target.url,
                    headers=target.headers,
                    data=target.body
                    )
        else:
            req = method(
                    target.url,
                    headers=target.headers
                    )
        response = await req
        if response.status == target.status_code:
            state = True
        else:
            state = False
        return MonitoringResult(
                expected_status_code=target.status_code,
                status_code=response.status,
                state=state,
                url=target.url,
                response=await response.text())


async def watch(f: IO = None) -> None:
    if f is None:
        f = open("targets.yaml")
    monitors = []
    try:
        targets_config = yaml.load(f, Loader=yaml.BaseLoader)
        targets = get_targets(targets_config["monitor_targets"])
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
                message=result.response,
                url=result.url),
                targets_config)
