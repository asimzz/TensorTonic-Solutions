def bayes_theorem(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
    """
    Returns the posterior probability rounded to four decimals.
    """
    def round_float(f: float):
        return round(float(f), 4)

    p_not_a = 1 - p_a
    p_b = round_float(p_b_given_a * p_a + p_b_given_not_a * p_not_a)
    p_a_given_b = round_float(p_b_given_a * p_a / p_b)
    return p_a_given_b