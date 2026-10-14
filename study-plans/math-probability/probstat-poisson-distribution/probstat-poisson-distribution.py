from math import exp, factorial

def poisson_distribution(lam: float, max_k: int) -> list:
    """
    Returns the PMF list, cumulative probability, and zero-event probability.
    """
    pmf = [(lam ** k * exp(-lam))/factorial(k) for k in range(max_k+1)]
    return [pmf, sum(pmf), exp(-lam)]
