"""pytest verifier for problems/balanced_brackets."""
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
    assert _load_solution().balanced_brackets("") is True


def test_simple_balanced():
    assert _load_solution().balanced_brackets("()") is True


def test_simple_unbalanced_unclosed():
    assert _load_solution().balanced_brackets("(") is False


def test_simple_unbalanced_wrong_close():
    assert _load_solution().balanced_brackets(")") is False


def test_mixed_types():
    assert _load_solution().balanced_brackets("(){}[]") is True


def test_nested_types():
    assert _load_solution().balanced_brackets("([{}])") is True


def test_interleaved_wrong():
    assert _load_solution().balanced_brackets("([)]") is False


def test_ignore_non_bracket():
    assert _load_solution().balanced_brackets("a(b[c]d)e") is True


def test_unmatched_after_correct():
    assert _load_solution().balanced_brackets("()(") is False
