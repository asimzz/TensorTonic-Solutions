import numpy as np
from scipy.stats import t

def t_test_one_sample(data: list, mu_0: float, alpha: float) -> dict:
    """
    Returns the t-statistic, degrees of freedom, p-value, and rejection decision.
    """
    n = len(data)
    degrees_of_freedom = n - 1
    data_array = np.array(data)
    x_bar = np.mean(data_array)
    s = np.std(data_array, ddof=1)
    t_statistic = (x_bar - mu_0)/(s/np.sqrt(n))
    p_value = 2 * t.sf(np.abs(t_statistic), df=degrees_of_freedom)
    return {
        "degrees_of_freedom": degrees_of_freedom,
        "p_value": p_value,
        "reject_null": p_value< alpha,
        "t_statistic": t_statistic 
    }
