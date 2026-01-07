from app.schemas.event import Event

_events_list: list[Event] = []


def validate_event(event: Event) -> Event:
    return event


def add_event(event: Event) -> Event:
    _events_list.append(event)
    return event


def get_all_events() -> list[Event]:
    return _events_list
