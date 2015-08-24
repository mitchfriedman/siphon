from unittest.mock import patch
from flask import json
from tests.resources.api_test_case import ApiTestCase


class TestDequeue(ApiTestCase):

    @patch('siphon.queue_manager.dequeue')
    def test_dequeue(self, dequeue):
        dequeue.return_value = {
            'item': {
                'key': 'abc',
                'creator': 'mitch',
                'type': 'email'
            }
        }

        response = self.post('/api/Queues/foobar/Dequeue')

        dequeue.assert_called_with('foobar')

        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'item': {
                'key': 'abc',
                'creator': 'mitch',
                'type': 'email'
            }
        }, json.loads(response.data))

    def test_dequeue_no_queue_name(self):
        response = self.post('/api/Queues/Dequeue')

        self.assertEqual(404, response.status_code)

    @patch('siphon.queue_manager.dequeue')
    def test_dequeue_unexistant_queue(self, dequeue):
        dequeue.return_value = None
        response = self.post('/api/Queues/foobar/Dequeue')

        self.assertEqual(400, response.status_code)

    @patch('siphon.queue_manager.dequeue')
    def test_dequeue_empty_queue(self, dequeue):
        dequeue.return_value = {}
        response = self.post('/api/Queues/foobar/Dequeue')

        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'message': 'Queue is empty'
        }, json.loads(response.data))
