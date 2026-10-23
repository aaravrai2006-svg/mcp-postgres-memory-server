import os
import json
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class MemoryEntry(BaseModel):
    id: str
    category: str
    content: str
    tags: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PostgresMemoryServer:
    def __init__(self):
        self.memories: Dict[str, MemoryEntry] = {}

    def store_memory(self, category: str, content: str, tags: Optional[List[str]] = None) -> MemoryEntry:
        mem_id = f"mem_{len(self.memories) + 1:04d}"
        entry = MemoryEntry(
            id=mem_id,
            category=category,
            content=content,
            tags=tags or []
        )
        self.memories[mem_id] = entry
        return entry

    def query_memories(self, query: str, limit: int = 5) -> List[MemoryEntry]:
        query_lower = query.lower()
        results = [
            m for m in self.memories.values()
            if query_lower in m.content.lower() or any(query_lower in t.lower() for t in m.tags)
        ]
        return results[:limit]

if __name__ == "__main__":
    server = PostgresMemoryServer()
    server.store_memory("user_preference", "User prefers concise Python 3.12 code", ["python", "style"])
    print("MCP Postgres Memory Server initialized successfully.")
