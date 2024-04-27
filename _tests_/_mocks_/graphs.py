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
    [INF, 0, 3, INF, INF, 4, INF, 5],
    [INF, INF, 0, 1, INF, 6, INF, INF],
    [1, INF, INF, 0, 2, INF, 2, INF],
    [INF, 4, INF, INF, 0, 4, INF, INF],
    [INF, 4, INF, INF, INF, 0, 1, INF],
]


short_graph_solution = [
    [0, 5, 8, 9],
    [INF, 0, 3, 4],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0],
]

medium_graph_solution = [
    [0, 5, 8, 9, 11],
    [9, 0, 3, 4, 6],
    [6, 11, 0, 1, 3],
    [5, 10, 13, 0, 2],
    [
        INF,
        INF,
        INF,
        INF,
        0,
    ],
]

large_graph_solution = [
    [0, 5, 8, 9, 11, 9, 7, INF],
    [5, 0, 3, 4, 6, 4, INF, 5],
    [2, 7, 0, 1, 3, 6, INF, INF],
    [1, 6, 9, 0, 2, 6, 2, INF],
    [9, 4, 7, 8, 0, 4, INF, INF],
    [9, 4, 7, 8, 10, 0, 1, INF],
]
