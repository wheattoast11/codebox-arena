# graph_bfs_shortest_path

Write a function `shortest_path(graph, start, end)` that returns the
length (number of edges) of the shortest path between two nodes in an
**undirected, unweighted** graph. Return `-1` if no path exists.

The graph is passed as an adjacency dict: keys are node identifiers
(strings or ints), values are lists of neighbor identifiers. Self-loops
and parallel edges may be present and must not break the algorithm.

- `shortest_path({"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A", "C")` → `2`
- `shortest_path({"A": ["B"], "B": ["A"], "C": []}, "A", "C")` → `-1`
- `shortest_path({"A": []}, "A", "A")` → `0`

If `start` or `end` is not a key in `graph`, raise `KeyError`.

## signature

```python
def shortest_path(graph, start, end):
    ...
```

## verifier

`tests/test_graph_bfs_shortest_path.py` — must pass under `pytest`.
Tests cover trivial (start == end), 2-hop, longer chain, disconnected,
self-loop in path, parallel edges, missing-node KeyError.

## difficulty

hard · BFS with visited set, handles disconnected and self-loops
