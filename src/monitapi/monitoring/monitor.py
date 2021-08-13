import asyncio
import socket
import time
import uuid
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


async def monitor_http(target: MonitoringTarget) -> MonitoringResult:
    state: bool
    async with ClientSession(
            read_timeout=target.timeout,
            conn_timeout=target.timeout) as session:
        if target.method:
            method = getattr(session, target.method.lower())
        else:
            raise Exception("Required method for monitoring http")
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


async def monitor_stun(target: MonitoringTarget) -> MonitoringResult:
    err = Exception()
    for i in range(target.retry):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setblocking(False)
            host, port = target.url.split("stun:")[1].split(":")
            sock.bind(("0.0.0.0", int(port)))
            mtype = b"\x00\x01"
            msg = b"\x00\x01\x00\x00\xff\xff\xff\xff"
            tid = uuid.uuid4().bytes
            length = bytearray([len(msg)]).rjust(2, b"\x00")
            header = mtype + length + tid
            sock.sendto(header+msg, (host, int(port)))
            in_err = Exception()
            for j in range(int(target.timeout * 2)):
                time.sleep(0.5)
                try:
                    sock.recvfrom(1024)
                    break
                except Exception as e:
                    in_err = e
            else:
                raise in_err
            break
        except Exception as e:
            logger.warning(("Monitor failed. "
                            f"Target: {target.url}"))
            err = e
            time.sleep(target.retry_wait)
    else:
        return MonitoringResult(
                expected_status_code=0,
                status_code=0,
                state=False,
                url=target.url,
                response=str(err))
    return MonitoringResult(
            expected_status_code=0,
            status_code=0,
            state=True,
            url=target.url,
            response="")


async def monitor_tcp(target: MonitoringTarget) -> MonitoringResult:
    err = Exception()
    for i in range(target.retry):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host, port = target.url.split("tcp:")[1].split(":")
            sock.settimeout(target.timeout)
            sock.connect((host, int(port)))
            sock.close()
            break
        except Exception as e:
            logger.warning(("Monitor failed. "
                            f"Target: {target.url}"))
            err = e
            time.sleep(target.retry_wait)
    else:
        return MonitoringResult(
                expected_status_code=0,
                status_code=0,
                state=False,
                url=target.url,
                response=str(err))
    return MonitoringResult(
            expected_status_code=0,
            status_code=0,
            state=True,
            url=target.url,
            response="")


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
        if target.url.startswith("http://") or target.url.startswith("https://"):
            task = asyncio.ensure_future(monitor_http(target))
        elif target.url.startswith("stun:"):
            task = asyncio.ensure_future(monitor_stun(target))
        elif target.url.startswith("tcp:"):
            task = asyncio.ensure_future(monitor_tcp(target))
        else:
            logger.warning(f"Unsupported target type. target: {target.url}")
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
