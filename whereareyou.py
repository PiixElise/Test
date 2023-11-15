def em_distance(counts_a, counts_b):
    earth = 0
    cumulative_diff = []
    diff_array = []

    for count_a, count_b in zip(counts_a, counts_b):
        diff = count_a - count_b
        diff_array.append(diff)

    for cur_diff in diff_array:
        earth = earth + cur_diff
        earth_abs = abs(earth)
        cumulative_diff.append(earth_abs)

    emd_output = sum(cumulative_diff)
    print(emd_output)