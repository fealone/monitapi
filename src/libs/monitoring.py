from aiohttp import ClientSession

from models import MonitoringResult, MonitoringTarget


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
                response=await response.text())
