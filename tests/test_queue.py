import unittest
from siphon.queue import Queue
from redis import StrictRedis


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.test_connection = StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def tearDown(self):
        self.test_connection.flushall()

    def test_create_queue_no_connection(self):
        queue = Queue('foo')

        self.assertEqual('queue:foo', queue.name)
        self.assertEqual(None, queue.database)

    def test_create_queue_with_connection(self):
        queue = Queue('foo', connection=self.test_connection)

        self.assertEqual('queue:foo', queue.name)
        self.assertEqual(self.test_connection, queue.database)

    def test_add_to_queue(self):
        queue = Queue('foo', connection=self.test_connection)

        queue.add_to_queue('ahs71bsa')
        self.assertEqual('ahs71bsa', queue._peek_last_element())

    def test_remove_from_queue(self):
        queue = Queue('foo', connection=self.test_connection)

        queue.add_to_queue('ahs71bsa')
        queue.add_to_queue('abcdefg')

        popped = queue.pop()

        self.assertEqual('ahs71bsa', popped)
        self.assertEqual('abcdefg', queue._peek_last_element())

    def test_remove_from_empty_queue(self):
        queue = Queue('foo', connection=self.test_connection)

        popped = queue.pop()
        self.assertEqual(None, popped)

    def test_set_data_hash(self):
        queue = Queue('foo', connection=self.test_connection)

        queue.set_hash_data('ahs71bsa', {
            'id': 'ahs71bsa',
            'creator': 'Mitch',
            'type': 'email'
        })

        self.assertEqual({
            'id': 'ahs71bsa',
            'creator': 'Mitch',
            'type': 'email'
        }, queue._get_hash_data('ahs71bsa'))

    def test_delete_hash_data(self):
        queue = Queue('foo', connection=self.test_connection)

        queue.set_hash_data('ahs71bsa', {
            'id': 'ahs71bsa',
            'creator': 'Mitch',
            'type': 'email'
        })

        queue._delete_hash_data('ahs71bsa')
        self.assertEqual(None, queue._get_hash_data('ah71bsa'))

    def test_connection(self):
        self.assertIsNotNone(self.test_connection)
