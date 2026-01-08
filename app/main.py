import uvicorn

import os
from fastapi import FastAPI

from app.api.events import event_router

app = FastAPI()

app.include_router(router=event_router)
