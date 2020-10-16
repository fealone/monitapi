import json
from typing import Any, Dict

from libs.exceptions import NotificationError

from notification.libs.notifier import Notifier
from notification.models import NotificationMessage

import requests


def replace_payload(payload: Dict[str, Any], message: NotificationMessage) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    for key, value in payload.items():
        if isinstance(value, dict):
            output[key] = replace_payload(value, message)
        if isinstance(value, str):
            output[key] = replace_variable(value, message)
        elif isinstance(value, list):
            output[key] = [replace_variable(v, message) for v in value]
        elif not isinstance(value, dict):
            output[key] = value
    return output


def replace_variable(variable: Any, message: NotificationMessage) -> Any:
    if isinstance(variable, list):
        return [replace_variable(v, message) for v in variable]
    elif isinstance(variable, dict):
        return replace_payload(variable, message)
    elif isinstance(variable, str):
        return variable.replace(
            "{{message}}", message.message).replace(
                "{{status_code}}", str(message.status_code)).replace(
                    "{{expected_status_code}}", str(message.expected_status_code))
    else:
        return variable


class SlackNotifier(Notifier):

    def notify(self, message: NotificationMessage) -> None:
        payload = replace_payload(self.payload, message)
        res = requests.post(
                self.endpoint,
                headers={"Content-Type": "applicaton/json"},
                data=json.dumps(payload))
        if res.status_code != 200:
            raise NotificationError(res.content)
