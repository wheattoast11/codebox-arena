"""pytest verifier for problems/is_palindrome."""
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


def test_empty():
    assert _load_solution().is_palindrome("") is True


def test_single():
    assert _load_solution().is_palindrome("a") is True


def test_simple_yes():
    assert _load_solution().is_palindrome("racecar") is True


def test_simple_no():
    assert _load_solution().is_palindrome("hello") is False


def test_mixed_case():
    assert _load_solution().is_palindrome("RaceCar") is True


def test_with_spaces():
    assert _load_solution().is_palindrome("nurses run") is True
