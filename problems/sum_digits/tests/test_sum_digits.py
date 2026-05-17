"""pytest verifier for problems/sum_digits."""
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


def test_zero():
    assert _load_solution().sum_digits(0) == 0


def test_single_digit():
    assert _load_solution().sum_digits(7) == 7


def test_multi_digit():
    assert _load_solution().sum_digits(123) == 6


def test_with_internal_zero():
    assert _load_solution().sum_digits(1024) == 7


def test_negative_raises():
    with pytest.raises(ValueError):
        _load_solution().sum_digits(-5)
