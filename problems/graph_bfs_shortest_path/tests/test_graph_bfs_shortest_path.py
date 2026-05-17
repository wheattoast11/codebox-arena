"""pytest verifier for problems/graph_bfs_shortest_path."""
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


def test_trivial_start_equals_end():
    assert _load_solution().shortest_path({"A": []}, "A", "A") == 0


def test_two_hop():
    g = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert _load_solution().shortest_path(g, "A", "C") == 2


def test_longer_chain():
    g = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C", "E"], "E": ["D"]}
    assert _load_solution().shortest_path(g, "A", "E") == 4


def test_disconnected_returns_neg1():
    g = {"A": ["B"], "B": ["A"], "C": []}
    assert _load_solution().shortest_path(g, "A", "C") == -1


def test_self_loop_does_not_break():
    g = {"A": ["A", "B"], "B": ["A", "B"]}
    assert _load_solution().shortest_path(g, "A", "B") == 1


def test_parallel_edges():
    g = {"A": ["B", "B", "B"], "B": ["A", "A"]}
    assert _load_solution().shortest_path(g, "A", "B") == 1


def test_takes_shortest_when_multiple_paths():
    # A-B-D is length 2; A-B-C-D would be length 3. BFS picks length 2.
    g = {"A": ["B"], "B": ["A", "C", "D"], "C": ["B", "D"], "D": ["B", "C"]}
    assert _load_solution().shortest_path(g, "A", "D") == 2


def test_missing_start_raises():
    with pytest.raises(KeyError):
        _load_solution().shortest_path({"A": []}, "Z", "A")


def test_missing_end_raises():
    with pytest.raises(KeyError):
        _load_solution().shortest_path({"A": []}, "A", "Z")
