from tests import BaseRedisTest


class TestQueue(BaseRedisTest):

    def test_connection(self):
        self.assertIsNotNone(self.test_connection)

    def test_add_garbage(self):
        self.test_connection.set('foo', 'bar')

    def test_flush_after_test(self):
        self.assertEqual(None, self.test_connection.get('foo'))
