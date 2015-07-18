from redis import StrictRedis


def create_connection(host='localhost', port=6379, db=0, **kwargs):
    return StrictRedis(host=host, port=port, db=db, decode_responses=True, **kwargs)
