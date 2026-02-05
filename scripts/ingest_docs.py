import requests

N8N_INGEST_WEBHOOK = "http://localhost:5678/webhook/helpdesk-ingest"
QDRANT_URL = "http://localhost:6333"


def ensure_collection():
    r = requests.put(
        f"{QDRANT_URL}/collections/helpdesk",
        json={"vectors": {"size": 384, "distance": "Cosine"}},
        timeout=30,
    )
    r.raise_for_status()


def ingest():
    r = requests.post(N8N_INGEST_WEBHOOK, timeout=60)
    r.raise_for_status()
    print("Ingest triggered.")


if __name__ == "__main__":
    ensure_collection()
    ingest()
