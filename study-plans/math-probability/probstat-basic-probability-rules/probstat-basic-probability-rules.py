def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """
    def round_float(f: float):
        return round(float(f), 4)
    p_a_or_b = round_float(p_a + p_b - p_a_and_b)
    p_ac = round_float(1 - p_a)
    p_bc = round_float(1 - p_b)
    p_a_and_bc = round_float(p_a - p_a_and_b)
    return [p_a_or_b, p_ac, p_bc, p_a_and_bc]