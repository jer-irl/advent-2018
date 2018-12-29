def helper(ns):
    num_children = ns[0]
    num_meta = ns[1]
    total = 0
    next_start_idx = 2

    if num_children == 0:
        total += sum(ns[next_start_idx: next_start_idx + num_meta])
    else:
        child_vals = []
        for _ in range(num_children):
            offset, value = helper(ns[next_start_idx:])
            next_start_idx += offset
            child_vals.append(value)
        for meta in ns[next_start_idx: next_start_idx + num_meta]:
            if meta == 0:
                continue
            elif meta > num_children:
                continue
            else:
                total += child_vals[meta - 1]

    return next_start_idx + num_meta, total


def solve(input_data):
    ns = [int(n) for n in input_data.split()]

    _, total = helper(ns)
    return total
