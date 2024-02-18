import networkx as nx


def is_maximal_independent_set(graph: nx.Graph, independent_set: list, vertices=None, edges=None) -> bool:
    """
    Check if a given set of vertices forms a maximal independent set in a graph.

    Parameters:
    - graph (nx.Graph): The input graph.
    - independent_set (list): List of vertices to be checked for maximality.
    - vertices (list): List of vertices (optional, use if the graph is not provided).
    - edges (list): List of edges (optional, use if the graph is not provided).

    Returns:
    - bool: True if the input set is a maximal independent set, False otherwise.
    """
    if graph is None and (vertices is None or edges is None):
        raise ValueError("Either provide a graph or both vertices and edges.")

    # If the graph is not provided, create one from vertices and edges.
    if graph is None:
        graph = nx.Graph()
        graph.add_nodes_from(vertices)
        graph.add_edges_from(edges)

    # Complement of the independent set.
    complement_set = [node for node in graph.nodes() if node not in independent_set]

    # Check the independence property.
    independence_property = all(not graph.has_edge(u, v) for u in independent_set for v in independent_set)

    # Check the maximality property.
    maximality_checks = [not all(not graph.has_edge(u, v) for v in independent_set) for u in complement_set]
    maximality_property = all(maximality_checks)

    # Return the result.
    return independence_property and maximality_property