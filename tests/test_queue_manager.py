from siphon.queue_manager import QueueManager
from tests import BaseRedisTest


class TestQueueManager(BaseRedisTest):

    def setUp(self):
        super().setUp()
        self.queue_manager = QueueManager(self.test_connection)

    def test_create_queue(self):
        self.queue_manager.create_queue('foo')

        self.assertIsNotNone(self.queue_manager.queues['foo'])

    def test_enqueue(self):
        self.queue_manager.create_queue('foo')

        rv = self.queue_manager.enqueue('foo', 'abcdef', {
            'id': 'abcdef',
            'creator': 'mitch',
            'type': 'email'
        })

        self.assertEqual(True, rv)

    def test_dequeue(self):
        self.queue_manager.create_queue('foo')

        self.queue_manager.enqueue('foo', 'abcdef', {
            'id': 'abcdef',
            'creator': 'mitch',
            'type': 'email'
        })

        data = self.queue_manager.dequeue('foo')

        self.assertEqual({
            'id': 'abcdef',
            'creator': 'mitch',
            'type': 'email'
        }, data)
