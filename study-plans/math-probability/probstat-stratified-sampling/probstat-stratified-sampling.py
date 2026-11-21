from math import floor, sqrt

def stratified_sample(strata_means: list, strata_stds: list, strata_sizes: list, total_sample: int) -> dict:
    """
    Returns exact allocations, the stratified mean, and its standard error.
    """
    weights = [N_h / sum(strata_sizes) for N_h in strata_sizes]
    ideal_allocs = [total_sample * W_h for W_h in weights]
    
    # 2. Floor each ideal allocation with a minimum of 1
    allocations = [max(1, floor(x)) for x in ideal_allocs]
    
    # 3. Calculate fractional remainders (0 if clamped up to 1)
    remainders = [
        (x - floor(x) if x >= 1 else 0.0, i)
        for i, x in enumerate(ideal_allocs)
    ]
    remainders.sort(key=lambda item: item[0], reverse=True)
    
    # 4. Distribute remaining slots by largest remainder
    remaining_slots = total_sample - sum(allocations)
    for k in range(remaining_slots):
        idx = remainders[k][1]
        allocations[idx] += 1
    stratified_mean = sum([W_h * mean_h for W_h, mean_h in zip(weights, strata_means)])
    stratified_se = sqrt((sum([(W_h ** 2 * std_h ** 2) / n_h for W_h, std_h, n_h in zip(weights, strata_stds, allocations)])))
    return {
        "allocations": allocations,
        "stratified_mean": stratified_mean,
        "stratified_se": stratified_se
    }