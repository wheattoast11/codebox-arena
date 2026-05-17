import collections
import time

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.ttls = {}

    def _is_expired(self, key):
        if key not in self.ttls:
            return False
        return time.monotonic() > self.ttls[key]

    def _remove_expired(self, key):
        if key in self.cache:
            if self._is_expired(key):
                del self.cache[key]
                del self.ttls[key]
                return True
        return False

    def get(self, key):
        if key not in self.cache:
            return -1
        
        if self._is_expired(key):
            del self.cache[key]
            del self.ttls[key]
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value, ttl_seconds=None):
        if key in self.cache:
            # Update value and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
            if ttl_seconds is not None:
                self.ttls[key] = time.monotonic() + ttl_seconds
            else:
                # If TTL was previously set, remove it; otherwise keep no TTL
                if key in self.ttls:
                    del self.ttls[key]
        else:
            if len(self.cache) >= self.capacity:
                # Pop the first item (least recently used)
                # But we need to clean up the popped item's TTL if it exists
                old_key, _ = self.cache.popitem(last=False)
                if old_key in self.ttls:
                    del self.ttls[old_key]
            
            self.cache[key] = value
            if ttl_seconds is not None:
                self.ttls[key] = time.monotonic() + ttl_seconds
            # If ttl_seconds is None, we don't add to ttls, meaning no expiry

    def size(self):
        # Remove expired entries and count remaining
        expired_keys = [k for k in self.cache if self._is_expired(k)]
        for k in expired_keys:
            del self.cache[k]
            if k in self.ttls:
                del self.ttls[k]
        return len(self.cache)
