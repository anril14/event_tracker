from app.schemas.event import Event, Metadata
from app.db.queries.orm import EventSyncORM

_events_list: list[Event] = []


def validate_event(event: Event) -> Event:
    return event


def add_event(event: Event) -> Event:
    _events_list.append(event)
    return event


def get_all_events() -> list[Event]:
    orm_events = EventSyncORM.get_data()
    result_events: list[Event] = []
    for event in orm_events:
        result_events.append(
            Event(
                id=event.id,
                event_type=event.event_type,
                user_id=event.user_id,
                sent_at=event.sent_at,
                metadata=Metadata(
                    page=event.page,
                    device_type=event.device_type
                )
            )
        )
    return result_events
