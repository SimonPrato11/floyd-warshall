"""
Unit tests for the Floyd-Warshall recursive algorithm implementation.
"""

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
    """Test cases for the Floyd-Warshall recursive algorithm."""

    def test_short_graph(self):
        """
        Test the Floyd-Warshall algorithm with a small graph.
        """
        graph = copy.deepcopy(short_graph)
        validate_graph(graph)  # Validate the graph before proceeding
        expected = short_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_medium_graph(self):
        """
        Test the Floyd-Warshall algorithm with a medium-sized graph.
        """
        graph = copy.deepcopy(medium_graph)
        validate_graph(graph)  # Validate the graph before proceeding
        expected = medium_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)

    def test_large_graph(self):
        """
        Test the Floyd-Warshall algorithm with a large graph.
        """
        graph = copy.deepcopy(large_graph)
        validate_graph(graph)  # Validate the graph before proceeding
        expected = large_graph_solution
        result = floyd_warshall_recursive(graph)
        self.assertEqual(result, expected)


class TestValidateGraphFunction(unittest.TestCase):
    """Unit tests for the validate_graph function."""

    def test_validate_graph_with_non_list_input(self):
        """
        Test that the validate_graph function raises a TypeError
        when the input is not a list.
        """
        with self.assertRaises(TypeError) as context:
            validate_graph("This is a string, not a list")

        self.assertEqual(
            str(context.exception), "Invalid format: argument should be a list"
        )

    def test_validate_graph_with_non_integer_in_sublist(self):
        """
        Test that the validate_graph function raises a ValueError
        when any sublist contains non-integer elements.
        """
        graph_with_error = [[1, 2, 3], [4, 5, "six"]]

        with self.assertRaises(ValueError) as context:
            validate_graph(graph_with_error)
        self.assertEqual(
            str(context.exception),
            "Invalid format: all elements in the sublists must be integers",
        )


if __name__ == "__main__":
    unittest.main()
