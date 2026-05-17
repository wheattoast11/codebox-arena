"""pytest verifier for problems/lru_with_ttl."""
import importlib.util
import pathlib
import time
import pytest


def _load_solution():
    here = pathlib.Path(__file__).resolve().parent.parent
    sol = here / "solution.py"
    if not sol.exists():
        pytest.skip(f"solution.py not present at {sol} · box has not attempted this problem yet")
    spec = importlib.util.spec_from_file_location("solution", sol)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ─── existing LRU contract (must still pass) ──────────────────────────────

def test_zero_capacity_raises():
    LRUCache = _load_solution().LRUCache
    with pytest.raises(ValueError):
        LRUCache(0)


def test_basic_put_get():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    assert c.get(1) == "a"
    assert c.get(2) == "b"


def test_get_missing_returns_neg1():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    assert c.get(99) == -1


def test_eviction_order_unchanged():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    c.put(3, "c")           # evicts 1
    assert c.get(1) == -1
    assert c.get(2) == "b"


def test_get_promotes_to_mru():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    c.get(1)
    c.put(3, "c")           # evicts 2, not 1
    assert c.get(1) == "a"
    assert c.get(2) == -1


# ─── new TTL contract ─────────────────────────────────────────────────────

def test_put_without_ttl_never_expires():
    """ttl_seconds=None (default) means no expiry — original behavior."""
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    time.sleep(0.2)
    assert c.get(1) == "a"


def test_put_with_ttl_expires():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a", ttl_seconds=0.1)
    assert c.get(1) == "a"      # not yet expired
    time.sleep(0.2)
    assert c.get(1) == -1       # expired → missing


def test_put_with_ttl_then_update_resets():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a", ttl_seconds=0.2)
    time.sleep(0.15)
    c.put(1, "b", ttl_seconds=0.3)   # update before expiry; resets timer
    time.sleep(0.15)
    assert c.get(1) == "b"      # would have expired under first TTL, not new one


def test_expired_entry_returns_neg1_and_size_drops():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(3)
    c.put(1, "a", ttl_seconds=0.1)
    c.put(2, "b")  # no TTL
    assert c.size() == 2
    time.sleep(0.2)
    # touch the expired key — should now be missing
    assert c.get(1) == -1
    # size should not count expired entries that have been observed missing
    assert c.size() == 1


def test_mixed_ttl_and_no_ttl_in_same_cache():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(3)
    c.put(1, "a")
    c.put(2, "b", ttl_seconds=0.1)
    c.put(3, "c")
    time.sleep(0.2)
    assert c.get(1) == "a"
    assert c.get(2) == -1
    assert c.get(3) == "c"
