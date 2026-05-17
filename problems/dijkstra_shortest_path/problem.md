# dijkstra_shortest_path

**Extend the existing `shortest_path` BFS** (in `current_implementation.py`)
to add a NEW function `dijkstra(graph, start, end)` that handles
**weighted edges** via Dijkstra's algorithm.

The starting code is a working unweighted BFS that returns the number
of edges in the shortest path between two nodes. Your job is to add
a function that handles edge weights — the input is now a dict-of-dicts.

## API additions

- `dijkstra(graph, start, end)` — returns the **sum of edge weights**
  on the shortest weighted path between `start` and `end`. Returns `-1`
  if no path exists. Raises `KeyError` if `start` or `end` is not in
  `graph`. All edge weights are non-negative integers.

Input format for weighted graphs:
```python
{
    "A": {"B": 5, "C": 2},   # node A connects to B (weight 5) and C (weight 2)
    "B": {"A": 5, "C": 1},
    "C": {"A": 2, "B": 1},
}
```

This is **different** from the unweighted BFS format (`{"A": ["B", "C"]}`).
The `dijkstra` function uses the new dict-of-dicts format.

## examples

- `dijkstra({"A": {}}, "A", "A")` → `0`
- `dijkstra({"A": {"B": 5}, "B": {"A": 5}}, "A", "B")` → `5`
- `dijkstra({"A": {"B": 5, "C": 2}, "B": {"A": 5, "C": 1}, "C": {"A": 2, "B": 1}}, "A", "B")` → `3`
  (path A → C → B is weight 2+1 = 3, shorter than direct A → B = 5)

## existing API contract (must keep working)

- `shortest_path(graph, start, end)` — unweighted BFS on adjacency-list
  graph; returns number of edges or `-1` if no path. Raises `KeyError`
  if missing.

## verifier

`tests/test_dijkstra_shortest_path.py` — includes both the prior
unweighted-BFS tests AND new weighted Dijkstra tests.

## difficulty

iter70 · extend-mode · data-structure-replacement test — the box must
recognize that adapting BFS to weighted edges requires replacing the
FIFO queue with a min-priority queue (heapq), AND adapt the input
format from adjacency list to adjacency dict-of-dicts
