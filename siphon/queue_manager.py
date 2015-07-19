from siphon.queue import Queue
from siphon.redis_connection import create_connection
from werkzeug.exceptions import HTTPException


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
            raise HTTPException('QueueNotFound')

        queue.enqueue(key, data)

        return True

    def dequeue(self, queue_name):
        queue = self._get_queue(queue_name)

        if queue is None:
            raise HTTPException('QueueNotFound')

        return queue.dequeue()

    def _get_queue(self, queue_name):
        if queue_name in self.queues:
            return self.queues[queue_name]

        return None