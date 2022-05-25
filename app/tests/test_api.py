from unittest import TestCase


class TestAPI(TestCase):
    def setUp(self):
        self.url = "http://localhost:8080"
        self.created_id = None
        self.new_log = {
            'ip': "0.0.0.0",
            'protocol': "Yartsev",
            'time': "1989-04-09",
            'url': "2021-11-01"
        }

    def test_create(self):
        """Testing create log"""
        pass

    def test_retrieve(self):
        """Testing object retrieving by id"""
        pass

    def test_list(self):
        """Testing get log list"""

    def test_delete(self):
        """Testing delete log"""
