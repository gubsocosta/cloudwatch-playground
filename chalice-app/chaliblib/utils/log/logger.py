import logging
import os
from typing import Optional


class Logger:
    def __new__(cls, app_name: str, handler: Optional[logging.Handler] = None):
        logger = logging.getLogger(app_name)
        logger.setLevel(logging.INFO if os.getenv("APP_ENV") == "production" else logging.DEBUG)

        if handler is not None and not any(type(h) is type(handler) for h in logger.handlers):
            logger.addHandler(handler)

        return logger

