"""pytest verifier for problems/kadane_max_subarray."""
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


def test_classic_kadane():
    assert _load_solution().max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single_element():
    assert _load_solution().max_subarray([42]) == 42


def test_all_negative():
    # answer is the largest (closest to zero) single element
    assert _load_solution().max_subarray([-3, -1, -2, -7]) == -1


def test_all_positive():
    assert _load_solution().max_subarray([1, 2, 3, 4]) == 10


def test_single_negative():
    assert _load_solution().max_subarray([-5]) == -5


def test_empty_raises():
    with pytest.raises(ValueError):
        _load_solution().max_subarray([])
