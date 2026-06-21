import logging
import sys

from app.core.config import settings


def setup_logger() -> logging.Logger:

    logger = logging.getLogger("inventory_system")

    logger.setLevel(settings.LOG_LEVEL)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger


logger = setup_logger()