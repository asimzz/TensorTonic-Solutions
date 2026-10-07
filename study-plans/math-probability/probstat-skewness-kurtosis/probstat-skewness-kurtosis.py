import numpy as np

def skewness_kurtosis(data: list) -> dict:
    """
    Returns adjusted statistics and their interpretations in a dictionary.
    """
    centered = data - np.mean(data)
    n = len(data)
    s = np.std(data, ddof=1)
    s_contribution = centered / s
    signed_contribution = s_contribution ** 3
    k_contribution = s_contribution ** 4
    skewness_factor = n/((n-1)*(n-2))
    kurtosis_factor = n*(n+1)/((n-1)*(n-2)*(n-3))
    g1 = round(float(skewness_factor * np.sum(signed_contribution)), 4)
    g2 = kurtosis_factor * np.sum(k_contribution)
    g2 = round(float(g2 - 3*(n-1)**2/ ((n-2)*(n-3))), 4)
    skew_interp = "approximately symmetric"
    kurtosis_interp = "mesokurtic"
    if g1 > 0.5:
        skew_interp = "right-skewed"
    elif g1 < -0.5:
        skew_interp = "left-skewed"
    if g2 > 1:
        kurtosis_interp = "leptokurtic"
    elif g2 < -1:
        kurtosis_interp = "platykurtic"
    return {
        "skewness": g1,
        "kurtosis": g2,
        "skew_interpretation": skew_interp,
        "kurtosis_interpretation": kurtosis_interp
    }