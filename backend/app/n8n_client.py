import requests
from app.config import settings


def call_chat_webhook(payload: dict) -> dict:
    resp = requests.post(settings.n8n_chat_webhook_url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def call_create_ticket(payload: dict) -> dict:
    resp = requests.post(settings.n8n_create_ticket_webhook_url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def call_ticket_status(payload: dict) -> dict:
    resp = requests.post(settings.n8n_ticket_status_webhook_url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()
