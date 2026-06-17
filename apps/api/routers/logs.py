from fastapi import APIRouter
from pydantic import BaseModel

from packages.common.logger import get_recent_logs

router = APIRouter(prefix="/logs", tags=["Logs"])


class LogEntry(BaseModel):
    level: str = "INFO"
    message: str = ""


@router.get("")
async def get_logs(limit: int = 50):
    logs = get_recent_logs(limit=limit)
    return {"logs": logs}
