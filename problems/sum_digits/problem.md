# sum_digits

Write a function `sum_digits(n)` that returns the sum of the decimal
digits of a non-negative integer `n`.

`sum_digits(0)` returns `0`. For negative inputs the function raises
`ValueError`.

## signature

```python
def sum_digits(n):
    ...
```

## verifier

`tests/test_sum_digits.py` — must pass under `pytest`. Tests check
zero, a single digit, a multi-digit number, a number with a 0 in
the middle, and the negative-input ValueError contract.

## difficulty

easy
