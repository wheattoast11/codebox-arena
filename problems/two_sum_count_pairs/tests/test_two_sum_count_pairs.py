"""pytest verifier for problems/two_sum_count_pairs."""
import importlib.util
import pathlib
import random
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
    assert _load_solution().count_pairs_with_sum([], 0) == 0


def test_single_no_pair():
    assert _load_solution().count_pairs_with_sum([5], 5) == 0


def test_basic_pairs():
    assert _load_solution().count_pairs_with_sum([1, 2, 3, 4], 5) == 2


def test_duplicates_combinatorial():
    # Three 1's, target 2 → C(3, 2) = 3 pairs
    assert _load_solution().count_pairs_with_sum([1, 1, 1], 2) == 3


def test_all_zeros():
    # Four 0's, target 0 → C(4, 2) = 6
    assert _load_solution().count_pairs_with_sum([0, 0, 0, 0], 0) == 6


def test_negatives():
    # (-1,1) and (2,-2) sum to 0
    assert _load_solution().count_pairs_with_sum([-1, 1, 2, -2, 3], 0) == 2


def test_no_match():
    assert _load_solution().count_pairs_with_sum([1, 2, 3], 10) == 0


def test_self_pair_not_counted():
    # arr = [3, 3], target = 6: one pair (i=0, j=1)
    assert _load_solution().count_pairs_with_sum([3, 3], 6) == 1


@pytest.mark.timeout(2)
def test_performance_gated_n100k():
    # Naive O(n^2) = 10^10 ops, way over 2s.
    # Efficient running-hashmap = O(n) = 10^5 ops, milliseconds.
    random.seed(11)
    n = 100_000
    arr = [random.randint(-50, 50) for _ in range(n)]
    target = 7

    # Ground truth via efficient running-hashmap
    from collections import defaultdict
    counts = defaultdict(int)
    expected = 0
    for x in arr:
        expected += counts[target - x]
        counts[x] += 1

    assert _load_solution().count_pairs_with_sum(arr, target) == expected
