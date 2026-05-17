# two_sum_count_pairs

Write a function `count_pairs_with_sum(arr, target)` that returns the
number of **unordered pairs** `(i, j)` with `i < j` such that
`arr[i] + arr[j] == target`.

`arr` is a list of integers (may contain duplicates). `target` is an
integer.

For example:
- `count_pairs_with_sum([1, 2, 3, 4], 5)` → `2` ((1,4) and (2,3))
- `count_pairs_with_sum([1, 1, 1], 2)` → `3` (every pair of the three 1's)
- `count_pairs_with_sum([0, 0, 0, 0], 0)` → `6` (C(4,2))
- `count_pairs_with_sum([], 0)` → `0`
- `count_pairs_with_sum([5], 5)` → `0` (need two distinct indices)
- `count_pairs_with_sum([-1, 1, 2, -2, 3], 0)` → `2` ((-1,1) and (2,-2))

The verifier includes both **correctness tests** (small `n`) and
**performance-gated tests** (`n = 100_000`, with `pytest.mark.timeout(2)`).
A naive O(n²) implementation will pass correctness but **fail timeout**.
Efficient O(n) is required — the canonical approach is a single pass
using a hashmap of value→count, accumulating pair-counts as you go.

## signature

```python
def count_pairs_with_sum(arr, target):
    ...
```

## verifier

`tests/test_two_sum_count_pairs.py` — covers empty, single element,
duplicates (where the pair count is combinatorial), zero target with
negative+positive cancels, and a perf-gated test at `n = 100_000`.

## difficulty

perf-gated · classic two-sum extended to count pairs · brute O(n²) is
correct but times out, the trick is the running-hashmap accumulator
