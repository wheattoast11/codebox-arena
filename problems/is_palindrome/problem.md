# is_palindrome

Write a function `is_palindrome(s)` that returns `True` if the input
string reads the same forwards and backwards, `False` otherwise.

Comparison is **case-insensitive** and ignores spaces. Punctuation
is treated as a regular character (no stripping). The empty string
is a palindrome.

## signature

```python
def is_palindrome(s):
    ...
```

## verifier

`tests/test_is_palindrome.py` — must pass under `pytest`. Tests check
empty, simple palindromes, non-palindromes, mixed case, and a phrase
with spaces.

## difficulty

easy
