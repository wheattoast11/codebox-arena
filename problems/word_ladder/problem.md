# word_ladder

Write a function `word_ladder(begin, end, word_list)` that returns the
length of the **shortest transformation sequence** from `begin` to
`end`, where:

- only one letter can change at a time
- each intermediate word must be in `word_list`
- the `end` word must be in `word_list`
- the `begin` word need not be in `word_list`
- the length counts the **number of words** in the sequence (including
  `begin` and `end`)

Return `0` if no valid sequence exists.

For example:
- `word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])` → `5`
  (hit → hot → dot → dog → cog)
- `word_ladder("hit", "cog", ["hot","dot","dog","lot","log"])` → `0`
  (no `cog` in word list)
- `word_ladder("a", "c", ["a","b","c"])` → `2`
  (a → c is a single one-letter change)

All inputs are lowercase ASCII; `begin` and `end` are the same length.
The word list has no duplicates.

## signature

```python
def word_ladder(begin, end, word_list):
    ...
```

## verifier

`tests/test_word_ladder.py` — must pass under `pytest`. Tests cover
the classic hit→cog case, missing-end, trivial single-step, no path
exists in disconnected word graph, same-word case, and a case where
two different paths exist (BFS must pick the shortest).

## difficulty

novel-shape · BFS composed with adjacency-on-the-fly (build neighbors
by one-letter mutation) · recognizing the graph-from-strings is the trick
