"""
Safety Controller - classifies actions as SAFE, APPROVAL_REQUIRED, or BLOCKED.

Phase 1: simple rule-based classification.
"""

import logging
import re

logger = logging.getLogger("jarvis.safety.controller")

SAFE = "SAFE"
APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
BLOCKED = "BLOCKED"


class SafetyController:
    """Classifies actions based on risk level."""

    def __init__(self):
        # Keywords that trigger blocking
        self._blocked_patterns = [
            r"\bformat\s+(disk|drive|c:|d:)\b",
            r"\bdelete\s+(windows|system32)\b",
            r"\bfactory\s+reset\b",
            r"\bdestroy\s+(repo|repository)\b",
            r"\bmodify\s+password\b",
            r"\bremove\s+all\s+(files|data)\b",
            r"\brm\s+-rf\s+/\b",
        ]

        # Keywords that require approval
        self._approval_patterns = [
            r"\bwrite\s+(file|to)\b",
            r"\binstall\b",
            r"\brun\s+command\b",
            r"\bexecute\b",
            r"\bdeploy\b",
            r"\bedit\s+repo\b",
            r"\bdelete\s+(file|document)\b",
            r"\bmodify\s+(config|configuration)\b",
            r"\bgit\s+push\b",
            r"\bgit\s+commit\b",
            r"\brm\b",
            r"\bmv\b",
            r"\bchmod\b",
        ]

    def classify(self, message: str) -> str:
        """Classify a message/action as SAFE, APPROVAL_REQUIRED, or BLOCKED."""
        msg_lower = message.lower()

        # Check blocked patterns first
        for pattern in self._blocked_patterns:
            if re.search(pattern, msg_lower):
                logger.warning(f"BLOCKED action detected: {message[:100]}")
                return BLOCKED

        # Check approval patterns
        for pattern in self._approval_patterns:
            if re.search(pattern, msg_lower):
                logger.info(f"APPROVAL_REQUIRED for: {message[:100]}")
                return APPROVAL_REQUIRED

        return SAFE
