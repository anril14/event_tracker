from sqlalchemy import Table, Column, Integer, BigInteger, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base


class UsersOrm(Base):
    __tablename__: str = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


metadata_obj = MetaData()

users_table = Table(
    'users',
    metadata_obj,
    Column('id', BigInteger, primary_key=True),
    Column('username', String)
)
