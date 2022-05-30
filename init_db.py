import asyncio
import asyncpg

import json





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
            "user" varchar(30) not null,
            "time" timestamp,
            "method" varchar(30),
            url varchar(600) not null,
            protocol varchar(30) not null,
            status varchar(30) not null,
            size varchar(30) not null,
            referrer varchar(600) not null,
            agent varchar(600) not null,
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
        INSERT INTO logs(ip, indent, "user", "time", "method", url, protocol, status, size, referrer, agent, other)
        VALUES('13.66.139.0', '-', '-', '19/Dec/2020:13:57:26 +0100', 'GET', '/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53', 'HTTP/1.1', '200', '32653', '-', 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', '-'),
        ('42.236.10.125', '-', '-', '19/Dec/2020:15:23:11 +0100', 'GET', '/templates/_system/css/general.css', 'HTTP/1.1', '404', '239', 'http://www.almhuette-raith.at/', 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 baidu.sogo.uc.UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN', '-')
        ''')

    await conn.execute('''
        INSERT INTO log_files(file, processed) 
        VALUES($1, $2)
    ''', '/url/url', True)

    await conn.close()


if __name__ == '__main__':
    from app.settings.config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, DB_NAME

    USER_DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}'

    asyncio.get_event_loop().run_until_complete(setup_db(USER_DB_URL))
    asyncio.get_event_loop().run_until_complete(insert_test_data(USER_DB_URL))
