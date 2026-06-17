from fastapi import APIRouter
from pydantic import BaseModel

from packages.memory.store import MemoryStore

router = APIRouter(prefix="/memory", tags=["Memory"])
store = MemoryStore()


class MemoryItem(BaseModel):
    type: str = "note"
    namespace: str = "personal"
    content: str
    metadata: dict = {}


@router.get("/search")
async def search_memory(q: str = "", namespace: str = "", limit: int = 10):
    results = store.search(query=q, namespace=namespace, limit=limit)
    return {"results": results}


@router.post("/save")
async def save_memory(item: MemoryItem):
    result = store.save(
        type=item.type,
        namespace=item.namespace,
        content=item.content,
        metadata=item.metadata,
    )
    return {"saved": result}


@router.get("/recent")
async def recent_memory(namespace: str = "", limit: int = 20):
    results = store.list_recent(namespace=namespace, limit=limit)
    return {"results": results}
