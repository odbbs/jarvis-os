"""
Project Registry - manages all project configurations.

Phase 1: config structures only. No real repository connections.
"""

import logging

logger = logging.getLogger("jarvis.projects.registry")


class ProjectRegistry:
    """Registry of all known projects."""

    def __init__(self):
        self._projects = {
            "auto": {
                "id": "auto",
                "name": "Auto",
                "description": "Automatic project detection",
                "status": "active",
                "repo_path": "",
                "server_notes": "",
                "deployment_notes": "",
                "coding_rules": [],
            },
            "aligna": {
                "id": "aligna",
                "name": "Aligna",
                "description": "Aligna - Career Readiness Assessment Platform",
                "status": "placeholder",
                "repo_path": "",
                "server_notes": "",
                "deployment_notes": "",
                "coding_rules": [],
            },
            "raf4": {
                "id": "raf4",
                "name": "RAF4",
                "description": "RAF4 Project",
                "status": "placeholder",
                "repo_path": "",
                "server_notes": "",
                "deployment_notes": "",
                "coding_rules": [],
            },
            "oddb": {
                "id": "oddb",
                "name": "ODDB",
                "description": "ODDB Project",
                "status": "placeholder",
                "repo_path": "",
                "server_notes": "",
                "deployment_notes": "",
                "coding_rules": [],
            },
        }

    def list_all(self) -> list:
        return [v for v in self._projects.values()]

    def get(self, project_id: str) -> dict | None:
        return self._projects.get(project_id)
