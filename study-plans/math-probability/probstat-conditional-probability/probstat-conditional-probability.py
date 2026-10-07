def conditional_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns both rounded conditional probabilities in the required order.
    """
    def round_float(f: float):
        return round(float(f), 4)
    p_a_b = round_float(p_a_and_b/p_b)
    p_b_a = round_float(p_a_and_b/p_a)
    return [p_a_b, p_b_a]