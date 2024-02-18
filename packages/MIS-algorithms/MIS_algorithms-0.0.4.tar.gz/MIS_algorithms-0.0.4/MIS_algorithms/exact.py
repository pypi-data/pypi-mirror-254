import networkx as nx
from communities.algorithms import bron_kerbosch
from pulp import LpProblem, LpVariable, lpSum, LpMaximize

from .functions.is_maximal_independent_set import is_maximal_independent_set


def exact(G: nx.Graph) -> list:
    """
    Find a maximum independent set in a graph using the exact algorithm.

    Parameters:
    - G (nx.Graph): The input graph.

    Returns:
    - list: List of nodes forming a maximum independent set.
    """
    
    G_complement = nx.complement(G)
    A = nx.to_numpy_array(G_complement)
    output = bron_kerbosch(A, pivot=True)
    max_independent_set = max(output, key=lambda x: len(x))
    
    # Convert node indices to 1-based indexing
    max_independent_set = [i + 1 for i in max_independent_set]
    
    if is_maximal_independent_set(G, max_independent_set):
        return max_independent_set   
    
    else:
        print('Exact algorithm did not return MIS.')
        exit()
        

def exact_sparse(G: nx.Graph) -> list:
    """
    Find a maximum independent set in a graph using a linear programming-based approach.

    Parameters:
    - G (nx.Graph): The input graph.

    Returns:
    - list: List of nodes forming a maximum independent set.
    """
    
    # Create a binary variable for each node indicating whether it is in the independent set
    nodes = list(G.nodes())
    x = LpVariable.dicts("x", nodes, cat='Binary')

    # Create the linear programming problem
    prob = LpProblem("Maximum_Independent_Set", LpMaximize)

    # Objective function: maximize the sum of variables (nodes in the independent set)
    prob += lpSum(x[node] for node in nodes)

    # Constraint: adjacent nodes cannot both be in the independent set
    for edge in G.edges():
        prob += x[edge[0]] + x[edge[1]] <= 1

    # Solve the problem
    prob.solve()

    # Get the nodes in the independent set
    max_independent_set = [node for node in nodes if x[node].value() == 1]

    if is_maximal_independent_set(G, max_independent_set):
        return max_independent_set   
    
    else:
        print('Exact algorithm did not return MIS.')
        exit()


def exact_bipartite(G: nx.Graph) -> list:
    """
    Find an exact solution for an independent set in a bipartite graph.

    Parameters:
    - G (nx.Graph): The input bipartite graph.

    Returns:
    - list: List of nodes forming an independent set.
    """
    
    # Find a maximum matching in the bipartite graph
    matching = nx.bipartite.maximum_matching(G)
    
    # Convert the matching to a minimum vertex cover
    vertex_cover = nx.bipartite.to_vertex_cover(G, matching)
    
    # The exact independent set is the complement of the minimum vertex cover
    max_independent_set = list(set(G) - vertex_cover)
    
    if is_maximal_independent_set(G, max_independent_set):
        return max_independent_set   
    
    else:
        print('Exact algorithm did not return MIS.')
        exit()