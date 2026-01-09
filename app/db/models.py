import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
from app.enums import DeviceType


class EventsOrm(Base):
    __tablename__: str = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str]
    user_id: Mapped[int]
    sent_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    page: Mapped[str]
    device_type: Mapped[DeviceType]

    def __repr__(self):
        return (f'id = {self.id} \n'
                f'event_type = {self.event_type} \n'
                f'user_id = {self.user_id} \n'
                f'sent_at = {self.sent_at} \n'
                f'page = {self.page} \n'
                f'device_type = {self.device_type} \n')
