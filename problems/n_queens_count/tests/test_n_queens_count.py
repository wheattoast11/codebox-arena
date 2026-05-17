"""pytest verifier for problems/n_queens_count."""
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


def test_n_one():
    assert _load_solution().n_queens_count(1) == 1


def test_n_two_no_solution():
    assert _load_solution().n_queens_count(2) == 0


def test_n_three_no_solution():
    assert _load_solution().n_queens_count(3) == 0


def test_n_four():
    assert _load_solution().n_queens_count(4) == 2


def test_n_five():
    assert _load_solution().n_queens_count(5) == 10


def test_n_six():
    assert _load_solution().n_queens_count(6) == 4


def test_n_seven():
    assert _load_solution().n_queens_count(7) == 40


def test_n_eight():
    assert _load_solution().n_queens_count(8) == 92


def test_n_zero_raises():
    with pytest.raises(ValueError):
        _load_solution().n_queens_count(0)


def test_n_negative_raises():
    with pytest.raises(ValueError):
        _load_solution().n_queens_count(-1)
