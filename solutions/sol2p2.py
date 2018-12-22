import itertools


def num_different_chars(id1, id2):
    return sum(1 if a != b else 0 for a, b in zip(id1, id2))


def shared_chars(id1, id2):
    return ''.join(a for a, b in zip(id1, id2) if a == b)


def solve(input_data):
    box_ids = input_data.split()
    for id1, id2 in itertools.combinations(box_ids, 2):
        if num_different_chars(id1, id2) == 1:
            return shared_chars(id1, id2)

    raise Exception("Pair not found")
