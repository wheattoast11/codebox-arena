"""pytest verifier for problems/fib."""
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


def test_fib_0():
    assert _load_solution().fib(0) == 0


def test_fib_1():
    assert _load_solution().fib(1) == 1


def test_fib_10():
    assert _load_solution().fib(10) == 55


def test_fib_20():
    assert _load_solution().fib(20) == 6765
