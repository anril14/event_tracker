from fastapi import APIRouter

from app.service.event_service import add_event, validate_event, get_all_events

from app.schemas.event import Event

print('Event router loaded')

event_router = APIRouter(
    prefix='/events'
)


@event_router.post('/')
def create_event(event: Event):
    validated = validate_event(event)
    return add_event(validated)


@event_router.get('/')
def get_events() -> list[Event]:
    return get_all_events()
