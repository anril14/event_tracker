from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from app.enums import DeviceType


class Metadata(BaseModel):
    page: str
    device_type: DeviceType


class Event(BaseModel):
    id: int
    event_type: str
    user_id: int
    sent_at: datetime
    metadata: Metadata


class InEvent(BaseModel):
    event_type: str
    user_id: int
    sent_at: datetime
    metadata: Metadata
