import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    a_dot_b = np.dot(a, b)
    a_l2_norm = np.linalg.norm(a)
    b_l2_norm = np.linalg.norm(b)
    if a_l2_norm == 0 or b_l2_norm == 0:
        return 0.0
    cosine_a_b = a_dot_b/(a_l2_norm * b_l2_norm)
    return float(cosine_a_b)