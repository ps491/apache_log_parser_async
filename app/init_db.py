import asyncio
import asyncpg

import json

DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'

USER_CONFIG = get_config()
USER_DB_URL = DSN.format(**USER_CONFIG['postgres'])


async def setup_db(dsn_url):
    conn = await asyncpg.connect(dsn=dsn_url)
    # drop tables
    await conn.execute('''
        DROP TABLE IF EXISTS logs CASCADE;
        DROP TABLE IF EXISTS log_files CASCADE;
    ''')

    # creating logs
    await conn.execute('''
        CREATE TABLE users(
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
            other varchar(30) not null,
               
            
            
            user varchar(30) not null,
            is_active bool not null DEFAULT true,
            api_key uuid DEFAULT uuid_generate_v4()
        );
    ''')

    # creating log files
    await conn.execute('''
        CREATE TABLE albums(
            id serial PRIMARY KEY,
            file varchar(40) not null,
            processed boolean default false,
            
        );
    ''')

    await conn.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(setup_db(USER_DB_URL))

