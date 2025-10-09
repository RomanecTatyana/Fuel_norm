"""Підключення до SQLite з корисними PRAGMA."""
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy import event
from .config import DATABASE_URL

def get_engine(url: str | None = None) -> Engine:
    engine = create_engine(url or DATABASE_URL, future=True)
    # Увімкнути foreign_keys та WAL для кожного нового з'єднання
    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("PRAGMA journal_mode = WAL;")
        cursor.execute("PRAGMA synchronous = NORMAL;")
        cursor.close()
    return engine