import asyncio
from sqlalchemy import text, insert
from app.db.database import sync_session_factory
from app.db.models import UsersOrm
from app.db.database import sync_engine, Base


def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def insert_data():
    with sync_session_factory() as session:
        user_bobr = UsersOrm(username='bobr')
        user_volk = UsersOrm(username='volk')
        session.add_all([user_bobr, user_volk])
        session.commit()


def get_data():
    with sync_engine.connect() as conn:
        query = text('''
        select *
        from users
        ''')
        print(conn.execute(query).all())


create_tables()
insert_data()
get_data()
