import logging

LINE_FORMAT = "%(asctime)s - [%(levelname)s] %(name)s - %(message)s"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


class ConsoleHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        formatter = logging.Formatter(fmt=LINE_FORMAT, datefmt=DATE_FORMAT)
        self.setFormatter(formatter)
