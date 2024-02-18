import networkx as nx
import numpy as np


def reduced_graph(G: nx.Graph, node_arr: list) -> nx.Graph:
    """
    Generate a reduced graph by removing a specified set of nodes and their neighbors.

    Parameters:
    - G (nx.Graph): The input graph.
    - node_arr (list): List of nodes to be removed along with their neighbors.

    Returns:
    - nx.Graph: The reduced graph after removing the specified nodes and their neighbors.
    """
    # Create an array to store nodes to be removed.
    remove_arr = []

    # Iterate through each node in the specified set.
    for node in node_arr:
        # Add the current node and its neighbors to the removal array.
        remove_arr = np.append(remove_arr, node)
        remove_arr = np.append(remove_arr, [n for n in G.neighbors(node)])

    # Create a new graph by excluding nodes in the removal array.
    new_graph = [node for node in G if node not in set(remove_arr)]
    G_reduced = G.subgraph(new_graph)

    return G_reduced