def perms_and_combs(n: int, r: int) -> list:
    """
    Returns permutations, combinations, and n factorial as integers.
    """
    def f(n: int):
        m = 1
        for i in range(2, n+1):
            m = m * i
        return m
    N = f(n)
    n_minus_r_fact = f(n-r)
    P = N // n_minus_r_fact
    C = N // (f(r) * n_minus_r_fact)

    return [P, C, N]