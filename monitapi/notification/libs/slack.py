import json

import requests

from .notifier import Notifier
from .replace_payload import replace_payload
from ..models import NotificationMessage
from ...libs.exceptions import NotificationError


class SlackNotifier(Notifier):

    def notify(self, message: NotificationMessage) -> None:
        payload = replace_payload(self.payload, message)
        res = requests.post(
                self.endpoint,
                headers={"Content-Type": "applicaton/json"},
                data=json.dumps(payload))
        if res.status_code != 200:
            raise NotificationError(res.content)
