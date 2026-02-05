# System Architecture (Demo)

## Components
- **Frontend (React + Vite)**: Chat UI with citations and admin panel.
- **FastAPI Backend**: API gateway to n8n, logging, metrics, and data endpoints.
- **n8n**: Orchestrates ingestion, retrieval, and tool calls.
- **Qdrant**: Vector search for document chunks.
- **PostgreSQL**: System of record for users, tickets, logs, feedback.

## Data Flow
1. User sends a message from UI.
2. FastAPI posts to n8n chat webhook.
3. n8n retrieves user role, does vector search in Qdrant.
4. n8n calls LLM helper (demo LLM) with strict prompt rules.
5. n8n returns answer + citations + optional tool intent.
6. FastAPI executes tool workflow in n8n if needed.
7. Result + citations returned to UI and logged.
