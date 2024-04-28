"""Utility functions for validating graph structures."""


def validate_graph(graph):
    """
    Validates that the input is a list of lists of integers.

    Raises:
    TypeError: If `graph` is not a list or if the elements of the list are not lists of integers.
    ValueError: If any list inside the main list contains non-integer types.

    Returns:
    None.
    """
    if not isinstance(graph, list):
        raise TypeError("Invalid format: argument should be a list")

    for sublist in graph:
        if not isinstance(sublist, list):
            raise TypeError(
                "Invalid format: each item in the graph should be a list of integers"
            )
        for item in sublist:
            if not isinstance(item, int):
                raise ValueError(
                    "Invalid format: all elements in the sublists must be integers"
                )
