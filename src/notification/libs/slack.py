import json

from libs.exceptions import NotificationError

from notification.libs.notifier import Notifier
from notification.libs.replace_payload import replace_payload
from notification.models import NotificationMessage

import requests


class SlackNotifier(Notifier):

    def notify(self, message: NotificationMessage) -> None:
        payload = replace_payload(self.payload, message)
        res = requests.post(
                self.endpoint,
                headers={"Content-Type": "applicaton/json"},
                data=json.dumps(payload))
        if res.status_code != 200:
            raise NotificationError(res.content)
