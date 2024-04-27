"""Decribe waht this function does"""


def validate_graph(graph):
    if not isinstance(graph, list):
        raise TypeError("Invalid format: argument should be a list")
