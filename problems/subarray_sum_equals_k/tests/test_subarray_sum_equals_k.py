"""pytest verifier for problems/subarray_sum_equals_k."""
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
    assert _load_solution().count_subarrays_with_sum([], 0) == 0


def test_single_match():
    assert _load_solution().count_subarrays_with_sum([5], 5) == 1


def test_single_no_match():
    assert _load_solution().count_subarrays_with_sum([5], 3) == 0


def test_classic_ones():
    assert _load_solution().count_subarrays_with_sum([1, 1, 1], 2) == 2


def test_increasing():
    assert _load_solution().count_subarrays_with_sum([1, 2, 3], 3) == 2  # [1,2] and [3]


def test_all_zeros_summing_to_zero():
    # n=3 has 6 contiguous subarrays: [0], [0], [0], [0,0], [0,0], [0,0,0]
    assert _load_solution().count_subarrays_with_sum([0, 0, 0], 0) == 6


def test_negatives_cancel_to_zero():
    assert _load_solution().count_subarrays_with_sum([1, -1, 1], 0) == 2  # [1,-1] and [-1,1]


def test_negative_k():
    assert _load_solution().count_subarrays_with_sum([-1, -2, -3], -3) == 2  # [-1,-2] and [-3]


@pytest.mark.timeout(2)
def test_performance_gated_n100k():
    # n=100_000 random small ints. Naive O(n^2) = 10^10 ops ⇒ minutes.
    # Efficient prefix-sum-hashmap = 10^5 ops ⇒ ms.
    random.seed(7)
    n = 100_000
    arr = [random.randint(-2, 2) for _ in range(n)]
    k = 0
    # Compute ground truth via the same efficient algorithm so the test
    # only checks the box agrees, not asks the box to match a brute count.
    from collections import defaultdict
    prefix = 0
    counts = defaultdict(int)
    counts[0] = 1
    expected = 0
    for x in arr:
        prefix += x
        expected += counts[prefix - k]
        counts[prefix] += 1

    assert _load_solution().count_subarrays_with_sum(arr, k) == expected
