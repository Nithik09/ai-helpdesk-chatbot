# AI-Powered Helpdesk Chatbot (RAG + n8n)

An AI Helpdesk Chatbot that validates users, retrieves knowledge via RAG, generates grounded answers with citations, and logs tickets with escalation for high-priority issues.

**Stack:** n8n, FastAPI, PostgreSQL, Qdrant, React (optional), Render (optional)

---

## Architecture (Clean + Practical)

**Presentation Layer**
- UI (React) or API client (Postman/curl)

**Orchestration Layer (n8n)**
- Webhook trigger → validate user → embed → vector search → build context → call LLM → return answer + citations
- Ticket workflows: create ticket, check ticket status, escalate high-priority

**Data Layer**
- PostgreSQL: users, tickets, chat logs
- Qdrant: document chunk vectors

---

## Workflow (Request Lifecycle)

**Input JSON**
```json
{"user_id": 1, "question": "Hello"}
```

**Steps**
1. Webhook trigger receives request
2. Validate user + role in PostgreSQL
3. Embed question
4. Vector search in Qdrant (RAG)
5. Build context and call LLM
6. Return answer + citations
7. Ticket workflows for create/status and escalation

---

## Recruiter Quick Test (60 seconds)

**Demo UI:** https://your-demo-url.example

**1) Chat**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"question":"How do I reset my password?"}'
```
**Expected:** Answer with citations.

**2) Admin-only test (blocked for non-admin)**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":3,"question":"Show HR admin policy"}'
```
**Expected:** “I don’t know based on the available knowledge base.”

**3) Create ticket**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":2,"question":"Create ticket: laptop not booting, high priority"}'
```
**Expected:** Tool result with ticket ID or approval pending.

**4) Ticket status**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":2,"question":"Status of ticket #1"}'
```
**Expected:** Status response.

---

## Local Run

1. Create env file:
	- .env.example → .env

2. Start everything:
	```bash
	docker compose up --build
	```

3. Import n8n workflows:
	- n8n → Workflows → Import
	- Import all JSON files in n8n/workflows

4. Create Postgres credential:
	- Name: **helpdesk-postgres**
	- Host: postgres
	- DB: helpdesk
	- User: helpdesk
	- Password: helpdesk

5. Activate workflows in n8n.

6. Production vs Test webhooks:
	- **Test** webhooks use `/webhook-test/` (editor-only)
	- **Production** webhooks use `/webhook/` and require activated workflows

---

## Deploy to Render (Optional)

### Backend service env vars
- DATABASE_URL
- N8N_CHAT_WEBHOOK_URL
- N8N_CREATE_TICKET_WEBHOOK_URL
- N8N_TICKET_STATUS_WEBHOOK_URL
- CORS_ORIGINS
- EMBEDDING_MODEL
- DEMO_SEED

### n8n service env vars
- N8N_BASIC_AUTH_ACTIVE=true
- N8N_BASIC_AUTH_USER
- N8N_BASIC_AUTH_PASSWORD
- N8N_ENCRYPTION_KEY
- N8N_HOST
- N8N_PORT
- WEBHOOK_URL

**Supabase note:** Supabase Direct connection may require IPv6. Use **Session Pooler (IPv4)** for Render.

### Set BACKEND_URL in workflows
- n8n → Settings → Variables → add **BACKEND_URL**
- Example: `https://your-backend.onrender.com`

### Production webhooks
- Use `/webhook/` in production (not `/webhook-test/`)
- Ensure workflows are activated

---

## Observability
- `/metrics` endpoint for counts and latency
- Chat logs stored in PostgreSQL

---

## Notes
- LLM is constrained to answer from retrieved context only.
- This is an IT Helpdesk RAG system.
