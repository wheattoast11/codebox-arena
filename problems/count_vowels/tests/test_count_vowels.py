"""pytest verifier for problems/count_vowels."""
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
    assert _load_solution().count_vowels("") == 0


def test_simple():
    assert _load_solution().count_vowels("hello") == 2


def test_mixed_case():
    assert _load_solution().count_vowels("HELLO") == 2


def test_all_vowels():
    assert _load_solution().count_vowels("aeiouAEIOU") == 10


def test_no_vowels():
    assert _load_solution().count_vowels("rhythm") == 0
