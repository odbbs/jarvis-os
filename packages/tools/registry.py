"""
Tool Registry - modular tool definitions for JARVIS OS.

Each tool has a name, description, risk level, and schema placeholders.
Phase 1: safe stubs only. Dangerous tools are not implemented.
"""

import logging

logger = logging.getLogger("jarvis.tools.registry")

RISK_SAFE = "SAFE"
RISK_APPROVAL = "APPROVAL_REQUIRED"
RISK_BLOCKED = "BLOCKED"


class ToolRegistry:
    """Registry of all available tools."""

    def __init__(self):
        self._tools = {
            "filesystem.read": {
                "name": "filesystem.read",
                "description": "Read a file from the workspace",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"content": {"type": "string"}}},
            },
            "filesystem.write": {
                "name": "filesystem.write",
                "description": "Write content to a file",
                "risk_level": RISK_APPROVAL,
                "requires_approval": True,
                "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"success": {"type": "boolean"}}},
            },
            "filesystem.search": {
                "name": "filesystem.search",
                "description": "Search for files or content in the workspace",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"pattern": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"results": {"type": "array"}}},
            },
            "git.status": {
                "name": "git.status",
                "description": "Check git repository status",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"status": {"type": "string"}}},
            },
            "git.diff": {
                "name": "git.diff",
                "description": "View unstaged changes in a git repository",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"diff": {"type": "string"}}},
            },
            "terminal.run": {
                "name": "terminal.run",
                "description": "Execute a terminal command",
                "risk_level": RISK_APPROVAL,
                "requires_approval": True,
                "input_schema": {"type": "object", "properties": {"command": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"stdout": {"type": "string"}, "stderr": {"type": "string"}}},
            },
            "memory.search": {
                "name": "memory.search",
                "description": "Search stored memories",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"query": {"type": "string"}, "namespace": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"results": {"type": "array"}}},
            },
            "memory.save": {
                "name": "memory.save",
                "description": "Save a memory record",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"content": {"type": "string"}, "namespace": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"id": {"type": "string"}, "saved": {"type": "boolean"}}},
            },
            "model.call": {
                "name": "model.call",
                "description": "Call an LLM model with a prompt",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"model": {"type": "string"}, "prompt": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"response": {"type": "string"}}},
            },
            "project.list": {
                "name": "project.list",
                "description": "List all registered projects",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {}},
                "output_schema": {"type": "object", "properties": {"projects": {"type": "array"}}},
            },
            "project.get": {
                "name": "project.get",
                "description": "Get details about a specific project",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"project_id": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"project": {"type": "object"}}},
            },
            "approval.request": {
                "name": "approval.request",
                "description": "Request user approval for an action",
                "risk_level": RISK_SAFE,
                "requires_approval": False,
                "input_schema": {"type": "object", "properties": {"action": {"type": "string"}, "reason": {"type": "string"}}},
                "output_schema": {"type": "object", "properties": {"approved": {"type": "boolean"}}},
            },
        }

    def list_all(self) -> list:
        return [v for v in self._tools.values()]

    def get(self, tool_id: str) -> dict | None:
        return self._tools.get(tool_id)
