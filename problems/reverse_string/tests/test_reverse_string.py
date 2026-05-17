"""pytest verifier for problems/reverse_string."""
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
    assert _load_solution().reverse_string("") == ""


def test_ascii():
    assert _load_solution().reverse_string("hello") == "olleh"


def test_repeated():
    assert _load_solution().reverse_string("aaaa") == "aaaa"


def test_whitespace():
    assert _load_solution().reverse_string("a b c") == "c b a"


def test_unicode():
    assert _load_solution().reverse_string("héllo") == "olléh"
