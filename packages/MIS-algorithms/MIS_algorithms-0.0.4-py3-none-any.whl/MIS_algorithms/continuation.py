import networkx as nx
import numpy as np
import random
from scipy import integrate, linalg
import warnings

from .functions.is_maximal_independent_set import is_maximal_independent_set
from .functions.reduced_graph import reduced_graph


def LV_integrate(G: nx.Graph, tau: float, x0: np.ndarray, t_end: int = 1e7) -> np.ndarray:
    """Integrate the generalized Lotka-Volterra equations.

    Parameters:
    - G (nx.Graph): The input graph.
    - tau (float): A parameter in the equations.
    - x0 (np.ndarray): Initial state.
    - t_end (int): End time for integration.

    Returns:
    - np.ndarray: The integrated state.
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        # Define the correct parameters
        A = nx.to_numpy_array(G)
        r = np.ones(len(G))
        M = -tau * A - np.identity(len(G))

        # Define the generalized Lotka-Volterra equations and its jacobian
        f = lambda t, x: np.diag(x) @ (r + M @ x)
        J = lambda t, x: np.identity(r) + np.diag(x) @ M + np.diag(M @ x)

        # Set integration methods.
        ode15s = integrate.ode(f, J)
        ode15s.set_integrator('dopri5')

        # Stop integration upon bifurcation
        def solout(t, x):
            if min(x) < 1e-6:
                return -1
            else:
                return 0

        ode15s.set_solout(solout)
        ode15s.set_initial_value(x0, 0)

        # Integrate system.
        y = ode15s.integrate(t_end)
        y = np.transpose(y)

        return y


def F(point: np.ndarray) -> float:
    """Calculate product of array elements.

    Parameters:
    - point (np.ndarray): Input array.

    Returns:
    - float: The product of array elements.
    """
    return np.prod(point)


def dxdtau(A: np.ndarray, tau: float) -> np.ndarray:
    """Calculate derivative of interior fixed point as a function of tau.

    Parameters:
    - A (np.ndarray): Input matrix.
    - tau (float): A parameter.

    Returns:
    - np.ndarray: The calculated derivative.
    """
    M = tau * A + np.identity(len(A))
    prod1 = linalg.solve(-M, np.ones(len(A)), assume_a='sym')
    prod2 = linalg.solve(M, prod1, assume_a='sym')
    return A @ prod2


def dFdtau(A: np.ndarray, tau: float, point: np.ndarray) -> float:
    """Calculate derivative of functional as a function of tau.

    Parameters:
    - A (np.ndarray): Input matrix.
    - tau (float): A parameter.
    - point (np.ndarray): Input array.

    Returns:
    - float: The calculated derivative.
    """
    derivatives = dxdtau(A, tau)
    total_product = np.prod(point)

    if min(np.abs(point)) > 1e-100:
        products = total_product / point
        return np.sum(derivatives * products)
    else:
        products = np.array([np.prod([point[j] for j in range(len(point)) if j != i]) for i in range(len(point))])
        return np.sum(derivatives * products)


def newton_method(F: callable, tau_initial: float, tolerance: float, G: nx.Graph) -> float:
    """Find bifurcation tau.

    Parameters:
    - F (callable): Function.
    - tau_initial (float): Initial value of tau.
    - tolerance (float): Tolerance value.
    - G (nx.Graph): The input graph.

    Returns:
    - float: The bifurcation tau.
    """
    A = nx.to_numpy_array(G)
    tau_max = 1 / abs(np.linalg.eigvalsh(A)[0])
    dt = 1e200

    tau = tau_initial
    iteration = 0
    max_iterations = 500

    while dt > tolerance and tau < tau_max and iteration < max_iterations:
        M = tau * A + np.identity(len(G))

        try:
            point = linalg.solve(M, np.ones(len(A)), assume_a='sym')
            dFdtau_value = dFdtau(A, tau, point)

            if abs(dFdtau_value) < 1e-200:
                break

            tau1 = tau - F(point) / dFdtau_value

        except:
            return tau_max, True

        dt = abs(tau1 - tau)
        tau = tau1
        iteration += 1

    if abs(tau - tau_max) < 1e-5:
        return tau_max, True
    else:
        if min(point) < 1e-3:
            return min(tau, tau_max), min(tau, tau_max) == tau_max
        else:
            return tau_max, True


def transcritical_removal(H: nx.Graph, tau_bif: float, comments: bool = False) -> list:
    """Determine bifurcated variables at transcritical bifurcation.

    Parameters:
    - H (nx.Graph): The input graph.
    - tau_bif (float): Bifurcation tau.
    - comments (bool): Whether to print comments.

    Returns:
    - list: List of nodes to be removed.
    """
    set_off_factor = 1
    H0 = nx.to_numpy_array(H)

    while True and tau_bif * set_off_factor < 1.5:
        try:
            final_state = linalg.solve((tau_bif * set_off_factor) * H0 + np.identity(len(H0)),
                                       np.ones(len(H0)), assume_a='sym')

        except:
            nodes_to_remove = []
            break

        nodes_to_remove = [node for i, node in enumerate(H) if final_state[i] < 1e-5]

        if len(nodes_to_remove) == 0:
            set_off_factor *= 1.0001
            if comments:
                print('Bifurcation did not occur. Setoff increased.')
        else:
            break

    return nodes_to_remove


def pitchfork_removal(H: nx.Graph, tau_bif: float, comments: bool = False) -> list:
    """Determine bifurcated variables at pitchfork bifurcation.

    Parameters:
    - H (nx.Graph): The input graph.
    - tau_bif (float): Bifurcation tau.
    - comments (bool): Whether to print comments.

    Returns:
    - list: List of nodes to be removed.
    """
    setoff_backward_factor = 0.999
    setoff_forward_factor = 1
    t_end = 1e15
    perturbation = 1e-5
    selection_threshold = 1e-4

    H0 = nx.to_numpy_array(H)
    tau_f = tau_bif

    # State before bifurcation
    tau_b = tau_bif * setoff_backward_factor
    initial_state = linalg.solve(tau_b * H0 + np.identity(len(H0)), np.ones(len(H0)), assume_a='sym')
    initial_state_perturbed = [item if item < selection_threshold or item > 1 - selection_threshold
                               else item + random.uniform(0, perturbation) for item in initial_state]

    # Keep running loop until bifurcation has occurred. This can happen because Newton methods are not specific enough
    while True:
        tau_f = tau_bif * setoff_forward_factor

        # Determine values after bifurcation
        final_state = LV_integrate(H, tau_f, initial_state_perturbed, t_end=t_end)

        nodes_to_remove = [node for i, node in enumerate(H) if final_state[i] < selection_threshold]

        if len(nodes_to_remove) == 0:
            setoff_forward_factor *= 1.005
            t_end *= 10
            perturbation *= 2
            if comments:
                print('Bifurcation did not occur. Setoff increased.')

        elif tau_f > 10:
            print('Algorithm failed. Pitchfork bifurcation did not occur!')
            exit()
        else:
            break

    return nodes_to_remove


def continuation_iteration(G: nx.Graph, comments: bool = False) -> list:
    """Numerical Continuation Lotka-Volterra Algorithm without guaranteed maximality.

    Parameters:
    - G (nx.Graph): The input graph.
    - comments (bool): Whether to print comments.

    Returns:
    - list: List of nodes.
    """
    # Make a copy of the graph G to not disturb it.
    H = G.copy()

    # Set parameters for numerical continuation.
    tau_initial = 1e-10
    tolerance_newton = 1e-8
    nodes_bifurcated = []

    # While there is still a fixed point inside the interior, keep iterating.
    while H.number_of_edges() > 0:

        # Determine the value of tau at which the next bifurcation happens.
        subgraphs = [H.subgraph(subgraph) for subgraph in list(nx.connected_components(H)) if
                      len(H.subgraph(subgraph)) != 1]
        bifurcation_points = [newton_method(F, tau_initial, tolerance_newton, subgraph) for subgraph in subgraphs]
        tau_bif = min([bifurcation_point[0] for bifurcation_point in bifurcation_points])
        pitchfork_flag = any(
            [bifurcation_point[1] for bifurcation_point in bifurcation_points if
             abs(bifurcation_point[0] - tau_bif) < 1e-5])

        if not pitchfork_flag:
            """Transcritical bifurcation"""
            nodes_to_remove = transcritical_removal(H, tau_bif, comments)

            if len(nodes_to_remove) == 0:
                pitchfork_flag = True

            if comments:
                print('Bifurcation type: Transcritical')

        elif pitchfork_flag:
            """Pitchfork bifurcation"""
            nodes_to_remove = pitchfork_removal(H, tau_bif, comments)

            if comments:
                print('Bifurcation type: Pitchfork')

        nodes_bifurcated.extend(nodes_to_remove)

        # Remove the bifurcated vertices from G
        H.remove_nodes_from(nodes_bifurcated)

        if comments:
            print(f'Network size: {len(H)}\n')

    # Return maximal independent set
    return list(H.nodes())


def continuation(G: nx.Graph, comments: bool = False) -> list:
    """Numerical Continuation Lotka-Volterra Algorithm with guaranteed maximality.

    Parameters:
    - G (nx.Graph): The input graph.
    - comments (bool): Whether to print comments.

    Returns:
    - list: List of nodes.
    """
    G_copy = G.copy()
    output = []
    G_reduced = reduced_graph(G_copy, output)

    # We run the algorithm until maximality condition is satisfied
    while not is_maximal_independent_set(G, output) and len(G_reduced) != 0:

        output_iteration = continuation_iteration(G_reduced, comments)
        output = list(set(np.append(output, output_iteration)))

        G_reduced = reduced_graph(G_copy, output)

    if is_maximal_independent_set(G, output):
        return [int(item) for item in output]

    else:
        print('Continuation algorithm did not return MIS.')
        exit()