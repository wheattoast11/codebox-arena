# wildcard_regex_match

Write a function `wildcard_match(s, p)` that returns `True` if the
pattern `p` matches the entire string `s`, `False` otherwise. The
pattern recognizes two wildcards:

- `?` matches any single character
- `*` matches any sequence of characters (including the empty sequence)

All other characters in `p` match themselves literally. Matching must
cover the entire string (not a substring).

For example:
- `wildcard_match("abc", "a?c")` → `True`
- `wildcard_match("abcde", "a*e")` → `True`
- `wildcard_match("abc", "a*c*")` → `True`
- `wildcard_match("abc", "*")` → `True`
- `wildcard_match("", "*")` → `True`
- `wildcard_match("", "")` → `True`
- `wildcard_match("abc", "a?d")` → `False`
- `wildcard_match("abc", "ab")` → `False`
- `wildcard_match("abc", "abcd")` → `False`

## signature

```python
def wildcard_match(s, p):
    ...
```

## verifier

`tests/test_wildcard_regex_match.py` — must pass under `pytest`. Tests
cover empty cases, literal-only, single-`?`, single-`*`, multiple `*`,
star-at-end, star-at-start, adjacent stars, and a longer mixed case.

## difficulty

novel-shape · wildcards composed with 2D DP · the `*` recurrence
(skip-the-star OR consume-one-char) is the trick
