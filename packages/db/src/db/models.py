"""
Database models for supply-chain-scenario-rag.
"""

from sqlalchemy import JSON, Column, DateTime, Integer, String, Text, func

from .database import Base


class AuditEvent(Base):
    """Append-only audit log for scenario and chat actions."""

    __tablename__ = 'audit_events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(64), nullable=False, index=True)
    action_type = Column(String(32), nullable=False, index=True)
    scenario_id = Column(String(64), nullable=True)
    prompt_excerpt = Column(Text, nullable=True)
    response_metadata = Column(JSON, nullable=True)
    chunk_ids = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False, index=True)

    def __repr__(self) -> str:
        return f'<AuditEvent(id={self.id}, action_type={self.action_type!r})>'
