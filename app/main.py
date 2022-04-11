import logging

from aiohttp import web
from aiohttp_swagger3 import SwaggerDocs, SwaggerUiSettings, SwaggerInfo

app = web.Application()
routes = web.RouteTableDef()

log = logging.getLogger(__name__)


@routes.get("/logs/")
async def get_logs(request: web.Request, pet_id: int) -> web.Response:
    """
    Optional route description
    ---
    summary: Info for a specific pet
    tags:
      - logs

    responses:
      '200':
        description: An array of logs
    """

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
