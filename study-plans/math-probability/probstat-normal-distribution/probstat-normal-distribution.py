from scipy.stats import norm

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """
    z_score = (x - mu)/sigma
    cdf = norm.cdf(x, loc=mu, scale=sigma)
    pdf = norm.pdf(x, loc=mu, scale=sigma)
    prob_within_1_std = norm.cdf(1) - norm.cdf(-1)
    return {
        "cdf": cdf,
        "pdf": pdf,
        "prob_within_1_std": prob_within_1_std,
        "z_score": z_score
    }
