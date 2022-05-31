import logging

from aiohttp import web
from aiohttp_swagger3 import SwaggerDocs, SwaggerUiSettings, SwaggerInfo
from dataclasses import asdict

from database.connector import DataBaseClass, db_connector
from database.models import User
from parse.parse_log import parse_logs

app = web.Application()
routes = web.RouteTableDef()

log = logging.getLogger(__name__)

DataBase = DataBaseClass()


@routes.post("/log/")
async def create_log(request: web.Request, *args, **kwargs) -> web.Response:
    """
    Create log
    """

    data = await request.json()
    print(data)
    # user = User(**data)
    # print(User(**data))
    if await parse_logs(data):
        return web.json_response(data={"answer": "ok"}, status=201)
    return web.json_response(data={"answer": "not save"}, status=400)


@routes.get("/logs/")
async def get_logs(request: web.Request, ) -> web.Response:
    """All logs list"""
    data_from_db = [{"id": 101, "name": "Lessie"}, {"id": 101, "name": "Lessie"}]
    # result = await DataBase.execute("SELECT username, balance FROM users WHERE chat_id = $1",
    #                                 message.from_user.id, fetchval=True)
    # print('Ваш баланс:', result[0]['balance'])
    # print('Ваш ник:', result[0]['username'])
    return web.json_response([asdict(User(**i)) for i in data_from_db])


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
