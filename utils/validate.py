"""Utility functions for validating graph structures."""


def validate_graph(graph):
    """
    Validates that the input is a list.

    Raises:
    TypeError: If `graph` is not a list.

    Returns:
    None.
    """
    if not isinstance(graph, list):
        raise TypeError("Invalid format: argument should be a list")
