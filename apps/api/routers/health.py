from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "JARVIS OS API",
        "version": "0.1.0",
        "phase": 1,
    }
