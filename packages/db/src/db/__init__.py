__version__ = '0.0.0'

# Export main database classes and functions
from .database import Base, DatabaseService, get_db, get_db_service
from .models import AuditEvent

__all__ = [
    'DatabaseService',
    'get_db_service',
    'get_db',
    'Base',
    'AuditEvent',
    '__version__',
]
