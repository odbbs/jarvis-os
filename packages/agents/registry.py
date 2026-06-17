"""
Agent Registry - central list of all available agents.
"""

import logging

logger = logging.getLogger("jarvis.agents.registry")


class AgentRegistry:
    """Registry of all specialist agents in the system."""

    def __init__(self):
        self._agents = {
            "commander": {
                "name": "Commander",
                "description": "Central orchestrator - routes requests to specialist agents",
                "status": "active",
            },
            "coding-supervisor": {
                "name": "Coding Supervisor",
                "description": "Oversees all project-specific coding agents",
                "status": "placeholder",
            },
            "project-agent": {
                "name": "Project Agent",
                "description": "Manages project-specific tasks and context",
                "status": "placeholder",
            },
            "research": {
                "name": "Research",
                "description": "Web research and information gathering",
                "status": "placeholder",
            },
            "office": {
                "name": "Office",
                "description": "Document creation, spreadsheets, presentations",
                "status": "placeholder",
            },
            "memory": {
                "name": "Memory",
                "description": "Knowledge management and recall",
                "status": "active",
            },
            "automation": {
                "name": "Automation",
                "description": "Workflow automation and scheduled tasks",
                "status": "placeholder",
            },
        }

    def list_all(self) -> list:
        return [v for v in self._agents.values()]

    def get(self, agent_id: str) -> dict | None:
        return self._agents.get(agent_id)
