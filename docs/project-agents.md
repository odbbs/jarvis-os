# Project Agents

## Overview

JARVIS OS does not use a single generic coding agent. Instead, each project gets its own dedicated agent with project-specific context, rules, and memory. This prevents context pollution between projects and allows tailored behavior for each codebase.

## Architecture

```
Coding Supervisor
├── Aligna Agent
│   ├── Project Memory
│   ├── Repo Path
│   ├── Coding Rules
│   └── Server/Deployment Notes
├── RAF4 Agent
│   ├── Project Memory
│   ├── Repo Path
│   ├── Coding Rules
│   └── Server/Deployment Notes
└── ODDB Agent
    ├── Project Memory
    ├── Repo Path
    ├── Coding Rules
    └── Server/Deployment Notes
```

## Project Config Example

Each project agent has a configuration like:

```json
{
  "id": "aligna",
  "name": "Aligna",
  "repo_path": "C:\\JARVIS\\projects\\aligna",
  "server_notes": "Dev: localhost, Prod: example.com",
  "deployment_notes": "Deploy via deploy script",
  "coding_rules": [
    "Never run migrate:fresh",
    "Always write tests",
    "Follow Laravel conventions"
  ],
  "memory_namespace": "project:aligna",
  "allowed_commands": [
    "php artisan",
    "npm run",
    "git status"
  ]
}
```

## Starter Projects (Phase 1)

Phase 1 includes configuration stubs for:

| Project | Description |
|---------|-------------|
| **Aligna** | Career Readiness Assessment Platform |
| **RAF4** | RAF4 Project |
| **ODDB** | ODDB Project |

In Phase 1, these are registry entries only — no real repository connections, no agent logic. The structure is ready for Phase 2 when project agents are implemented.

## Adding a New Project Agent

To add a new project agent later:

1. Add the project config to `packages/projects/registry.py`
2. Create a memory namespace `project:<project-id>`
3. Add project-specific coding rules
4. Link the project repo path
5. (Phase 2+) Create the agent module in `packages/agents/`
