"""Time it"""

from timeit import timeit
import sys

from functions.main import floyd_warshall_recursive
from functions.floyd_algorithm import floydWarshall


RUNS = 100


def benchmark_floyd_warshall_recursive():
    INF = sys.maxsize
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0],
    ]
    floyd_warshall_recursive(graph)


def benchmark_floyd_warshall():
    INF = sys.maxsize
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0],
    ]
    floydWarshall(graph)


iterative_function_time = timeit(benchmark_floyd_warshall, number=RUNS)
recursive_function_time = timeit(benchmark_floyd_warshall_recursive, number=RUNS)

print(f"Time for recursive function: {recursive_function_time:.8f} seconds")
print(f"Time for iterative function : {iterative_function_time:.8f} seconds")
