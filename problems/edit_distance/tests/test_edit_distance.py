"""pytest verifier for problems/edit_distance."""
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


def test_both_empty():
    assert _load_solution().edit_distance("", "") == 0


def test_identical():
    assert _load_solution().edit_distance("abc", "abc") == 0


def test_empty_to_three():
    assert _load_solution().edit_distance("", "abc") == 3


def test_three_to_empty():
    assert _load_solution().edit_distance("abc", "") == 3


def test_kitten_to_sitting():
    assert _load_solution().edit_distance("kitten", "sitting") == 3


def test_single_substitution():
    assert _load_solution().edit_distance("cat", "bat") == 1


def test_single_insertion():
    assert _load_solution().edit_distance("cat", "cart") == 1


def test_single_deletion():
    assert _load_solution().edit_distance("cart", "cat") == 1


def test_case_sensitive():
    assert _load_solution().edit_distance("ABC", "abc") == 3


def test_unrelated():
    assert _load_solution().edit_distance("horse", "ros") == 3
