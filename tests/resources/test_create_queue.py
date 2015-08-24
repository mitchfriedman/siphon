from flask import json
from tests.resources.api_test_case import ApiTestCase


class TestCreateQueue(ApiTestCase):

    def test_create_queue(self):
        response = self.post('/api/Queues', data={
            'queue_name': 'foobar'
        })

        self.assertEqual(201, response.status_code)
        self.assertEqual({
            'name': 'foobar'
        }, json.loads(response.data))

    def test_create_no_queue_name(self):
        response = self.post('/api/Queues')

        self.assertEqual(400, response.status_code)
