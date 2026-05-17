# count_inversions

Write a function `count_inversions(arr)` that returns the number of
**inversions** in the input list: the count of pairs `(i, j)` where
`i < j` and `arr[i] > arr[j]`.

For example:
- `count_inversions([])` → `0`
- `count_inversions([1, 2, 3])` → `0` (sorted has no inversions)
- `count_inversions([3, 2, 1])` → `3` ((3,2), (3,1), (2,1))
- `count_inversions([2, 4, 1, 3, 5])` → `3` ((2,1), (4,1), (4,3))

The verifier includes both **correctness tests** (small `n`) and
**performance-gated tests** (`n = 10_000`, with `pytest.mark.timeout(2)`).
A naive O(n²) implementation will pass correctness but **fail timeout**.
Efficient O(n log n) is required — the canonical approach is a modified
merge-sort that counts inversions during the merge step.

## signature

```python
def count_inversions(arr):
    ...
```

## verifier

`tests/test_count_inversions.py` — must pass under `pytest`. Tests cover
empty, sorted, reverse-sorted, mixed, single-element, repeated elements,
and a perf-gated test at `n = 10_000` that fails timeout under O(n²).

## difficulty

perf-gated · the brute-force O(n²) is correct but slow · the trick is
recognizing that merge-sort can count cross-pair inversions during merge
