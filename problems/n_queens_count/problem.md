# n_queens_count

Write a function `n_queens_count(n)` that returns the number of
distinct solutions to the n-queens puzzle: placing `n` chess queens
on an `n × n` board such that no two queens attack each other (same
row, same column, or same diagonal).

For example:
- `n_queens_count(1)` → `1`
- `n_queens_count(2)` → `0`
- `n_queens_count(3)` → `0`
- `n_queens_count(4)` → `2`
- `n_queens_count(8)` → `92`

For `n <= 0` raise `ValueError`.

## signature

```python
def n_queens_count(n):
    ...
```

## verifier

`tests/test_n_queens_count.py` — must pass under `pytest`. Tests
cover the trivial n=1 case, no-solution cases (n=2, n=3), the
classic n=4 → 2 case, n=5 → 10, n=6 → 4, n=8 → 92, and the
ValueError contract for invalid n.

The verifier uses n up to 8. A brute O(n!) enumeration works but is
slow; the canonical efficient approach uses backtracking with three
sets (column, +diagonal, -diagonal) for O(1) constraint checks at
each row.

## difficulty

novel-shape · backtracking composed with constraint-tracking sets ·
the constraint-as-set-membership encoding is the trick (vs. O(n)
per-row scans)
