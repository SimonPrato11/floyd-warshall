"""Decribe waht this function does"""


def floyd_warshall_recursive(graph):
    num_vertices = len(graph)
    state = {}  # This dictionary will cache the results of subproblems

    def find_path(inter, start, end):
        # Memoization check: return the cached result if available
        if (inter, start, end) in state:
            return state[(inter, start, end)]

        # Base case: if no intermediate vertices are allowed, return direct path
        if inter == -1:
            return graph[start][end]

        # Recursive case: Compute shortest path with and without the intermediate vertex
        without_inter = find_path(inter - 1, start, end)
        with_inter = find_path(inter - 1, start, inter) + find_path(
            inter - 1, inter, end
        )

        # The minimum of both paths is the shortest path considering up to 'inter' as intermediate
        result = min(without_inter, with_inter)

        # Cache the result before returning
        state[(inter, start, end)] = result
        return result

    # Update the graph with the shortest paths computed recursively
    for inter in range(num_vertices):
        for start in range(num_vertices):
            for end in range(num_vertices):
                graph[start][end] = find_path(inter, start, end)

    return graph
