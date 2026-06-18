from collections import deque
import heapq


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


def dijkstra(graph, start, end):
    """
    Returns the sum of edge weights on the shortest weighted path between
    start and end in a weighted graph.
    Returns -1 if no path exists.
    Raises KeyError if start or end is not in graph.
    """
    if start not in graph:
        raise KeyError(f"Start node '{start}' not in graph")
    if end not in graph:
        raise KeyError(f"End node '{end}' not in graph")

    if start == end:
        return 0

    # Priority queue stores (current_distance, node)
    pq = [(0, start)]
    # Dictionary to keep track of the shortest distance to each node
    distances = {start: 0}
    # Set to keep track of visited nodes (nodes for which we have found the shortest path)
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # If we have already processed this node with a shorter distance, skip
        if current_node in visited:
            continue

        visited.add(current_node)

        # If we reached the end node, return the distance
        if current_node == end:
            return current_dist

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            new_dist = current_dist + weight

            # If a shorter path to neighbor is found, update distance and push to queue
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return -1
