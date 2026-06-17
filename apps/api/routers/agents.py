from fastapi import APIRouter

from packages.agents.registry import AgentRegistry

router = APIRouter(prefix="/agents", tags=["Agents"])


@router.get("")
async def list_agents():
    registry = AgentRegistry()
    return {"agents": registry.list_all()}
