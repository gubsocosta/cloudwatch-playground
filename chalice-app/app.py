import logging
from chalice import Chalice, Response
from datetime import datetime

app = Chalice(app_name='chalice-app')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'], cors=True)
def index():
    return Response(
        body={"message": "Hello from Chalice!"},
    )


@app.route('/logs', methods=['POST'], cors=True)
def test_logs():
    logger.debug("This is an DEBUG log message.")
    logger.info("This is an INFO log message.")
    logger.warning("This is a WARNING log message.")
    logger.error("This is an ERROR log message.")
    logger.critical("This is a CRITICAL log message.")

    return Response(
        body={"message": "Log created successfully."},
    )

@app.route('/logs-with-context', methods=['POST'], cors=True)
def test_logs_with_context():
    body = app.current_request.json_body

    param_1 = body.get("param_1", "default_value_1")
    param_2 = body.get("param_2", "default_value_2")

    context = {
        "param_1": param_1,
        "param_2": param_2,
        "timestamp": datetime.utcnow().isoformat()
    }

    logger.debug("", extra=context)

    return Response(
        body={"message": "Log with context created successfully."},
    )

@app.route('/logs-with-exception', methods=['POST'], cors=True)
def test_logs_with_exception():
    try:
        1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        context = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }
        logger.error("An exception occurred", exc_info=True, extra=context)

    return Response(
        body={"message": "Exception log created successfully."},
    )
