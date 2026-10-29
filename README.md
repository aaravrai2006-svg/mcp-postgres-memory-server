<div align="center">

# 🧠 MCP PostgreSQL Semantic Memory Server

[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard_1.0-10B981?style=for-the-badge)](https://modelcontextprotocol.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Python](https://img.shields.io/badge/Python-FastMCP-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![M8ven Score](https://m8ven.ai/badge/mcp/aaravrai2006-svg-mcp-postgres-memory-server-1b8kqf?v=46555ee3afe3ad9e052cfb82a891ece6)](https://m8ven.ai/mcp/aaravrai2006-svg-mcp-postgres-memory-server-1b8kqf?s=readme)
<p align="center">
  <b>A production-grade Model Context Protocol (MCP) server equipping LLMs (Claude, Gemini, Antigravity) with long-term episodic memory, entity graphs, and contextual search.</b>
</p>

</div>

---

## 🛠️ MCP Tools Exposed

1. `store_memory(category, content, tags, metadata)`: Persists an entity observation or episodic memory block.
2. `query_memories(search_query, limit, min_relevance)`: Retrieves top-k semantically relevant memories.
3. `list_entities(filter_tag)`: Traverses discovered agent knowledge graphs.
4. `prune_stale_memories(older_than_days)`: Maintains index freshness.

## 🚀 Installation & Configuration

```json
{
  "mcpServers": {
    "postgres-memory": {
      "command": "python",
      "args": ["-m", "mcp_server.server"],
      "env": {
        "DATABASE_URL": "postgresql://postgres:password@localhost:5432/mcp_memory"
      }
    }
  }
}
```

---
*Authored by [Aarav Rai](https://github.com/aaravrai2006-svg)*
