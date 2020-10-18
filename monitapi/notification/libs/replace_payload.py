from typing import Any, Dict

from ..models import NotificationMessage


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
                    "{{expected_status_code}}", str(message.expected_status_code)).replace(
                            "{{url}}", str(message.url))
    else:
        return variable
