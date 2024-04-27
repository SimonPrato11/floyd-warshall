"""
Unit tests for the Floyd-Warshall recursive algorithm implementation.
"""

import unittest
import copy

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
    """Test cases for the Floyd-Warshall recursive algorithm."""

    def test_short_graph(self):
        """
        Test the Floyd-Warshall algorithm with a small graph.
        """
        graph = copy.deepcopy(short_graph)
        expected = short_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_medium_graph(self):
        """
        Test the Floyd-Warshall algorithm with a medium-sized graph.
        """
        graph = copy.deepcopy(medium_graph)
        expected = medium_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_large_graph(self):
        """
        Test the Floyd-Warshall algorithm with a large graph.
        """
        graph = copy.deepcopy(large_graph)
        expected = large_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_invalid_graph(self):
        """
        Test the Floyd-Warshall algorithm with an invalid graph input.
        """
        graph = "This is not a graph"
        with self.assertRaises(TypeError):
            floyd_warshall_recursive(graph)


if __name__ == "__main__":
    unittest.main()
