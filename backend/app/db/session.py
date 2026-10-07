from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL
from app.db.models import Base


def get_engine(database_url: str | None = None):
    url = database_url or DATABASE_URL
    connect_args = {'check_same_thread': False} if url.startswith('sqlite') else {}
    return create_engine(url, connect_args=connect_args, future=True)


def init_db(engine):
    Base.metadata.create_all(bind=engine)


engine = get_engine()
init_db(engine)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
