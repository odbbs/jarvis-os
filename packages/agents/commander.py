"""
Commander Agent - Central orchestrator for JARVIS OS.

Receives all user input, decides which agent to route to,
and returns structured results. Phase 1: skeleton only.
"""

import logging

logger = logging.getLogger("jarvis.agents.commander")


class CommanderAgent:
    """Central orchestrator for all agent routing."""

    def __init__(self):
        self.name = "commander"
        self.description = "Central orchestrator - routes requests to specialist agents"

    def process(self, message: str, project: str = "auto", mode: str = "chat") -> dict:
        """Process a user message and determine routing."""
        logger.info(f"Commander processing message (project={project}, mode={mode})")

        return {
            "agent": self.name,
            "project": project,
            "mode": mode,
            "tool_calls": [],
            "requires_approval": False,
        }
