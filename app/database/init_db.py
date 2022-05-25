import asyncio
import asyncpg

import json


from settings.config import POSTGRES_HOST, POSTGRES_PORT, USER, PASSWORD, DB_NAME
USER_DB_URL = f'postgresql://{USER}:{PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}'




async def setup_db(dsn_url):
    conn = await asyncpg.connect(dsn=dsn_url)
    # drop tables
    await conn.execute('''
        DROP TABLE IF EXISTS logs CASCADE;
        DROP TABLE IF EXISTS log_files CASCADE;
    ''')

    # creating logs
    await conn.execute('''
        CREATE TABLE logs(
            id serial PRIMARY KEY,
            ip varchar(30),
            indent varchar(30) not null,
            user varchar(30) not null,
            time timestamp,
            method varchar(30),
            url varchar(30) not null,
            protocol varchar(30) not null,
            status varchar(30) not null,
            referrer varchar(30) not null,
            agent varchar(30) not null,
            other varchar(30) not null
        )
    ''')

    # creating log files
    await conn.execute('''
        CREATE TABLE log_files(
            id serial PRIMARY KEY,
            file varchar(40) not null,
            processed boolean default false
            )
    ''')

    await conn.close()


async def insert_test_data(dsn_url):
    conn = await asyncpg.connect(dsn=dsn_url)
    await conn.execute('''
        INSERT INTO logs(ip, indent, user, time, method, url, protocol, status, referrer, agent, other)
        VALUES('admin@music.store', 'Vasya')
        ''')

    await conn.execute('''
        INSERT INTO log_files(file, processed) 
        VALUES($1, $2)
    ''', '/url/url', True)

    await conn.close()


if __name__ == '__main__':
    print(USER_DB_URL)
    asyncio.get_event_loop().run_until_complete(setup_db(USER_DB_URL))
    asyncio.get_event_loop().run_until_complete(insert_test_data(USER_DB_URL))
