
class Queue(object):
    """
    Basic queue backed by redis for storing arbitrary job data
    """

    def __init__(self, name, connection=None):
        if connection is None:
            raise Exception('No connection given. Exiting')

        self.database = connection
        self.name = '{}:{}'.format('queue', name)

    def enqueue(self, key, data):
        self._push_to_queue(key)
        self._set_hash_data(key, data)

    def _pop(self):
        return self.database.lpop(self.name)

    def _push_to_queue(self, key):
        """
        Enqueue an item by a key (which is assumed to be unique)
        :param key: A unique key to identify this item
        :return: No return

        ex:
        add_to_queue('ahs71bsa')

        This will be added to the queue currently in use
        """

        self.database.rpush(self.name, key)

    def _set_hash_data(self, key, data):
        """
        Set the hash data for a given unique key and attributes on that key
        :param key: A unique key to identify this item
        :param data: A python dictionary of keys to values to set on the key
        :return: No return
        """
        for k, v in data.items():
            self.database.hset(key, k, v)

    def _get_hash_data(self, key):
        """
        Get a python dictionary of the hash data for a given key
        :param key: The unique identifier for the key you wish to fetch data for
        :return: A dictionary of the data, or None
        """
        data = self.database.hgetall(key)
        if len(data.items()) == 0:
            return None

        return data

    def _delete_hash_data(self, key):
        """
        Delete the data from the table for a given key
        :param key: A unique identifier you wish to delete data for
        :return: No return
        """
        self.database.delete(key)

    def _peek_last_element(self):
        item = self.database.lrange(self.name, -1, -1)
        if item and len(item) > 0:
            return item[0]

        return item
