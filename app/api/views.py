from aiohttp import web

routes = web.RouteTableDef()


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
