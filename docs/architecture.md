# JARVIS OS Architecture

## Overview

JARVIS OS is a personal AI operating system. It is not just a chatbot — it will become a persistent digital employee capable of assisting with software development, project management, research, document creation, task management, knowledge management, automation, and future smart-home control.

## High-Level Architecture

```
User
  │
  ▼
┌────────────────┐
│  Commander     │  Central orchestrator - routes all requests
│  Agent         │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│  Safety        │  Classifies actions as SAFE / APPROVAL_REQUIRED / BLOCKED
│  Controller    │
└───────┬────────┘
        │
        ▼
┌─────────────────────────────────────┐
│        Specialist Agents            │
│                                     │
│  Coding Supervisor                  │
│    ├── Aligna Agent                 │
│    ├── RAF4 Agent                   │
│    └── ODDB Agent                   │
│  Research Agent                     │
│  Office Agent                       │
│  Memory Agent                       │
│  Automation Agent                   │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│        Tools / Services             │
│                                     │
│  Filesystem   Memory   Git          │
│  Models       Docker   Browser      │
│  Terminal     Office   Projects     │
└─────────────────────────────────────┘
```

## Repository Structure

```
jarvis-os/
├── apps/
│   ├── api/          # FastAPI backend
│   ├── web/          # Next.js frontend
│   └── worker/       # Background task worker (Phase 2+)
├── packages/
│   ├── agents/       # Agent definitions and registry
│   ├── common/       # Shared utilities (logging, helpers)
│   ├── memory/       # Memory storage and retrieval
│   ├── models/       # Model routing and provider interfaces
│   ├── projects/     # Project registry and configs
│   ├── safety/       # Safety Controller
│   └── tools/        # Tool registry
├── docker/           # Docker configs
├── docs/             # Documentation
└── scripts/          # Utility scripts
```

## Key Design Decisions

### Monorepo Structure
All code lives in one repository. Shared packages are local imports, not published packages. This keeps things simple during development and makes it easy to refactor across boundaries.

### Docker for Infrastructure, Local Dev for Code
PostgreSQL, Redis, and Qdrant run in Docker containers. The API and frontend run locally during development for fast iteration. Docker Compose can run the full stack when needed.

### Safety First
Every action is classified by the Safety Controller before execution. This prevents accidental damage and ensures the user always has control.

### Modular Agent Architecture
Each specialist agent is a self-contained module with its own memory, rules, and tool access. New agents can be added by creating a new module and registering it.

## Phase 1 Scope

Phase 1 is a working foundation:

- FastAPI backend with all core endpoints
- Next.js frontend with dashboard and chat interface
- Docker Compose for PostgreSQL, Redis, Qdrant
- Commander Agent skeleton
- Safety Controller skeleton
- Memory Store (in-memory for Phase 1)
- Model Router with provider placeholders
- Tool Registry with safe stubs
- Project Registry with starter configs
- Basic logging
- Documentation

## Phase 2+ (Not Building Yet)

- Real LLM provider integration
- Coding automation
- Office automation
- Voice interface
- Home Assistant integration
- Production authentication
- Complex autonomous workflows
- OneDrive integration
