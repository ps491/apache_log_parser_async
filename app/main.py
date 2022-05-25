import logging

from aiohttp import web
from aiohttp_swagger3 import SwaggerDocs, SwaggerUiSettings, SwaggerInfo

from database.db import DataBaseClass

app = web.Application()
routes = web.RouteTableDef()

log = logging.getLogger(__name__)

DataBase = DataBaseClass()


@routes.post("/log/")
async def create_log(request: web.Request) -> web.Response:
    """
    Create log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.delete("/log/")
async def delete_log(request: web.Request) -> web.Response:
    """
    Delete log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.patch("/log/")
async def update_log(request: web.Request) -> web.Response:
    """
    Update log
    """

    return web.json_response({"id": 101, "name": "Lessie"})


@routes.get("/log/{log_id}/")
async def get_log(request: web.Request, ) -> web.Response:
    """
    Log Detail

    """
    # result = await DataBase.execute("SELECT username, balance FROM users WHERE chat_id = $1",
    #                                 message.from_user.id, fetchval=True)
    # print('Ваш баланс:', result[0]['balance'])
    # print('Ваш ник:', result[0]['username'])
    return web.json_response({"id": 101, "name": "Lessie"})


@routes.get("/log/")
async def get_logs(request: web.Request, ) -> web.Response:
    """
    Log Detail

    """
    # result = await DataBase.execute("SELECT username, balance FROM users WHERE chat_id = $1",
    #                                 message.from_user.id, fetchval=True)
    # print('Ваш баланс:', result[0]['balance'])
    # print('Ваш ник:', result[0]['username'])
    return web.json_response([{"id": 101, "name": "Lessie"}, {"id": 101, "name": "Lessie"}])


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
