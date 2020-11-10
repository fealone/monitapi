from typing import Any, Dict, Generator, List

from .libs.slack import SlackNotifier
from .models import NotificationMessage, NotificationTarget, NotificationType
from ..libs.logging import get_alert_logger


logger = get_alert_logger()


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
