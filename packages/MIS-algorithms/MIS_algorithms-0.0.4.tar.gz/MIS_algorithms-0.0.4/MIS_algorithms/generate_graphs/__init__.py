# __init__.py

# Import important classes, functions, or variables that you want to make available when the package is imported.
from .erdos_renyi import erdos_renyi
from .random_bipartite import random_bipartite
from .random_geometric import random_geometric

# Define the __all__ variable to specify what should be imported when using "from my_package import *".
__all__ = ['erdos_renyi', 'random_bipartite', 'random_geometric']