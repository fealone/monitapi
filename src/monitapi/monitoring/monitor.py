import asyncio
from typing import Any, Dict, Generator, IO, List

from aiohttp import ClientSession

import yaml

from .models import MonitoringResult, MonitoringTarget
from ..libs.exceptions import IncorrectYaml
from ..libs.logging import get_logger
from ..notification.notification import NotificationMessage, notify


logger = get_logger()


def get_targets(targets: List[Dict[str, Dict[str, Any]]]) -> Generator[MonitoringTarget, None, None]:
    for target in targets:
        yield MonitoringTarget(**target)


async def monitor(target: MonitoringTarget) -> MonitoringResult:
    state: bool
    async with ClientSession(
            read_timeout=target.timeout,
            conn_timeout=target.timeout) as session:
        method = getattr(session, target.method.lower())
        error = ""
        response = None
        is_retry = False
        for i in range(target.retry):
            is_success = True
            if is_retry:
                await asyncio.sleep(target.retry_wait)
            try:
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
            except Exception as e:
                error = str(e)
                is_success = False
                logger.warning(("Monitor failed. "
                                f"Target: {target.url}, "
                                f"Expect: {target.status_code}"))
                is_retry = True
                continue
            if response.status != target.status_code:
                is_success = False
                logger.warning(("Monitor failed. "
                                f"Target: {target.url}, "
                                f"Status: {response.status}, "
                                f"Expect: {target.status_code}"))
                is_retry = True
                continue
            if is_success:
                break
        if is_success:
            state = True
        else:
            state = False
        return MonitoringResult(
                expected_status_code=target.status_code,
                status_code=response.status if response else 0,
                state=state,
                url=target.url,
                response=await response.text() if response else error)


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
