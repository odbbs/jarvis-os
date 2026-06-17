from fastapi import APIRouter

from packages.models.router import ModelRouter

router = APIRouter(prefix="/models", tags=["Models"])


@router.get("")
async def list_models():
    router = ModelRouter()
    return {"models": router.list_available()}
