"""
Common utilities - logging, helpers, and shared utilities.
"""

import logging
from datetime import datetime, timezone

logger = logging.getLogger("jarvis.common")

# Simple in-memory log ring buffer for the logs endpoint
_log_buffer = []
_MAX_LOG_ENTRIES = 500


class JarvisLogger:
    """Custom logger that also writes to the in-memory buffer."""

    @staticmethod
    def info(message: str):
        logger.info(message)
        _log_buffer.append({"level": "INFO", "message": message, "timestamp": datetime.now(timezone.utc).isoformat()})
        _trim_buffer()

    @staticmethod
    def warning(message: str):
        logger.warning(message)
        _log_buffer.append({"level": "WARNING", "message": message, "timestamp": datetime.now(timezone.utc).isoformat()})
        _trim_buffer()

    @staticmethod
    def error(message: str):
        logger.error(message)
        _log_buffer.append({"level": "ERROR", "message": message, "timestamp": datetime.now(timezone.utc).isoformat()})
        _trim_buffer()


def _trim_buffer():
    while len(_log_buffer) > _MAX_LOG_ENTRIES:
        _log_buffer.pop(0)


def get_recent_logs(limit: int = 50) -> list:
    return _log_buffer[-limit:]
