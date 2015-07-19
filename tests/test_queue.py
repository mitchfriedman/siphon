from siphon.queue import Queue
from tests import BaseRedisTest
from nose.tools import raises


class TestQueue(BaseRedisTest):

    def setUp(self):
        super().setUp()

    def _create_queue(self, conn, name=None):
        name = name or 'foo'

        return Queue(name, connection=conn)

    @raises(Exception)
    def test_create_queue_no_connection(self):
        queue = self._create_queue(None)

        self.assertEqual('queue:foo', queue.name)
        self.assertEqual(None, queue.database)

    def test_create_queue_with_connection(self):
        queue = self._create_queue(self.test_connection)

        self.assertEqual('queue:foo', queue.name)
        self.assertEqual(self.test_connection, queue.database)

    def test_add_to_queue(self):
        queue = self._create_queue(self.test_connection)

        queue._push_to_queue('ahs71bsa')
        self.assertEqual('ahs71bsa', queue._peek_last_element())

    def test_remove_from_queue(self):
        queue = self._create_queue(self.test_connection)

        queue._push_to_queue('ahs71bsa')
        queue._push_to_queue('abcdefg')

        popped = queue._pop()

        self.assertEqual('ahs71bsa', popped)
        self.assertEqual('abcdefg', queue._peek_last_element())

    def test_remove_from_empty_queue(self):
        queue = self._create_queue(self.test_connection)

        popped = queue._pop()
        self.assertEqual(None, popped)

    def test_set_data_hash(self):
        queue = self._create_queue(self.test_connection)

        queue._set_hash_data('ahs71bsa', {
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
        queue = self._create_queue(self.test_connection)

        queue._set_hash_data('ahs71bsa', {
            'id': 'ahs71bsa',
            'creator': 'Mitch',
            'type': 'email'
        })

        queue._delete_hash_data('ahs71bsa')
        self.assertEqual(None, queue._get_hash_data('ah71bsa'))
