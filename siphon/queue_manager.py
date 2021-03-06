from siphon.queue import Queue
from siphon.redis_connection import create_connection
from flask import abort


class QueueManager(object):

    queues = {}

    def __init__(self, connection=None):
        self.connection = connection or create_connection()

    def create_queue(self, queue_name):
        self.queues[queue_name] = Queue(queue_name, self.connection)

        return self.queues[queue_name]

    def enqueue(self, queue_name, key, data):
        queue = self._get_queue(queue_name)

        if queue is None:
            abort(404)

        return queue.enqueue(key, data)

    def dequeue(self, queue_name):
        queue = self._get_queue(queue_name)

        return queue.dequeue() if queue else None

    def _get_queue(self, queue_name):
        return self.queues.get(queue_name, None)

