from collections import deque


def shortest_path(graph, start, end):
    """
    Returns the length (number of edges) of the shortest path between
    two nodes in an undirected, unweighted graph.
    Returns -1 if no path exists.
    Raises KeyError if start or end is not a key in graph.
    """
    if start not in graph:
        raise KeyError(f"Start node '{start}' not in graph")
    if end not in graph:
        raise KeyError(f"End node '{end}' not in graph")

    if start == end:
        return 0

    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])

    while queue:
        current, dist = queue.popleft()
        for neighbor in graph[current]:
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1
