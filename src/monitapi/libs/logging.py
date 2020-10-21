import logging
import sys

logger = logging.getLogger("monitapi.alert")
for handler in logger.handlers:
    logger.removeHandler(handler)

handler = logging.StreamHandler(sys.stderr)

FORMAT = '%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] %(message)s'
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)


def get_logger() -> logging.Logger:
    return logger
