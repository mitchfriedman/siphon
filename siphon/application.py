from collections import namedtuple
from clint.textui import colored

Style = namedtuple('Style', ['success', 'fail',])

colors = Style(success=colored.green,
               fail=colored.red)

def run():
    print("Running.............", colors.success('ok'))


class QueueManager(object):

    queues = {}

    def __init__(self):
        pass

    def enqueue(self, queue_name, key, data):
        pass

    def dequeue(self, queue_name):
        pass

