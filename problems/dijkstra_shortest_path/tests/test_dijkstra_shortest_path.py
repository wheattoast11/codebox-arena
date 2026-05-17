"""pytest verifier for problems/dijkstra_shortest_path."""
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


# ─── existing BFS contract (must still pass) ──────────────────────────────

def test_bfs_trivial_start_equals_end():
    assert _load_solution().shortest_path({"A": []}, "A", "A") == 0


def test_bfs_two_hop():
    g = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert _load_solution().shortest_path(g, "A", "C") == 2


def test_bfs_disconnected_returns_neg1():
    g = {"A": ["B"], "B": ["A"], "C": []}
    assert _load_solution().shortest_path(g, "A", "C") == -1


def test_bfs_missing_start_raises():
    with pytest.raises(KeyError):
        _load_solution().shortest_path({"A": []}, "Z", "A")


# ─── new Dijkstra contract ────────────────────────────────────────────────

def test_dijkstra_trivial():
    assert _load_solution().dijkstra({"A": {}}, "A", "A") == 0


def test_dijkstra_single_edge():
    g = {"A": {"B": 5}, "B": {"A": 5}}
    assert _load_solution().dijkstra(g, "A", "B") == 5


def test_dijkstra_picks_shorter_weighted_path():
    # A→B direct is 5; A→C→B is 2+1 = 3. Dijkstra picks 3.
    g = {"A": {"B": 5, "C": 2},
         "B": {"A": 5, "C": 1},
         "C": {"A": 2, "B": 1}}
    assert _load_solution().dijkstra(g, "A", "B") == 3


def test_dijkstra_longer_chain():
    g = {"A": {"B": 1}, "B": {"A": 1, "C": 2}, "C": {"B": 2, "D": 3}, "D": {"C": 3}}
    assert _load_solution().dijkstra(g, "A", "D") == 6


def test_dijkstra_disconnected():
    g = {"A": {"B": 1}, "B": {"A": 1}, "C": {}}
    assert _load_solution().dijkstra(g, "A", "C") == -1


def test_dijkstra_missing_start():
    with pytest.raises(KeyError):
        _load_solution().dijkstra({"A": {}}, "Z", "A")


def test_dijkstra_missing_end():
    with pytest.raises(KeyError):
        _load_solution().dijkstra({"A": {}}, "A", "Z")


def test_dijkstra_avoids_high_weight_edge():
    # A→B is weight 100; A→C→B is weight 1+1=2. Dijkstra picks 2.
    g = {"A": {"B": 100, "C": 1},
         "B": {"A": 100, "C": 1},
         "C": {"A": 1, "B": 1}}
    assert _load_solution().dijkstra(g, "A", "B") == 2


def test_dijkstra_zero_weight_edge():
    g = {"A": {"B": 0}, "B": {"A": 0, "C": 5}, "C": {"B": 5}}
    assert _load_solution().dijkstra(g, "A", "C") == 5
