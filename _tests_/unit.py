import unittest
import copy

from utils.validate import validate_graph
from functions.recursive import floyd_warshall_recursive
from _tests_._mocks_.graphs import (
    short_graph,
    medium_graph,
    large_graph,
    short_graph_solution,
    medium_graph_solution,
    large_graph_solution,
)


class TestFloydWarshallRecursive(unittest.TestCase):
    def test_short_graph(self):
        graph = copy.deepcopy(short_graph)
        expected = short_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_medium_graph(self):
        graph = copy.deepcopy(medium_graph)
        expected = medium_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_large_graph(self):
        graph = copy.deepcopy(large_graph)
        expected = large_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_invalid_graph(self):
        graph = "This is not a graph"
        with self.assertRaises(TypeError):
            floyd_warshall_recursive(graph)


if __name__ == "__main__":
    unittest.main()
