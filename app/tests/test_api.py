import json

from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web

from main import get_logs, create_log


class TestAPI(AioHTTPTestCase):

    async def get_application(self):
        """Get app with added routes"""
        app = web.Application()
        app.router.add_get('/logs/', get_logs)
        app.router.add_post('/log/', create_log)
        return app

    async def test_log_create(self):
        """Testing create log"""
        test_data = {"id": 101, "name": "Lessie"}
        async with self.client.request("POST", "/log/", data=json.dumps(test_data, indent=2).encode('utf-8')) as resp:
            self.assertEqual(resp.status, 201)
            data = await resp.json()

        self.assertEqual(test_data, data)

    async def test_get_list(self):
        """Testing get log list"""
        async with self.client.request("GET", "/logs/") as resp:
            self.assertEqual(resp.status, 200)
            data = await resp.json()
        test_data = [{"id": 101, "name": "Lessie"}, {"id": 101, "name": "Lessie"}]
        print(type(test_data), type(data))
        self.assertEqual(test_data, data)
