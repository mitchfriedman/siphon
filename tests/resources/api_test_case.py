from unittest import TestCase
from siphon.resources.application import create_app


class ApiTestCase(TestCase):

    app = create_app()

    def setUp(self):
        super().setUp()
        self.app = self.app.test_client()

    def request(self, method, url, **kwargs):
        return self.app.open(url, method=method, **kwargs)

    def get(self, *args, **kwargs):
        return self.request("GET", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request("POST", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.request("PUT", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.request("DELETE", *args, **kwargs)
