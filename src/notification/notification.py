from typing import Any, Dict, Generator, List
import logging
import sys

from notification.models import NotificationMessage, NotificationTarget, NotificationType
from notification.libs.slack import SlackNotifier


logger = logging.getLogger("monitapi.alert")
for handler in logger.handlers:
    logger.removeHandler(handler)

handler = logging.StreamHandler(sys.stderr)

FORMAT = '%(asctime)s %(levelname)-5.5s [%(name)s] [%(threadName)s] %(message)s'
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)


def get_targets(targets: List[Dict[str, Dict[str, Any]]]) -> Generator[NotificationTarget, None, None]:
    for target in targets:
        yield NotificationTarget(**target)


def notify(message: NotificationMessage, targets_config: Dict[str, Any]) -> None:
    targets = get_targets(targets_config.get("notification_targets", []))
    for target in targets:
        if target.type == NotificationType.slack:
            notifier = SlackNotifier(target)
            notifier.notify(message)
    logger.error(message.dict())
