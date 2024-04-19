"""Mocks for function tests"""

import sys

INF = sys.maxsize
short_graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
medium_graph = [
    [0, 5, INF, 10, INF],
    [INF, 0, 3, INF, INF],
    [INF, INF, 0, 1, INF],
    [5, INF, INF, 0, 2],
    [INF, INF, INF, INF, 0],
]
large_graph = [
    [0, 5, INF, 10, INF, INF, 7, INF],
    [INF, 0, 3, INF, INF, INF, INF, INF],
    [INF, INF, 0, 1, INF, 6, INF, INF],
    [1, INF, INF, 0, 2, INF, INF, INF],
    [INF, 4, INF, INF, 0, 4, INF, INF],
    [INF, INF, INF, INF, INF, 0, 1, INF],
    [INF, 4, INF, INF, INF, INF, 0, 3],
    [INF, INF, INF, INF, INF, INF, INF, 0],
]
