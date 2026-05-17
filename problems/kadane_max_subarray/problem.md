# kadane_max_subarray

Write a function `max_subarray(nums)` that returns the largest sum of
any contiguous (non-empty) subarray of the input list.

For example, `max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` returns `6`
(from the subarray `[4, -1, 2, 1]`).

If `nums` is empty the function raises `ValueError`. The input may
contain negative numbers, zeros, and positive numbers in any order.

## signature

```python
def max_subarray(nums):
    ...
```

## verifier

`tests/test_kadane_max_subarray.py` — must pass under `pytest`. Tests
cover the classic Kadane case, an all-negative case (answer is the
single largest element), a single-element case, an all-positive case,
and the empty-input ValueError contract.

## difficulty

medium · classic Kadane dynamic-programming pattern
