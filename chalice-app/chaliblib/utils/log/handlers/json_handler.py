import json
import logging
from datetime import datetime, timezone

_LOG_RECORD_ATTRS = frozenset({
    "name", "msg", "args", "levelname", "levelno", "pathname",
    "filename", "module", "exc_info", "exc_text", "stack_info",
    "lineno", "funcName", "created", "msecs", "relativeCreated",
    "thread", "threadName", "processName", "process", "message",
    "taskName",
})


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.message = record.getMessage()
        log_record = {
            "timestamp": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.message,
        }
        extra = {k: v for k, v in record.__dict__.items() if k not in _LOG_RECORD_ATTRS}
        if extra:
            log_record["context"] = extra
        if record.exc_info and record.exc_info[0] is not None:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


class JsonHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.setFormatter(JsonFormatter())
