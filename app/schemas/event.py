from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from app.enums import DeviceType


class Metadata(BaseModel):
    page: str
    device_type: str

    @field_validator('device_type', mode='after')
    @classmethod
    def validate_event_type(cls, value: str) -> str:
        try:
            DeviceType(value)
        except ValueError:
            raise ValueError(f'Invalid device type: {value}')
        return value


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
