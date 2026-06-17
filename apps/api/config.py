from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Keys
    openai_api_key: str = ""
    deepseek_api_key: str = ""
    moonshot_api_key: str = ""
    anthropic_api_key: str = ""

    # Database
    database_url: str = "postgresql+asyncpg://jarvis:jarvis@localhost:5432/jarvis"
    database_url_sync: str = "postgresql://jarvis:jarvis@localhost:5432/jarvis"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = ""

    # JARVIS
    jarvis_env: str = "development"
    jarvis_debug: bool = True
    jarvis_log_level: str = "INFO"
    jarvis_secret_key: str = "change-this-to-a-random-secret-key"

    # Paths
    jarvis_workspace_root: str = "C:\\JARVIS"
    jarvis_projects_root: str = "C:\\JARVIS\\projects"
    jarvis_memory_root: str = "C:\\JARVIS\\memory"
    jarvis_logs_root: str = "C:\\JARVIS\\logs"

    # Default model
    jarvis_default_model: str = "gpt"

    # API Server
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
