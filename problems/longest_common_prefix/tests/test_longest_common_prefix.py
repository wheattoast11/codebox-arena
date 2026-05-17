"""pytest verifier for problems/longest_common_prefix."""
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


def test_empty_list():
    assert _load_solution().longest_common_prefix([]) == ""


def test_single_string():
    assert _load_solution().longest_common_prefix(["hello"]) == "hello"


def test_classic_flower():
    assert _load_solution().longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_no_common_prefix():
    assert _load_solution().longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_long_shared():
    assert _load_solution().longest_common_prefix(
        ["interspecies", "interstellar", "interstate"]
    ) == "inters"


def test_empty_string_in_list():
    assert _load_solution().longest_common_prefix(["abc", "", "abd"]) == ""


def test_identical_strings():
    assert _load_solution().longest_common_prefix(["same", "same", "same"]) == "same"


def test_one_is_prefix_of_others():
    assert _load_solution().longest_common_prefix(["abc", "abcdef", "abcd"]) == "abc"
