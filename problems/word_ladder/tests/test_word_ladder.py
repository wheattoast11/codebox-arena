"""pytest verifier for problems/word_ladder."""
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


def test_classic_hit_to_cog():
    result = _load_solution().word_ladder(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    )
    assert result == 5


def test_missing_end_returns_zero():
    result = _load_solution().word_ladder(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    )
    assert result == 0


def test_trivial_single_step():
    # a → c is one letter change; path is a, c (length 2)
    assert _load_solution().word_ladder("a", "c", ["a", "b", "c"]) == 2


def test_no_path_disconnected():
    # "abc" → "xyz" cannot be reached via one-letter changes through ["abd"]
    result = _load_solution().word_ladder("abc", "xyz", ["abd"])
    assert result == 0


def test_same_word():
    # begin == end and end is in word_list — length 1 (just the word itself)
    # If your implementation treats this as needing zero steps, return 1
    # because the sequence has one word.
    result = _load_solution().word_ladder("dog", "dog", ["dog"])
    assert result == 1


def test_picks_shortest_when_multiple_paths():
    # cat → bat → bad → bed: length 4
    # cat → cot → cog → bog → bog... longer paths possible
    # The shortest is cat → bat → bad → bed = 4
    result = _load_solution().word_ladder(
        "cat", "bed", ["bat", "bad", "bed", "cot", "cog", "bog"]
    )
    assert result == 4


def test_end_directly_reachable():
    # one letter different, end in word_list
    result = _load_solution().word_ladder("cat", "bat", ["bat", "cot"])
    assert result == 2
