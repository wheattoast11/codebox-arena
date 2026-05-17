# edit_distance

Write a function `edit_distance(s1, s2)` that returns the minimum
number of single-character edits (insertions, deletions, or
substitutions) required to convert `s1` into `s2`. Also known as
Levenshtein distance.

- `edit_distance("", "")` → `0`
- `edit_distance("abc", "abc")` → `0`
- `edit_distance("", "abc")` → `3` (three insertions)
- `edit_distance("abc", "")` → `3` (three deletions)
- `edit_distance("kitten", "sitting")` → `3` (k→s, e→i, +g)

Both inputs are strings (may be empty). Comparison is case-sensitive.

## signature

```python
def edit_distance(s1, s2):
    ...
```

## verifier

`tests/test_edit_distance.py` — must pass under `pytest`. Tests cover
both-empty, identical, one-empty (each direction), classic
kitten→sitting case, single substitution, single insertion, single
deletion, case sensitivity, and an unrelated-strings case.

## difficulty

hard · classic 2D DP · base cases are matrix row/column 0
