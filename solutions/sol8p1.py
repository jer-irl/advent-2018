def helper(ns):
    num_children = ns[0]
    num_meta = ns[1]
    total = 0

    next_start_idx = 2
    for _ in range(num_children):
        offset, meta = helper(ns[next_start_idx:])
        next_start_idx += offset
        total += meta

    total += sum(ns[next_start_idx: next_start_idx + num_meta])

    return next_start_idx + num_meta, total


def solve(input_data):
    ns = [int(n) for n in input_data.split()]

    _, total = helper(ns)
    return total
