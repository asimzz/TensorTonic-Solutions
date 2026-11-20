import numpy as np
from scipy.stats import norm

def clt_confidence_interval(data: list, confidence: float) -> list:
    """
    Returns the sample mean, standard error, and confidence-interval endpoints.
    """
    sample_data = np.array(data)
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)
    standard_error = sample_std/np.sqrt(len(sample_data))
    alpha = 1 - confidence
    critical_value = norm.ppf(1 - alpha / 2)
    lower_endpoint =  sample_mean - (critical_value * standard_error) 
    upper_endpoint =  sample_mean + (critical_value * standard_error) 
    return [sample_mean, standard_error, lower_endpoint, upper_endpoint]
    
