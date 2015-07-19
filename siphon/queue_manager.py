from siphon.queue import Queue
from siphon.redis_connection import create_connection


class QueueManager(object):

    queues = {}

    def __init__(self, connection=None):
        self.connection = connection or create_connection()

    def create_queue(self, queue_name):
        self.queues[queue_name] = Queue(queue_name, self.connection)

        return self.queues[queue_name]

    def enqueue(self, queue_name, key, data):
        queue = self.queues[queue_name]
        queue.enqueue(key, data)

        return True

    def dequeue(self, queue_name):
        queue = self.queues[queue_name]

        return queue.dequeue()
