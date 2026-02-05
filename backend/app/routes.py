import json
import time
import re
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sentence_transformers import SentenceTransformer
from app.schemas import ChatRequest, ChatResponse, TicketOut, LogOut
from app.database import get_db
from app.models import ChatLog, Ticket
from app.n8n_client import call_chat_webhook, call_create_ticket, call_ticket_status
from app.metrics import build_metrics
from app.config import settings

router = APIRouter()
embedder = SentenceTransformer(settings.embedding_model)


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/embed")
def embed(payload: dict):
    texts = payload.get("texts", [])
    if not texts:
        raise HTTPException(status_code=400, detail="texts is required")
    vectors = embedder.encode(texts, normalize_embeddings=True).tolist()
    return {"vectors": vectors}


@router.post("/llm")
def demo_llm(payload: dict):
    question = payload.get("question", "")
    contexts = payload.get("contexts", [])
    if not contexts:
        return {"answer": "I don't know based on the available knowledge base.", "citations": [], "tool_intent": None}

    citations = [{"title": c["title"], "chunk_id": c["chunk_id"]} for c in contexts[:3]]
    answer = "Here is what I found:\n" + "\n".join([f"- {c['text']}" for c in contexts[:3]])

    tool_intent = None
    if "create ticket" in question.lower() or "open ticket" in question.lower():
        priority = "HIGH" if "high" in question.lower() else "MEDIUM"
        tool_intent = {
            "tool_name": "CreateTicketTool",
            "args": {"title": "Helpdesk request", "priority": priority, "description": question},
        }

    match = re.search(r"ticket\s*#?(\d+)", question.lower())
    if "status" in question.lower() and match:
        tool_intent = {"tool_name": "GetTicketStatusTool", "args": {"ticket_id": int(match.group(1))}}

    return {"answer": answer, "citations": citations, "tool_intent": tool_intent}


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    start = time.time()
    payload = call_chat_webhook({"user_id": req.user_id, "question": req.question})

    tool_result = None
    tool_intent = payload.get("tool_intent")

    if tool_intent:
        tool_name = tool_intent.get("tool_name")
        args = tool_intent.get("args", {})
        if tool_name == "CreateTicketTool":
            tool_result = call_create_ticket(args)
        elif tool_name == "GetTicketStatusTool":
            tool_result = call_ticket_status(args)

    latency_ms = int((time.time() - start) * 1000)

    log = ChatLog(
        user_id=req.user_id,
        question=req.question,
        answer=payload.get("answer", ""),
        sources_json=json.dumps(payload.get("citations", [])),
        tool_calls_json=json.dumps(tool_intent) if tool_intent else None,
        latency_ms=latency_ms,
    )
    db.add(log)
    db.commit()

    return ChatResponse(
        answer=payload.get("answer", ""),
        citations=payload.get("citations", []),
        tool_intent=tool_intent,
        tool_result=tool_result,
    )


@router.get("/tickets", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).order_by(Ticket.id.desc()).all()


@router.get("/audit/{log_id}", response_model=LogOut)
def audit_log(log_id: int, db: Session = Depends(get_db)):
    log = db.query(ChatLog).filter(ChatLog.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log


@router.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    return build_metrics(db)
