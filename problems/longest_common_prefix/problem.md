# longest_common_prefix

Write a function `longest_common_prefix(strs)` that returns the longest
string that is a prefix of every string in the input list.

If `strs` is empty, return `""`. If any string in `strs` is empty,
return `""`. Comparison is case-sensitive.

For example:
- `longest_common_prefix(["flower", "flow", "flight"])` returns `"fl"`
- `longest_common_prefix(["dog", "racecar", "car"])` returns `""`
- `longest_common_prefix(["interspecies", "interstellar", "interstate"])` returns `"inters"`

## signature

```python
def longest_common_prefix(strs):
    ...
```

## verifier

`tests/test_longest_common_prefix.py` — must pass under `pytest`. Tests
cover the empty list, single string, common prefix exists, no common
prefix, empty string in list, and identical strings.

## difficulty

medium · linear-scan or vertical-scan pattern
