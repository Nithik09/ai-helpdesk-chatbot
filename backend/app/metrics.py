from sqlalchemy import func
from app.models import ChatLog, Ticket


def build_metrics(db):
    total_logs = db.query(func.count(ChatLog.id)).scalar()
    avg_latency = db.query(func.avg(ChatLog.latency_ms)).scalar() or 0
    total_tickets = db.query(func.count(Ticket.id)).scalar()
    by_status = db.query(Ticket.status, func.count(Ticket.id)).group_by(Ticket.status).all()

    return {
        "total_logs": total_logs,
        "avg_latency_ms": int(avg_latency),
        "total_tickets": total_tickets,
        "tickets_by_status": {status: count for status, count in by_status},
    }
