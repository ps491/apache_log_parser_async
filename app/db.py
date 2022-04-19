from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
# from pathlib
from communication_center.dbm.conn.tools import (POSTGRES_HOST, POSTGRES_PORT, USER, PASSWORD, DB_NAME)


class DataBaseClass:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_pool(self):
        self.pool = await asyncpg.create_pool('Ваше подключение')

    async def execute(self, command: str, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
        return result


class PostgresConnector:
    def __init__(self):
        self.CONNECTION = None

    async def try_to_connect(self):
        self.CONNECTION = await asyncpg.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME)

    async def close_connection(self):
        await self.CONNECTION.close()

    async def fetch(self, query, *args):
        if self.CONNECTION is None:
            await self.try_to_connect()
            result = await self.CONNECTION.fetch(query, *args)
            await self.CONNECTION.close()
            return result

    def db_connector(func):
        async def wrapper(*args, kwargs):
            connection = PostgresConnector()
            await connection.try_to_connect()
            result = await func(connection, *args, kwargs)
            await connection.close_connection()
            return result

        return wrapper
