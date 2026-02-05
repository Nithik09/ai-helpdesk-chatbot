from sqlalchemy import Column, Integer, String, Text, Timestamp, ForeignKey, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    path = Column(String, nullable=False)
    allowed_roles = Column(String, nullable=False)


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(Timestamp, nullable=False, server_default=func.now())


class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    sources_json = Column(Text)
    tool_calls_json = Column(Text)
    latency_ms = Column(Integer)
    created_at = Column(Timestamp, nullable=False, server_default=func.now())


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, ForeignKey("chat_logs.id"))
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(Timestamp, nullable=False, server_default=func.now())
