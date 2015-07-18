import unittest
from redis import StrictRedis
from siphon.redis_connection import create_connection


class BaseRedisTest(unittest.TestCase):
    def setUp(self):
        self.test_connection = create_connection()

    def tearDown(self):
        self.test_connection.flushall()
