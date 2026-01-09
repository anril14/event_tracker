import asyncio
from sqlalchemy import text, insert, select
from app.db.database import sync_session_factory
from app.db.models import EventsOrm
from app.db.database import sync_engine, Base
from app.schemas.event import InEvent, Event, Metadata


class EventSyncORM:

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_data(event: InEvent) -> Event:
        with sync_session_factory() as session:
            new_event = EventsOrm(
                event_type=event.event_type,
                user_id=event.user_id,
                page=event.metadata.page,
                device_type=event.metadata.device_type
            )
            session.add(new_event)
            session.commit()

            return Event(
                id=new_event.id,
                event_type=new_event.event_type,
                user_id=new_event.user_id,
                sent_at=new_event.sent_at,
                metadata=Metadata(
                    page=new_event.page,
                    device_type=new_event.device_type
                )
            )

    @staticmethod
    def get_data() -> list[EventsOrm]:
        with sync_session_factory() as session:
            result = session.scalars(select(EventsOrm)).all()
            return result
