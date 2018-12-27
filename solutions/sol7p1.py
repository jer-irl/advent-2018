def steps_ready(blocked_count):
    return [blockee for blockee in blocked_count.keys() if blocked_count[blockee] == 0]


def solve(input_data):
    pairs = [(toks[1], toks[7]) for toks in [line.split() for line in input_data.split('\n')[:-1]]]
    letters = set([pair[0] for pair in pairs]).union(set(pair[1] for pair in pairs))

    # The steps each step key is blocking
    steps_blocked = {}
    for letter in letters:
        steps_blocked[letter] = []
    for blocker, blockee in pairs:
        steps_blocked[blocker].append(blockee)

    # The count of steps blocking the key, or None if step is not already completed
    blocked_count = {}
    for letter in letters:
        blocked_count[letter] = 0
    for _, blockee in pairs:
        blocked_count[blockee] += 1

    res = ""
    while len(steps_ready(blocked_count)) > 0:
        ready_steps = steps_ready(blocked_count)
        next_step = sorted(ready_steps)[0]
        res += next_step
        blocked_count[next_step] = None
        for blockee in steps_blocked[next_step]:
            blocked_count[blockee] -= 1

    return res
