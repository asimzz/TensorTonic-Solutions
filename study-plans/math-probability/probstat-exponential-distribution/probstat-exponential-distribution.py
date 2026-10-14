from math import exp

def exponential_distribution(lam: float, t: float) -> dict:
    """
    Returns the PDF, CDF, survival probability, mean, and variance.
    """
    exponential_term = exp(-lam * t)
    cdf = 1 - exponential_term
    pdf = lam * exponential_term
    mean = 1/lam
    variance = 1/lam**2
    survival = exponential_term

    return {
        "cdf": cdf,
        "mean": mean,
        "pdf": pdf,
        "survival": survival,
        "variance": variance
    }
