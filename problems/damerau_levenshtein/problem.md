# damerau_levenshtein

**Extend the existing `edit_distance` function** (in
`current_implementation.py`) to add a NEW function `damerau_distance`
that counts a single-character **transposition** as one edit instead
of two substitutions.

The starting code is a working bottom-up 2D DP Levenshtein
implementation. Keep it working — `edit_distance(s1, s2)` must still
return the original Levenshtein value. Add `damerau_distance(s1, s2)`
that follows the Damerau-Levenshtein recurrence.

## API additions

- `damerau_distance(s1, s2)` — same shape as `edit_distance`, but
  when the last two characters of one string are the swap of the last
  two of the other (and the rest matches), count that as 1 edit, not 2.

Specifically (the canonical Damerau-Levenshtein optimal-string-alignment
recurrence):
```
if i >= 2 and j >= 2 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
    dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1)   # transposition
```

## examples

- `damerau_distance("", "")` → `0`
- `damerau_distance("abc", "abc")` → `0`
- `damerau_distance("ab", "ba")` → `1` (single transposition)
- `damerau_distance("abc", "acb")` → `1` (single transposition)
- `damerau_distance("kitten", "sitting")` → `3` (same as Levenshtein here)
- `damerau_distance("ca", "abc")` → `2` (insert b, transpose c↔a)

## existing API contract (must keep working)

- `edit_distance(s1, s2)` — original Levenshtein (no transposition shortcut)
- `edit_distance("ab", "ba")` → `2` (two substitutions, no transposition awareness)

## verifier

`tests/test_damerau_levenshtein.py` — includes both prior Levenshtein
tests and new Damerau-specific tests where transposition matters.

## difficulty

iter70 · extend-mode · algorithm-rule-change test — the box must read
the existing DP and add ONE more case to the recurrence without
breaking the original
