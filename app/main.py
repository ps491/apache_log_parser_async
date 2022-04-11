import logging
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from aiohttp import web
from aiohttp_swagger3 import SwaggerDocs, SwaggerUiSettings, SwaggerInfo

app = web.Application()
routes = web.RouteTableDef()

log = logging.getLogger(__name__)


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


DataBase = DataBaseClass()


@routes.post("/log/")
async def create_log(request: web.Request) -> web.Response:
    """
    Create log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.delete("/log/")
async def create_log(request: web.Request) -> web.Response:
    """
    Delete log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.patch("/log/")
async def create_log(request: web.Request) -> web.Response:
    """
    Update log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.get("/log/{log_id}/")
async def get_logs(request: web.Request, ) -> web.Response:
    """
    Log Detail

    """
    # result = await DataBase.execute("SELECT username, balance FROM users WHERE chat_id = $1",
    #                                 message.from_user.id, fetchval=True)
    # print('Ваш баланс:', result[0]['balance'])
    # print('Ваш ник:', result[0]['username'])
    return web.json_response({"id": 101, "name": "Lessie"})


app.add_routes(routes)

if __name__ == '__main__':
    s = SwaggerDocs(app,
                    info=SwaggerInfo(
                        title="test app",
                        version="2.2.2",
                        description="test description",
                    ),
                    swagger_ui_settings=SwaggerUiSettings(path="/docs"))
    s.add_routes(routes)
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO,
                        # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                        )
    web.run_app(app, port=7000)
