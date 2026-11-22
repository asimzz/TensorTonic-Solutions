from math import sqrt
from scipy.stats import norm

def z_test_one_sample(x_bar: float, mu_0: float, sigma: float, n: int, alpha: float) -> list:
    """
    Returns the z-statistic, two-sided p-value, and rejection decision.
    """
    z = (x_bar - mu_0)/(sigma/sqrt(n))
    p = 2 * norm.cdf(-abs(z))
    return [z, p, p < alpha]
