"""pytest verifier for problems/wildcard_regex_match."""
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
    assert _load_solution().wildcard_match("", "") is True


def test_empty_string_any_star():
    assert _load_solution().wildcard_match("", "*") is True


def test_empty_string_with_literal():
    assert _load_solution().wildcard_match("", "a") is False


def test_literal_match():
    assert _load_solution().wildcard_match("abc", "abc") is True


def test_literal_mismatch_length():
    assert _load_solution().wildcard_match("abc", "abcd") is False


def test_question_mark_single():
    assert _load_solution().wildcard_match("abc", "a?c") is True


def test_question_mark_no_match():
    assert _load_solution().wildcard_match("abc", "a?d") is False


def test_star_in_middle():
    assert _load_solution().wildcard_match("abcde", "a*e") is True


def test_star_at_end():
    assert _load_solution().wildcard_match("abcdef", "abc*") is True


def test_star_at_start():
    assert _load_solution().wildcard_match("abcdef", "*def") is True


def test_only_star():
    assert _load_solution().wildcard_match("anything", "*") is True


def test_multiple_stars():
    assert _load_solution().wildcard_match("abcdef", "a*c*f") is True


def test_adjacent_stars():
    assert _load_solution().wildcard_match("abc", "a**c") is True


def test_star_eats_zero_chars():
    assert _load_solution().wildcard_match("ac", "a*c") is True


def test_complex_mixed():
    assert _load_solution().wildcard_match("hello world", "h*o w?rld") is True


def test_complex_no_match():
    assert _load_solution().wildcard_match("hello", "h?lloo") is False
