# Agent Design

## Overview

JARVIS OS uses a hierarchical agent architecture. The Commander Agent sits at the top, routing requests to specialist agents. Each agent has defined responsibilities, memory namespaces, and tool access.

## Agent Hierarchy

```
Commander Agent
├── Coding Supervisor
│   ├── Aligna Agent
│   ├── RAF4 Agent
│   └── ODDB Agent
├── Research Agent
├── Office Agent
├── Memory Agent
└── Automation Agent
```

## Commander Agent

The Commander is the central orchestrator. It:

- Receives all user input
- Determines intent and context
- Routes to the appropriate specialist agent
- Returns structured responses
- Manages conversation flow

## Specialist Agents

### Coding Supervisor
Manages all project-specific coding agents. Does not do coding itself — delegates to project agents.

### Project Agents (Aligna, RAF4, ODDB)
Each project agent has:
- Project-specific memory namespace
- Repository path and context
- Coding rules specific to that project
- Task history
- Allowed commands
- Approval rules

### Research Agent
Web research, information gathering, and analysis.

### Office Agent
Document creation, spreadsheet management, presentations. Integrates with OneDrive in Phase 2+.

### Memory Agent
Knowledge management, recall, and organization.

### Automation Agent
Workflow automation, scheduled tasks, and background processes.

## Adding a New Agent

To add a new specialist agent in Phase 2+:

1. Create a new package in `packages/agents/`
2. Implement the agent class with required methods
3. Register it in `packages/agents/registry.py`
4. Add corresponding project config if project-specific

## Phase 1 Agent Status

| Agent | Status | Notes |
|-------|--------|-------|
| Commander | Active | Central routing skeleton |
| Coding Supervisor | Placeholder | Structure ready for Phase 2 |
| Project Agents | Placeholder | Configs exist, no logic |
| Research | Placeholder | Not built yet |
| Office | Placeholder | Not built yet |
| Memory | Active | In-memory store |
| Automation | Placeholder | Not built yet |
