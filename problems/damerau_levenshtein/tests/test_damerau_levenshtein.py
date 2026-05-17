"""pytest verifier for problems/damerau_levenshtein."""
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


# ─── existing Levenshtein contract (must still pass) ──────────────────────

def test_edit_distance_both_empty():
    assert _load_solution().edit_distance("", "") == 0


def test_edit_distance_identical():
    assert _load_solution().edit_distance("abc", "abc") == 0


def test_edit_distance_kitten_sitting():
    assert _load_solution().edit_distance("kitten", "sitting") == 3


def test_edit_distance_swap_is_two():
    # Plain Levenshtein treats "ab"→"ba" as 2 substitutions
    assert _load_solution().edit_distance("ab", "ba") == 2


# ─── new Damerau-Levenshtein contract ─────────────────────────────────────

def test_damerau_both_empty():
    assert _load_solution().damerau_distance("", "") == 0


def test_damerau_identical():
    assert _load_solution().damerau_distance("abc", "abc") == 0


def test_damerau_simple_swap_is_one():
    """The whole point: 'ab'→'ba' is 1 transposition, not 2 subs."""
    assert _load_solution().damerau_distance("ab", "ba") == 1


def test_damerau_swap_in_middle():
    """'abc'→'acb' is one transposition at the end."""
    assert _load_solution().damerau_distance("abc", "acb") == 1


def test_damerau_same_as_levenshtein_when_no_swap():
    # kitten → sitting has no adjacent-pair swaps; same answer as Levenshtein.
    assert _load_solution().damerau_distance("kitten", "sitting") == 3


def test_damerau_insertion_only():
    assert _load_solution().damerau_distance("abc", "abcd") == 1


def test_damerau_deletion_only():
    assert _load_solution().damerau_distance("abcd", "abc") == 1


def test_damerau_optimal_alignment_ca_abc():
    """ca → abc via OSA: insert 'b' (cab), transpose 'ca'→'ac' = 2 edits."""
    assert _load_solution().damerau_distance("ca", "abc") == 2
