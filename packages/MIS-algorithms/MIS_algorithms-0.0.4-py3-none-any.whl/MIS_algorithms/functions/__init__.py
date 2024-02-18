# __init__.py

# Import important classes, functions, or variables that you want to make available when the package is imported.
from .is_maximal_independent_set import is_maximal_independent_set
from .reduced_graph import reduced_graph

# Define the __all__ variable to specify what should be imported when using "from my_package import *".
__all__ = ['is_maximal_independent_set', 'reduced_graph']