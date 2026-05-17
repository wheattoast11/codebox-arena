# balanced_brackets

Write a function `balanced_brackets(s)` that returns `True` if the
brackets in the input string are properly matched and nested, `False`
otherwise.

Recognized bracket pairs: `()`, `[]`, `{}`. Other characters in the
string are ignored (e.g. `"a(b)c"` is balanced; `"a(b"` is not).

The empty string is balanced. Brackets must close in reverse order of
opening — `"([)]"` is **not** balanced even though counts match.

## signature

```python
def balanced_brackets(s):
    ...
```

## verifier

`tests/test_balanced_brackets.py` — must pass under `pytest`. Tests
cover the empty string, simple balanced, simple unbalanced, mixed
types, nested types, interleaved (`([)]` should fail), and the
ignore-non-bracket-chars rule.

## difficulty

medium · stack-based parsing
