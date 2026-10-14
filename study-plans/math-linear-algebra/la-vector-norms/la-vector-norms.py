import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    v = np.asarray(v)
    l1 = sum(abs(v))
    l2 = np.sqrt(sum(v ** 2))
    infinity_norms = max(abs(v))
    return np.asarray([l1, l2, infinity_norms])