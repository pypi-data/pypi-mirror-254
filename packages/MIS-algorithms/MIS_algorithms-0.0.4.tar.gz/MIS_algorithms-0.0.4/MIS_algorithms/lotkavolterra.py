import numpy as np
import networkx as nx
from scipy import integrate
import warnings

from .functions.is_maximal_independent_set import is_maximal_independent_set

def lotka_volterra(G: nx.Graph, tau: float, x0: np.ndarray) -> list:
    """
    Perform integration of the generalized Lotka-Volterra equations on the given graph.

    Parameters:
    - G (nx.Graph): The input graph.
    - tau (float): A parameter for the community matrix calculation.
    - x0 (np.ndarray): The initial state of the system.

    Returns:
    - list: List of nodes forming an independent set based on the Lotka-Volterra dynamics.
    """

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        A = nx.to_numpy_array(G)
        M = tau * A + np.identity(len(A))

        # Define the generalized Lotka-Volterra equations and its Jacobian
        f = lambda t, x: x - np.dot(np.dot(np.diag(x), M), x)
        J = lambda t, x: np.identity(len(A)) - (np.dot(np.diag(x), M) + np.diag(np.dot(M, x)))

        # Set up the ODE solver
        ode_solver = integrate.ode(f, J)
        ode_solver.set_integrator('dopri5')

        # Stop integration when all nodes converge to 0 or 1
        def solout(t, x):
            return -1 if np.all((x < 1e-5) | (x > 1 - 1e-5)) else 0

        ode_solver.set_solout(solout)

        # Integrate until binary output
        while True:
            t_end = 1e9
            ode_solver.set_initial_value(x0, 0)
            y = ode_solver.integrate(t_end)

            if solout(t_end, y) == -1:
                break

            x0 = y

        y = np.transpose(y)

        # Determine variables that converge to one
        nodes_arr = list(G.nodes())
        max_independent_set = [nodes_arr[i] for i in range(len(G)) if y[i] > 1 - 1e-5]

        if is_maximal_independent_set(G, max_independent_set):
            return max_independent_set
        else:
            print('Lotka-Volterra algorithm did not return MIS.')
            exit()