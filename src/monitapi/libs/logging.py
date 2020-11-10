import logging
import sys

alert_logger = logging.getLogger("monitapi.alert")
standard_logger = logging.getLogger("monitapi")

for logger in (alert_logger, standard_logger):
    for handler in logger.handlers:
        logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stderr)

    FORMAT = '%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] %(message)s'
    handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(handler)

standard_logger.setLevel(logging.INFO)


def get_alert_logger() -> logging.Logger:
    return alert_logger


def get_logger() -> logging.Logger:
    return standard_logger
