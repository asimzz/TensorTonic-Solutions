import numpy as np

def standard_errors(samples: list) -> dict:
    """
    Returns each sample standard error and their mean.
    """
    means_sum = 0
    se = []
    for s in samples: 
        s_data = np.array(s)
        s_mean = np.mean(s_data)
        means_sum = s_mean + means_sum
        s_std = np.std(s_data, ddof=1)
        se_s = s_std/np.sqrt(len(s_data))
        se.append(se_s)
    
    mean_se = means_sum / len(samples)
    return {
        "mean_se" : np.mean(se),
        "standard_errors" : se
    }
