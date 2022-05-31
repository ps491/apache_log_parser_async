import json
from datetime import datetime, timezone, timedelta

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
        test_data = {"log": '35.237.4.214 - - [19/Dec/2020:15:22:40 +0100] "GET /administrator/%22 HTTP/1.1" 404 226 "-" ' \
                    '"Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)" "-" '}
        result = {'ip': '35.237.4.214',
                  'indent': '-',
                  'user': '-',
                  'time': datetime(2020, 12, 19, 15, 22, 40, tzinfo=timezone(timedelta(seconds=3600))),
                  'method': 'GET',
                  'url': '/administrator/%22',
                  'protocol': 'HTTP/1.1',
                  'status': '404',
                  'size': '226',
                  'referrer': '-',
                  'agent': 'Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)',
                  'other': '-'}
        async with self.client.request("POST", "/log/", data=json.dumps(test_data, indent=2).encode('utf-8')) as resp:
            self.assertEqual(resp.status, 201)
            data = await resp.json()

        self.assertEqual(data, result)

    async def test_get_list(self):
        """Testing get log list"""
        async with self.client.request("GET", "/logs/") as resp:
            self.assertEqual(resp.status, 200)
            data = await resp.json()
        test_data = [{"id": 101, "name": "Lessie"}, {"id": 101, "name": "Lessie"}]
        print(type(test_data), type(data))
        self.assertEqual(test_data, data)
