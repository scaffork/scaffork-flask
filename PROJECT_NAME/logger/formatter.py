import logging
import logging.config
import os

# import regex4ocr
from flask_log_request_id import RequestIDLogFilter
from pythonjsonlogger import jsonlogger

# module variables to configure the logs
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")

LEVEL_MAPPING = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}


class JsonFormatter(jsonlogger.JsonFormatter):
    """
    Formats the logging output to fit a json-like format. Adds
    the 'severity' field instead of 'levelname' for Stackdriver
    logging purposees.
    """

    def __init__(self, fmt: str, *args, **kwargs):
        """
        Initializes the JsonFormatter with the desired format.
        """
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record: dict) -> dict:
        """
        Override of the jsonlogger.JsonFormatter method. Adds Stackdriver's
        severity field.
        """
        log_record["severity"] = log_record["levelname"]
        del log_record["levelname"]

        return log_record


def config_log() -> None:
    """
    Configures the application loggers to follow a json-like format.
    """
    handler = logging.StreamHandler()
    formatter = JsonFormatter(
        "%(message)s %(request_id)s %(name)s %(levelname)s %(lineno)s %(pathname)s %(asctime)s"
    )

    handler.addFilter(RequestIDLogFilter())
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers.clear()  # clears previous handlers for root logger
    root_logger.addHandler(handler)
