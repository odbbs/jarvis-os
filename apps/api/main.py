# JARVIS OS API
# Phase 1 - Foundation

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import health, chat, models, agents, projects, memory, tools, logs

logging.basicConfig(
    level=getattr(logging, settings.jarvis_log_level),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("jarvis.api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("JARVIS OS API starting up (Phase 1)")
    logger.info(f"Environment: {settings.jarvis_env}")
    logger.info(f"Debug: {settings.jarvis_debug}")
    yield
    logger.info("JARVIS OS API shutting down")


app = FastAPI(
    title="JARVIS OS API",
    description="Personal AI Operating System - Phase 1",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(chat.router)
app.include_router(models.router)
app.include_router(agents.router)
app.include_router(projects.router)
app.include_router(memory.router)
app.include_router(tools.router)
app.include_router(logs.router)
