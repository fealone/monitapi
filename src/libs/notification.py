import logging
import sys

from models import NotificationMessage


logger = logging.getLogger("monitapi.alert")
for handler in logger.handlers:
    logger.removeHandler(handler)

handler = logging.StreamHandler(sys.stderr)

FORMAT = '%(asctime)s %(levelname)-5.5s [%(name)s] [%(threadName)s] %(message)s'
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)


def notify(message: NotificationMessage) -> None:
    logger.error(message.dict())
