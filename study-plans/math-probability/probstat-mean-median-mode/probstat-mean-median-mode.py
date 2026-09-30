import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode = float(np.unique(x, return_counts=True)[0][np.argmax(np.unique(x, return_counts=True)[1])])
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }