import numpy as np

def discrete_moments(values: list, probabilities: list) -> list:
    """
    Returns the first moment, second moment, variance, and standard deviation.
    """
    mean = sum(v * p for v ,p in zip(values ,probabilities))
    second_moment = sum(v**2 * p for v ,p in zip(values ,probabilities))
    variance = second_moment - mean ** 2
    standard_deviation = np.sqrt(variance)
    return [mean, second_moment, variance, standard_deviation]
