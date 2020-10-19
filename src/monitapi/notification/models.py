from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel


class NotificationType(str, Enum):
    slack = "slack"


class NotificationMessage(BaseModel):
    expected_status_code: int
    status_code: int
    message: str
    url: str


class NotificationTarget(BaseModel):
    type: NotificationType
    endpoint: str
    payload: Dict[str, Any]
