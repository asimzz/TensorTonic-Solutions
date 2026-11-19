from math import sqrt
from scipy.stats import norm

def sampling_distribution(mu: float, sigma: float, n: int, threshold: float) -> dict:
    """
    Returns the sampling mean, sampling standard deviation, and lower-tail probability.
    """
    sampling_mean = mu
    sampling_std = sigma/sqrt(n)
    threshold_standarized = (threshold - mu) / sampling_std
    prob_below_threshold = norm.cdf(threshold_standarized)
    return {
        "prob_below_threshold": prob_below_threshold,
        "sampling_mean": sampling_mean,
        "sampling_std": sampling_std
    }
    
