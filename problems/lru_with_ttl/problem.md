# lru_with_ttl

**Extend the existing `LRUCache` class** (in `current_implementation.py`)
to support **per-entry TTL expiry**.

The starting code is a working LRU cache with `__init__(capacity)`,
`get(key)`, `put(key, value)`, and `size()`. Your job is to add
time-based expiry without breaking the existing API.

## API additions

- `put(key, value, ttl_seconds=None)` — `ttl_seconds` is now an
  optional third argument. When `None` (the default), behaves exactly
  like the original `put(key, value)`. When given a positive number,
  the entry expires that many seconds after insertion (or update).
- `get(key)` — if the key has expired, return `-1` (same as missing)
  AND remove the expired entry from the cache.
- `size()` — should NOT count expired entries that haven't been
  cleaned up yet. (Lazy cleanup is fine; eager cleanup is also fine.)

## existing API contract (must keep working)

- `LRUCache(capacity)` — ValueError if capacity <= 0
- `LRUCache.get(key)` — `-1` if missing
- `LRUCache.put(key, value)` — LRU eviction at capacity
- `LRUCache.size()` — current entry count

Time is measured via `time.monotonic()`. The verifier uses
`time.monotonic` for sleeps and can rely on real wall-clock progression
for the TTL check.

## verifier

`tests/test_lru_with_ttl.py` includes **both** the prior LRU tests and
the new TTL tests. Save your work as `problems/lru_with_ttl/solution.py`.

## difficulty

iter70 · extend-mode · data-structure extension test — the box must
read the existing OOP code and add time-based behavior without
breaking the original contract
