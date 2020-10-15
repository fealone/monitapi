from abc import ABC, abstractmethod
from typing import Any, Dict

from notification.models import NotificationTarget, NotificationMessage


class Notifier(ABC):

    def __init__(self, target: NotificationTarget):
        self.target = target

    @property
    def endpoint(self) -> str:
        return self.target.endpoint

    @property
    def payload(self) -> Dict[str, Any]:
        return self.target.payload


    @abstractmethod
    def notify(self, message: NotificationMessage) -> None:
        ...
