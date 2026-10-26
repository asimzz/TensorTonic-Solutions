from math import comb

def binomial_distribution(n: int, p: float, threshold: int) -> dict:
    """
    Returns the PMF, mean, variance, and probability at least threshold.
    """
    mean = n * p
    variance = mean * (1 - p)
    pmf = [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n+1)]
    prob_at_least = sum([comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(threshold, n+1)])
    return {
        "mean": mean,
        "pmf": pmf,
        "prob_at_least": prob_at_least,
        "variance":variance
    }
