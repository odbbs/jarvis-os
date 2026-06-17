from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from packages.safety.controller import SafetyController
from packages.models.router import ModelRouter
from packages.agents.commander import CommanderAgent

router = APIRouter(prefix="/chat", tags=["Chat"])

safety = SafetyController()
commander = CommanderAgent()
model_router = ModelRouter()


class ChatRequest(BaseModel):
    message: str
    model: str = "auto"
    agent: str = "commander"
    project: str = "auto"
    mode: str = "chat"


class ChatResponse(BaseModel):
    response: str
    model: str
    agent: str
    project: str
    mode: str
    tool_calls: list = []
    approval_required: bool = False
    timestamp: str = ""


@router.post("")
async def chat(request: ChatRequest) -> ChatResponse:
    # 1. Safety check
    safety_result = safety.classify(request.message)
    if safety_result == "BLOCKED":
        raise HTTPException(status_code=403, detail="Message blocked by Safety Controller")

    # 2. Route through Commander Agent
    agent_result = commander.process(request.message, request.project, request.mode)

    # 3. Route through model router
    model_result = await model_router.route(
        request.message,
        model=request.model,
        agent=request.agent,
        mode=request.mode,
    )

    return ChatResponse(
        response=model_result["response"],
        model=model_result.get("model_used", request.model),
        agent=request.agent,
        project=request.project,
        mode=request.mode,
        tool_calls=agent_result.get("tool_calls", []),
        approval_required=safety_result == "APPROVAL_REQUIRED",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
