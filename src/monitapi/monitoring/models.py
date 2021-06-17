from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class Method(str, Enum):
    head = "HEAD"
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    options = "OPTIONS"
    patch = "PATCH"


class MonitoringTarget(BaseModel):
    method: Optional[Method]
    url: str
    headers: Dict[str, str] = {}
    body: Optional[bytes]
    timeout: int = 10
    status_code: Optional[int]
    retry: int = 1
    retry_wait: int = 5


class MonitoringResult(BaseModel):
    expected_status_code: int
    status_code: int
    state: bool
    response: str
    url: str
