import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    centered = x - np.mean(x)
    n = len(x)
    var = float(np.sum(centered ** 2)/(n-1))
    std = float(np.sqrt(var))
    return {
        "variance": var,
        "std_dev": std
    }