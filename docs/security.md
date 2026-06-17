# JARVIS OS Security

## Overview

Security in JARVIS OS is multi-layered. The Safety Controller is the primary gatekeeper, but secrets management, API key handling, and physical access controls are equally important.

## API Keys

- All API keys are stored in `.env` file — never committed to Git
- `.env.example` contains placeholders with no real values
- `.gitignore` excludes `.env` from version control
- Phase 1 works without any API keys using mock responses

## Safety Controller

The Safety Controller classifies every action before execution:

| Classification | Description | Examples |
|---------------|-------------|---------|
| **SAFE** | No restrictions | Read file, search memory, generate response |
| **APPROVAL_REQUIRED** | User must approve | Write files, run terminal commands, deploy code |
| **BLOCKED** | Never allowed | Format disk, delete system folders, factory reset |

## Tool Risk Levels

Each tool in the registry has a risk level:

- **SAFE** tools can be called automatically
- **APPROVAL_REQUIRED** tools pause and request user confirmation
- **BLOCKED** tools are not implemented in any phase

## Workspace Isolation

JARVIS OS is designed to run within `C:\JARVIS` on Windows. All file operations should be constrained to this directory tree. The Safety Controller enforces this boundary.

## Future Security Enhancements (Phase 2+)

- Authentication and session management
- Audit logging of all tool calls
- Encrypted memory storage
- Network-level access controls
- Container security hardening
