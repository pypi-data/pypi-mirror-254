"""Unhandled exception. When all else fails."""
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class UnhandledException:
    """The result of a check."""

    message: str
    exception: str


def log_unhandled_exception(
    identifier: str,
    message: str,
    formatted_traceback: str,
):
    """Logs an unhandled exception."""
    payload = {
        "payload_type": "unhandled_exception",
        "log_check_name": identifier,
        "message": message,
        "traceback": formatted_traceback,
        "check": "Failed",
    }
    logger.error(payload)
