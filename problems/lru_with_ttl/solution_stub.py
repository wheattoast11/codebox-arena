class LRUCache:
    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value, ttl_seconds=None):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError
