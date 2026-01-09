import datetime

import uvicorn

import os
from fastapi import FastAPI

from app.api.events import event_router

# Testing
from app.db.queries.orm import EventSyncORM
from app.enums import DeviceType
from app.schemas.event import InEvent, Metadata

app = FastAPI()

app.include_router(router=event_router)

# TODO: Alembic миграции
EventSyncORM.create_tables()

# Testing
event = InEvent(
    event_type='1',
    metadata=Metadata(
        page='/event',
        device_type=DeviceType('pc')
    ),
    user_id=123,
    sent_at=datetime.datetime.now()
)
EventSyncORM.insert_data(
    event
)
EventSyncORM.insert_data(
    event
)

# print(EventSyncORM.get_data())
