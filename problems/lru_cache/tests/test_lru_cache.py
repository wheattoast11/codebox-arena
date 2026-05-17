"""pytest verifier for problems/lru_cache."""
import importlib.util
import pathlib
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


def test_zero_capacity_raises():
    LRUCache = _load_solution().LRUCache
    with pytest.raises(ValueError):
        LRUCache(0)


def test_negative_capacity_raises():
    LRUCache = _load_solution().LRUCache
    with pytest.raises(ValueError):
        LRUCache(-1)


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


def test_basic_eviction_order():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    c.put(3, "c")           # evicts key 1 (LRU)
    assert c.get(1) == -1
    assert c.get(2) == "b"
    assert c.get(3) == "c"


def test_get_promotes_to_mru():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    c.get(1)                # 1 becomes MRU; 2 is now LRU
    c.put(3, "c")           # evicts 2, not 1
    assert c.get(1) == "a"
    assert c.get(2) == -1
    assert c.get(3) == "c"


def test_put_existing_key_updates_and_promotes():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(2)
    c.put(1, "a")
    c.put(2, "b")
    c.put(1, "A")           # updates value, promotes to MRU
    c.put(3, "c")           # evicts 2 (LRU), not 1
    assert c.get(1) == "A"
    assert c.get(2) == -1
    assert c.get(3) == "c"


def test_capacity_one():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(1)
    c.put(1, "a")
    c.put(2, "b")
    assert c.get(1) == -1
    assert c.get(2) == "b"


def test_size_tracks_entries():
    LRUCache = _load_solution().LRUCache
    c = LRUCache(3)
    assert c.size() == 0
    c.put(1, "a")
    assert c.size() == 1
    c.put(2, "b")
    assert c.size() == 2
    c.put(1, "A")           # update, not new
    assert c.size() == 2
    c.put(3, "c")
    c.put(4, "d")           # evicts LRU; size stays at capacity
    assert c.size() == 3
