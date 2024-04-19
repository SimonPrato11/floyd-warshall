"""Time it"""

import timeit
import copy


from functions.recursive import floyd_warshall_recursive
from functions.iterative import floydWarshall
from _tests_._mocks_.graphs import short_graph, medium_graph, large_graph


RUNS = 100


def benchmark_floyd_warshall_recursive(graph):
    graph_copy = copy.deepcopy(graph)

    def test():
        floyd_warshall_recursive(graph_copy)

    return test


def benchmark_floyd_warshall(graph):
    graph_copy = copy.deepcopy(graph)

    def test():
        floydWarshall(graph_copy)

    return test


if __name__ == "__main__":
    graphs = {"short": short_graph, "medium": medium_graph, "large": large_graph}

    for name, graph in graphs.items():
        print(f"Testing {name} graph:")
        iterative_function_time = timeit.timeit(
            benchmark_floyd_warshall(graph), number=RUNS
        )
        recursive_function_time = timeit.timeit(
            benchmark_floyd_warshall_recursive(graph), number=RUNS
        )

        print(
            f"Time for recursive function on {name} graph: {recursive_function_time:.8f} seconds"
        )
        print(
            f"Time for iterative function on {name} graph : {iterative_function_time:.8f} seconds"
        )

# python -m _tests_.performance from root
