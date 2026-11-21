import numpy as np

def bootstrap_ci(data: list, n_bootstraps: int, confidence: float, seed: int) -> list:
    """
    Returns the bootstrap mean and percentile confidence interval.
    """
    rng = np.random.RandomState(seed)
    boot_means = np.array(
    [ np.mean(rng.choice(data, size=len(data), replace=True))
        for _ in range(n_bootstraps)]
    )
    alpha = 1 - confidence
    lower_q = (alpha / 2) * 100
    upper_q = (1 - alpha / 2) * 100

    lower, upper = np.percentile(boot_means, [lower_q, upper_q])
    boot_mean = np.mean(boot_means)
    return [boot_mean, lower, upper]