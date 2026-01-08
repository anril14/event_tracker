import asyncio
from sqlalchemy import text, insert, select
from app.db.database import sync_session_factory
from app.db.models import EventsOrm
from app.db.database import sync_engine, Base
from app.schemas.event import Event


class EventSyncORM:

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_data(event: Event):
        with sync_session_factory() as session:
            new_event = EventsOrm(
                event_type=event.event_type,
                user_id=event.user_id,
                page=event.metadata.page,
                device_type=event.metadata.device_type
            )
            session.add(new_event)
            session.commit()

    @staticmethod
    def get_data():
        with sync_session_factory() as session:
            result = session.scalars(select(EventsOrm)).all()
            return result
