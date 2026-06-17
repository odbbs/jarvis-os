"""
Model Router - routes requests to the appropriate LLM provider.

Phase 1: returns placeholder/mock responses when no API keys are configured.

Routing logic:
- GPT: default for general chat, coding, planning, writing, research
- Claude Code: escalation model only (explicit selection, GPT failure, complex tasks)
- DeepSeek: secondary low-cost coding/reasoning
- Moonshot: long-context analysis, large document/repo reasoning
"""

import logging
from datetime import datetime, timezone

from config import settings

logger = logging.getLogger("jarvis.models.router")


class ModelRouter:
    """Routes chat requests to the appropriate model provider."""

    PROVIDERS = {
        "auto": {"name": "Auto", "description": "Automatic model selection based on context"},
        "gpt": {"name": "GPT", "description": "OpenAI GPT - primary model"},
        "claude": {"name": "Claude Code", "description": "Anthropic Claude - escalation model"},
        "deepseek": {"name": "DeepSeek", "description": "DeepSeek - low-cost coding/reasoning"},
        "moonshot": {"name": "Moonshot", "description": "Moonshot/Kimi - long-context analysis"},
    }

    ROUTING_RULES = {
        "gpt": {"default": True, "priority": 1},
        "deepseek": {"default": False, "priority": 2},
        "moonshot": {"default": False, "priority": 3},
        "claude": {"default": False, "priority": 4},
    }

    def __init__(self):
        self._api_keys = {
            "gpt": settings.openai_api_key,
            "claude": settings.anthropic_api_key,
            "deepseek": settings.deepseek_api_key,
            "moonshot": settings.moonshot_api_key,
        }

    def list_available(self) -> list:
        return [{"id": k, **v} for k, v in self.PROVIDERS.items()]

    def resolve_model(self, requested: str) -> str:
        """Resolve which model to use based on request and routing rules."""
        if requested and requested != "auto":
            return requested

        # Auto: use the first available model with an API key, or GPT as default
        for model_id, cfg in sorted(self.ROUTING_RULES.items(), key=lambda x: x[1]["priority"]):
            if self._api_keys.get(model_id):
                return model_id

        return "gpt"  # default fallback

    async def route(self, message: str, model: str = "auto", agent: str = "commander", mode: str = "chat") -> dict:
        """Route a message to the appropriate model provider and return a response."""
        resolved = self.resolve_model(model)
        logger.info(f"Routing to model: {resolved} (requested: {model}, agent: {agent}, mode: {mode})")

        # Phase 1: mock response if no real API key configured
        if not self._api_keys.get(resolved):
            return self._mock_response(message, resolved)

        # Phase 2+ will call real providers here
        return self._mock_response(message, resolved)

    def _mock_response(self, message: str, model: str) -> dict:
        """Return a placeholder mock response when no API key is configured."""
        return {
            "response": f"[{self.PROVIDERS.get(model, {}).get('name', model)} mock response]\n\n"
                        f"Received: \"{message}\"\n\n"
                        f"This is a placeholder response. Configure an API key for {model} "
                        f"in your .env file to get real responses.",
            "model_used": model,
            "provider": self.PROVIDERS.get(model, {}).get("name", model),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
