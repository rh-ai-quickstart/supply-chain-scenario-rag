"""
SQLAdmin configuration for database administration UI

Access the admin panel at: http://localhost:8000/admin
"""

from db import AuditEvent
from sqladmin import Admin, ModelView
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost:5432/supply-chain-scenario-rag"
engine = create_engine(DATABASE_URL, echo=False)


class AuditEventAdmin(ModelView, model=AuditEvent):
    column_list = [
        AuditEvent.id,
        AuditEvent.session_id,
        AuditEvent.action_type,
        AuditEvent.scenario_id,
        AuditEvent.created_at,
    ]
    column_searchable_list = [AuditEvent.session_id, AuditEvent.action_type, AuditEvent.scenario_id]
    column_sortable_list = [AuditEvent.id, AuditEvent.action_type, AuditEvent.created_at]
    column_default_sort = [(AuditEvent.created_at, True)]
    name = "Audit Event"
    name_plural = "Audit Events"
    icon = "fa-solid fa-clipboard-list"


def setup_admin(app):
    """Set up SQLAdmin and mount it to the FastAPI app."""
    admin = Admin(app, engine, title="Supply Chain Scenario RAG Admin")
    admin.add_view(AuditEventAdmin)
    return admin
