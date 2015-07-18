
class Queue(object):
    """
    Basic queue backed by redis for storing arbitrary job data
    """

    def __init__(self, name, connection=None):
        self.database = connection or self._create_connection()
        self.name = '{}:{}'.format('queue', name)

    def _create_connection(self):
        return None

    def add_to_queue(self, key):
        """
        Enqueue an item with data by it's unique key
        :param key: A unique key to identify this item
        :param data: A dictionary of key values to set
        :return: No return

        ex:
        add_to_queue('ahs71bsa', {
            'id': 'ahs71bsa',
            'creator': 'Mitch',
            'type': 'email'
        })

        This will be added to the redis database in 2 ways:
            - Added to the end of a list (queue.name)
            - Each item in the data will be hashed and added to a hash
                located at the name of 'ahs71bsa'

        """

        self.database.rpush(self.name, key)

    def set_hash_data(self, key, data):
        for k, v in data.items():
            self.database.hset(key, k, v)

    def _get_hash_data(self, key):
        data = self.database.hgetall(key)
        if len(data.items()) == 0:
            return None

        return data

    def _delete_hash_data(self, key):
        self.database.delete(key)

    def pop(self):
        return self.database.lpop(self.name)

    def _peek_last_element(self):
        item = self.database.lrange(self.name, -1, -1)
        if item and len(item) > 0:
            return item[0]

        return item
