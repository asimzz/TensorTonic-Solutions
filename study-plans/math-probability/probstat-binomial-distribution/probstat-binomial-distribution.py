from math import comb

def binomial_distribution(n: int, p: float, threshold: int) -> dict:
    """
    Returns the PMF, mean, variance, and probability at least threshold.
    """
    pmf = [comb(n, k) * (p ** k) * (1 - p) ** (n-k) for k in range(n+1)]
    mean = n * p
    variance = mean * (1 - p)
    tail_prop = sum(comb(n, k) * (p ** k) * (1 - p)** (n-k) for k in range(threshold, n+1))
    return {
        "mean": mean,
        "pmf": pmf,
        "prob_at_least": tail_prop,
        "variance": variance
    }
