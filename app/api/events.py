from fastapi import APIRouter

from app.service.event_service import add_event, get_all_events

from app.schemas.event import Event, InEvent

print('Event router loaded')

event_router = APIRouter(
    prefix='/events',
    tags=['events']
)


@event_router.post('/', status_code=204)
def create_event(event: InEvent):
    add_event(event)


@event_router.get('/')
def get_events() -> list[Event]:
    return get_all_events()
