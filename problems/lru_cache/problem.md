# lru_cache

Implement an `LRUCache` class with a fixed capacity. Both `get(key)`
and `put(key, value)` must run in **O(1) average time**. When the cache
is full and a new key is inserted, evict the least-recently-used entry.

Accessing or updating a key (via `get` or `put` of an existing key)
counts as a use and moves it to most-recently-used.

API contract:
- `LRUCache(capacity)` — `capacity` is a positive integer; raise
  `ValueError` if `capacity <= 0`
- `cache.get(key)` — returns the stored value, or `-1` if the key is
  not present
- `cache.put(key, value)` — insert or update the key; evicts LRU if at
  capacity and the key is new
- `cache.size()` — returns the current number of entries

For example:
```python
c = LRUCache(2)
c.put(1, "a")
c.put(2, "b")
c.get(1)         # → "a"  (now 1 is MRU, 2 is LRU)
c.put(3, "c")    # evicts 2
c.get(2)         # → -1
c.get(3)         # → "c"
```

## verifier

`tests/test_lru_cache.py` — must pass under `pytest`. Tests cover the
ValueError, basic put+get, eviction order, access-promotes-to-MRU,
update-existing-key counts as use, capacity=1 edge case, and size.

## difficulty

hard · O(1) get and put requires the doubly-linked-list + hashmap pattern (or OrderedDict)
