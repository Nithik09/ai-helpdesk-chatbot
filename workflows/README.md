# n8n Workflows

Import the JSON files in this folder via **n8n → Workflows → Import from File**.

Required credentials in n8n:
- Postgres credential named `helpdesk-postgres` pointing to `postgres:5432` DB `helpdesk`.

Webhooks created:
- `POST /webhook/helpdesk-ingest`
- `POST /webhook/helpdesk-chat`
- `POST /webhook/create-ticket`
- `POST /webhook/ticket-status`
