from pydantic import BaseModel
from typing import List, Optional, Any


class ChatRequest(BaseModel):
    user_id: int
    question: str


class Citation(BaseModel):
    title: str
    chunk_id: str


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    tool_intent: Optional[dict] = None
    tool_result: Optional[dict] = None


class TicketOut(BaseModel):
    id: int
    title: str
    status: str
    priority: str
    description: str


class LogOut(BaseModel):
    id: int
    user_id: int
    question: str
    answer: str
    sources_json: Optional[str]
    tool_calls_json: Optional[str]
    latency_ms: Optional[int]
    created_at: Any
