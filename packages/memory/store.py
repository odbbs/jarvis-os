"""
Memory Store - Phase 1 in-memory storage.

Phase 1 uses a simple in-memory store with text search.
PostgreSQL and Qdrant integration will be added in Phase 2.
"""

import uuid
from datetime import datetime, timezone
import logging

logger = logging.getLogger("jarvis.memory.store")


class MemoryStore:
    """Simple in-memory memory store for Phase 1."""

    def __init__(self):
        self._records = []

    def save(self, type: str = "note", namespace: str = "personal", content: str = "", metadata: dict = None) -> dict:
        record = {
            "id": str(uuid.uuid4()),
            "type": type,
            "namespace": namespace,
            "content": content,
            "metadata": metadata or {},
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        self._records.append(record)
        logger.info(f"Memory saved: {record['id']} ({namespace})")
        return record

    def search(self, query: str = "", namespace: str = "", limit: int = 10) -> list:
        results = self._records[:]

        if namespace:
            results = [r for r in results if r["namespace"] == namespace]

        if query:
            q = query.lower()
            results = [r for r in results if q in r["content"].lower() or q in r["type"].lower()]

        results.sort(key=lambda r: r["created_at"], reverse=True)
        return results[:limit]

    def list_recent(self, namespace: str = "", limit: int = 20) -> list:
        results = self._records[:]
        if namespace:
            results = [r for r in results if r["namespace"] == namespace]
        results.sort(key=lambda r: r["created_at"], reverse=True)
        return results[:limit]
