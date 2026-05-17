# subarray_sum_equals_k

Write a function `count_subarrays_with_sum(arr, k)` that returns the
number of **contiguous (non-empty) subarrays** of `arr` whose elements
sum to exactly `k`.

`arr` is a list of integers (positive, negative, or zero). `k` is an
integer.

For example:
- `count_subarrays_with_sum([1, 1, 1], 2)` → `2` (`[1,1]` at index 0 and `[1,1]` at index 1)
- `count_subarrays_with_sum([1, 2, 3], 3)` → `2` (`[1,2]` and `[3]`)
- `count_subarrays_with_sum([], 0)` → `0` (empty list has no subarrays)
- `count_subarrays_with_sum([0, 0, 0], 0)` → `6` (every contiguous subarray)
- `count_subarrays_with_sum([1, -1, 1], 0)` → `2`

The verifier includes both **correctness tests** (small `n`) and
**performance-gated tests** (`n = 100_000`, with `pytest.mark.timeout(2)`).
A naive O(n²) implementation will pass correctness but **fail timeout**.
Efficient O(n) is required — the canonical approach is the
**prefix-sum + hashmap** technique.

## signature

```python
def count_subarrays_with_sum(arr, k):
    ...
```

## verifier

`tests/test_subarray_sum_equals_k.py` — covers empty, single element,
zero sums, negative numbers, classic [1,1,1] case, and a perf-gated test
at `n = 100_000` that fails timeout under O(n²).

## difficulty

perf-gated · prefix-sum-hashmap composition · brute force is O(n²)
which times out, the trick is recognizing that `prefix[j] - prefix[i] = k`
means counting `prefix[i] = prefix[j] - k` via running hashmap
