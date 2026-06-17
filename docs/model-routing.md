# Model Routing

## Overview

JARVIS OS supports multiple LLM providers with intelligent routing. The model router determines which provider to use based on the request context, task type, and configured API keys.

## Available Models

| Model ID | Provider | Priority | Use Case |
|----------|----------|----------|----------|
| `gpt` | OpenAI | 1 (Default) | General chat, coding, planning, writing, research, documents |
| `deepseek` | DeepSeek | 2 | Low-cost coding and reasoning |
| `moonshot` | Moonshot/Kimi | 3 | Long-context analysis, large document/repo reasoning |
| `claude` | Anthropic | 4 (Escalation) | Complex tasks, GPT failure fallback |

## Routing Rules

### GPT (Primary)
- Default for all general interactions
- Used for: chat, coding, planning, writing, research, document generation, project management
- First priority when `Auto` is selected

### Claude Code
- Not the default — escalation model only
- Used when: user explicitly selects Claude Code, user says "use Claude", GPT fails or struggles, task complexity justifies escalation
- Requires explicit selection or escalation request

### DeepSeek
- Secondary coding and reasoning model
- Lower cost alternative for routine coding tasks

### Moonshot/Kimi
- Long-context specialist
- Used for analyzing large codebases, documents, or repositories

## Auto Selection Logic

When the user selects `Auto`, the router:

1. Checks if the requested model has a configured API key
2. Falls back to GPT if no API key is configured
3. Uses the configured default model from `JARVIS_DEFAULT_MODEL`

## Phase 1 Behavior

In Phase 1, all model calls return mock/placeholder responses unless an API key is configured in `.env`. This allows development and testing without incurring API costs.
