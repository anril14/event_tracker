from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    id: int | None = None
    event_type: str
    user_id: str
    timestamp: datetime
    metadata: dict
