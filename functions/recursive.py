"""
Module containing the recursive implementation of the Floyd-Warshall algorithm.
This implementation finds the shortest paths in a weighted graph with positive or
negative edge weights.
"""


def floyd_warshall_recursive(graph):
    """
    Computes the shortest paths in a weighted graph using a recursive approach.

    This function modifies the input graph to reflect the shortest paths between
    all pairs of vertices.

    Parameters:
    graph (list of list of int): A 2D list representing the adjacency matrix of the graph,
    where a high value (like sys.maxsize) represents no direct path between vertices.

    Returns:
    list of list of int: The graph updated to represent the shortest
    path distances between all vertex pairs.
    """

    num_vertices = len(graph)
    state = {}  # Dictionary to cache the results.

    def find_path(inter, start, end):
        """
        Recursively find the shortest path between two vertices with the option to use
        an intermediate vertex.
        """
        # Return cached result if available to avoid redundant calculations.
        if (inter, start, end) in state:
            return state[(inter, start, end)]

        # Base case: No intermediate vertices, directly return the direct path.
        if inter == -1:
            return graph[start][end]

        # Recursive case: Consider paths through the intermediate vertex and directly.
        without_inter = find_path(inter - 1, start, end)
        with_inter = find_path(inter - 1, start, inter) + find_path(
            inter - 1, inter, end
        )

        # The minimum path distance is stored and used.
        result = min(without_inter, with_inter)
        state[(inter, start, end)] = result
        return result

    # Update the graph with the shortest paths computed.
    for inter in range(num_vertices):
        for start in range(num_vertices):
            for end in range(num_vertices):
                graph[start][end] = find_path(inter, start, end)

    return graph
