# JARVIS OS

**Personal AI Operating System — Phase 1**

JARVIS OS is a custom-built AI assistant platform. It will become a persistent digital employee capable of assisting with software development, project management, research, document creation, task management, knowledge management, and automation.

This is **Phase 1** — a working foundation with a FastAPI backend, Next.js frontend, Docker services, and a modular agent architecture.

## Quick Start

### Prerequisites

- Windows 11 (or WSL2/Linux)
- [Git](https://git-scm.com/)
- [Python 3.13+](https://www.python.org/)
- [Node.js v24+](https://nodejs.org/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with WSL2 backend)
- [VS Code](https://code.visualstudio.com/) (recommended)

### 1. Clone and Setup

```powershell
cd C:\JARVIS\workspace
git clone <repo-url> jarvis-os
cd jarvis-os
copy .env.example .env
```

Edit `.env` to add your API keys (optional for Phase 1 — mock responses work without them).

### 2. Start Docker Services

```powershell
docker compose up -d postgres redis qdrant
```

This starts PostgreSQL (port 5432), Redis (6379), and Qdrant (6333).

### 3. Start the Backend

```powershell
cd apps\api
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API is now available at http://localhost:8000.

### 4. Start the Frontend

In a new terminal:

```powershell
cd apps\web
npm install
npm run dev
```

The frontend is now available at http://localhost:3000.

### 5. Open the Dashboard

Navigate to http://localhost:3000/dashboard.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/chat` | Send a message to JARVIS |
| GET | `/models` | List available models |
| GET | `/agents` | List specialist agents |
| GET | `/projects` | List registered projects |
| GET | `/projects/{id}` | Get project details |
| GET | `/memory/search` | Search memory |
| POST | `/memory/save` | Save to memory |
| GET | `/memory/recent` | Recent memory entries |
| GET | `/tools` | List available tools |
| GET | `/logs` | View recent logs |

### Chat Endpoint

```json
POST /chat
{
  "message": "Hello, JARVIS",
  "model": "auto",
  "agent": "commander",
  "project": "auto",
  "mode": "chat"
}
```

Response:

```json
{
  "response": "...",
  "model": "gpt",
  "agent": "commander",
  "project": "auto",
  "mode": "chat",
  "tool_calls": [],
  "approval_required": false,
  "timestamp": "2026-06-17T..."
}
```

## Project Structure

```
jarvis-os/
├── apps/
│   ├── api/          # FastAPI backend
│   ├── web/          # Next.js frontend
│   └── worker/       # Background worker (Phase 2+)
├── packages/
│   ├── agents/       # Agent definitions and registry
│   ├── common/       # Shared utilities
│   ├── memory/       # Memory storage
│   ├── models/       # Model routing
│   ├── projects/     # Project registry
│   ├── safety/       # Safety Controller
│   └── tools/        # Tool registry
├── docker/
├── docs/
├── scripts/
├── .env.example
├── docker-compose.yml
└── README.md
```

## Available Models

| Model | Provider | Default |
|-------|----------|---------|
| GPT | OpenAI | ✅ Yes — primary model |
| Claude Code | Anthropic | ❌ No — escalation only |
| DeepSeek | DeepSeek | ❌ No — secondary |
| Moonshot | Moonshot/Kimi | ❌ No — long context |

## Available Agents

| Agent | Status |
|-------|--------|
| Commander | Active |
| Coding Supervisor | Placeholder |
| Project Agent | Placeholder |
| Research | Placeholder |
| Office | Placeholder |
| Memory | Active |
| Automation | Placeholder |

## Available Projects

| Project | Status |
|---------|--------|
| Auto | Active |
| Aligna | Placeholder |
| RAF4 | Placeholder |
| ODDB | Placeholder |

## Configuration

Copy `.env.example` to `.env` and configure:

```env
OPENAI_API_KEY=sk-...
DEEPSEEK_API_KEY=sk-...
MOONSHOT_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...
DATABASE_URL=postgresql+asyncpg://jarvis:jarvis@localhost:5432/jarvis
REDIS_URL=redis://localhost:6379/0
QDRANT_URL=http://localhost:6333
JARVIS_ENV=development
JARVIS_DEFAULT_MODEL=gpt
```

## What's Not Built Yet (Phase 2+)

- Real LLM provider integration (mock responses in Phase 1)
- PostgreSQL/Qdrant persistent storage
- Coding automation and tool execution
- Project agent intelligence
- Office document automation
- Voice interface
- Authentication and user management
- Background worker tasks
- Home Assistant integration
- OneDrive integration

## License

Private — JARVIS OS is a personal project.
