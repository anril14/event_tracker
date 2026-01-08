import asyncio
from sqlalchemy import text, insert
from app.db.database import sync_engine, async_engine
from app.db.models import metadata_obj, users_table


async def get_123():
    async with async_engine.connect() as conn:
        result = await conn.execute(text('select version()'))
        print(result)


# asyncio.run(get_123())

def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


def insert_data():
    with sync_engine.connect() as conn:
        # statement = text('''
        # insert into users
        # (id, username)
        # values
        # (1, 'vadim'),
        # (2, 'egor')
        # ''')
        statement = insert(users_table).values(
            [
                {'username': 'vadim'},
                {'username': 'egor'}
            ]

        )
        conn.execute(statement)
        conn.commit()


def get_data():
    with sync_engine.connect() as conn:
        query = text('''
        select *
        from users
        ''')
        print(conn.execute(query).all())


# create_tables()
# insert_data()
# get_data()
