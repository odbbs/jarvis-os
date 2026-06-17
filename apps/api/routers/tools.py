from fastapi import APIRouter

from packages.tools.registry import ToolRegistry

router = APIRouter(prefix="/tools", tags=["Tools"])


@router.get("")
async def list_tools():
    registry = ToolRegistry()
    return {"tools": registry.list_all()}
