from pydantic import BaseModel


class NotificationMessage(BaseModel):
    expected_status_code: int
    status_code: int
    message: str
