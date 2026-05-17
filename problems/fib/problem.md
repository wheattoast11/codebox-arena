# fib

Write a function `fib(n)` that returns the n-th Fibonacci number, with
`fib(0) == 0` and `fib(1) == 1`.

## signature

```python
def fib(n):
    ...
```

## verifier

`tests/test_fib.py` — must pass under `pytest`. Tests check `fib(0)`,
`fib(1)`, `fib(10)`, and `fib(20)` so memoization or an iterative form
is recommended; naive recursion will pass but be slow.

## difficulty

easy
