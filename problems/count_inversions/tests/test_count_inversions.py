"""pytest verifier for problems/count_inversions."""
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
    assert _load_solution().count_inversions([]) == 0


def test_single():
    assert _load_solution().count_inversions([42]) == 0


def test_sorted_zero():
    assert _load_solution().count_inversions([1, 2, 3, 4, 5]) == 0


def test_reverse_sorted():
    # n*(n-1)/2 inversions for fully reversed
    assert _load_solution().count_inversions([3, 2, 1]) == 3
    assert _load_solution().count_inversions([4, 3, 2, 1]) == 6


def test_mixed():
    assert _load_solution().count_inversions([2, 4, 1, 3, 5]) == 3


def test_repeated_elements():
    # equal elements are NOT inversions (strict >)
    assert _load_solution().count_inversions([1, 1, 1]) == 0
    assert _load_solution().count_inversions([2, 1, 2, 1]) == 3


@pytest.mark.timeout(2)
def test_performance_gated_n10k():
    # n = 10_000, reverse-sorted input.
    # Naive O(n^2) is ~10^8 ops ≈ 10s in Python ⇒ timeout.
    # Efficient O(n log n) is ~10^5 ops ⇒ milliseconds.
    n = 10_000
    arr = list(range(n, 0, -1))
    expected = n * (n - 1) // 2
    assert _load_solution().count_inversions(arr) == expected


@pytest.mark.timeout(2)
def test_performance_gated_random_n5k():
    # Random input at n=5000, still well over what O(n^2) can do in 2s
    random.seed(42)
    arr = random.sample(range(100_000), 5_000)
    # Compute expected via direct O(n^2) on a smaller sample? No — use any correct
    # implementation as ground truth. Use sorted-position-based count via bisect.
    import bisect
    sorted_so_far = []
    expected = 0
    for x in arr:
        idx = bisect.bisect_right(sorted_so_far, x)
        expected += len(sorted_so_far) - idx
        bisect.insort(sorted_so_far, x)
    assert _load_solution().count_inversions(arr) == expected
