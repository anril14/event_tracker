from pydantic import BaseModel
from datetime import datetime

class Metadata(BaseModel):
    page: str
    device_type: str

class Event(BaseModel):
    id: int | None = None
    event_type: str
    user_id: str
    timestamp: datetime
    metadata: Metadata
