"""pytest verifier for problems/add.

Imports the solution from `solution.py` (the box's submission). If only
`solution_stub.py` exists, the test fails — that's the expected pre-box
state and signals to the box that there's work to do.
"""
import importlib
import importlib.util
import pathlib
import pytest


def _load_solution():
    here = pathlib.Path(__file__).resolve().parent.parent
    sol = here / "solution.py"
    if not sol.exists():
        pytest.fail(f"solution.py not present at {sol} · box has not attempted this yet")
    spec = importlib.util.spec_from_file_location("solution", sol)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_add_basic():
    sol = _load_solution()
    assert sol.add(2, 3) == 5


def test_add_negative():
    sol = _load_solution()
    assert sol.add(-1, 1) == 0


def test_add_zero():
    sol = _load_solution()
    assert sol.add(0, 0) == 0


def test_add_large():
    sol = _load_solution()
    assert sol.add(10**9, 10**9) == 2 * 10**9
