# __init__.py

# Import important classes, functions, or variables that you want to make available when the package is imported.
from .continuation import continuation
from .exact import exact, exact_sparse, exact_bipartite
from .greedy import greedy
from .lotkavolterra import lotka_volterra

from .generate_graphs.erdos_renyi import erdos_renyi
from .generate_graphs.random_bipartite import random_bipartite
from .generate_graphs.random_geometric import random_geometric

from .functions.is_maximal_independent_set import is_maximal_independent_set
from .functions.reduced_graph import reduced_graph


# Define the __all__ variable to specify what should be imported when using "from my_package import *".
__all__ = ['continuation', 
           'exact', 
           'exact_sparse', 
           'exact_bipartite', 
           'greedy', 
           'lotka_volterra',
           'erdos_renyi',
           'random_bipartite',
           'random_geometric',
           'is_maximal_independent_set',
           'reduced_graph'
           ]