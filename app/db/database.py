import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from app.db.config import settings

sync_engine = create_engine(
    url=settings.url_psycopg,
    echo=False
)
async_engine = create_async_engine(
    url=settings.url_asyncpg,
    echo=False
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
