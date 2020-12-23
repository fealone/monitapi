import logging
import sys

alert_logger = None
standard_logger = None


def get_alert_logger() -> logging.Logger:
    global alert_logger
    if alert_logger is None:
        alert_logger = logging.getLogger("monitapi.alert")
    for handler in alert_logger.handlers:
        alert_logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stderr)

    FORMAT = '%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] %(message)s'
    handler.setFormatter(logging.Formatter(FORMAT))
    alert_logger.addHandler(handler)
    alert_logger.propagate = False
    return alert_logger


def get_logger() -> logging.Logger:
    global standard_logger
    if standard_logger is None:
        standard_logger = logging.getLogger("monitapi")
    for handler in standard_logger.handlers:
        standard_logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stderr)

    FORMAT = '%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] %(message)s'
    handler.setFormatter(logging.Formatter(FORMAT))
    standard_logger.addHandler(handler)
    standard_logger.setLevel(logging.INFO)
    standard_logger.propagate = False
    return standard_logger
