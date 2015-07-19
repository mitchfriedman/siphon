from unittest.mock import patch
from flask import json
from tests.resources.api_test_case import ApiTestCase


class TestApi(ApiTestCase):

    def setUp(self):
        super().setUp()

    @patch('siphon.queue_manager.enqueue')
    def test_enqueue(self, enqueue):
        response = self.post("/api/enqueue/foo", data={
            'key': 'foo123',
            'creator': 'mitch',
            'type': 'email'
        })

        enqueue.assert_called_with('foo', 'foo123', {
            'creator': 'mitch',
            'type': 'email'
        })

        self.assertEqual(201, response.status_code)
        self.assertEqual({
            'status': 'enqueued'
        }, json.loads(response.data))

    def test_enqueue_missing_queue_name(self):
        response = self.post('/api/enqueue', data={
            'id': 'foo123',
            'creator': 'mitch',
            'type': 'email'
        })

        self.assertEqual(404, response.status_code)

    def test_enqueue_missing_key(self):
        response = self.post('/api/enqueue/foo', data={
            'id': 'foo123',
            'creator': 'mitch',
            'type': 'email'
        })

        self.assertEqual(400, response.status_code)

    def test_enqueue_non_existant_queue(self):
        response = self.post('/api/enqueue/foo', data={
            'key': 'foo123'
        })

        self.assertEqual(400, response.status_code)

        resp = json.loads(response.data)
        self.assertEqual('A queue with that given name does not exist', resp['message'])
