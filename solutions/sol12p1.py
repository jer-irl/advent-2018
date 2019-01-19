def simulate_generation(state, rules):
    res = list(state)
    for i in range(len(state) - 5):
        matching_rule = [rule for rule in rules if rule[0] == state[i: i + 5]][0]
        res[i + 2] = matching_rule[1]

    return ''.join(res)


def solve(input_data):
    lines = input_data.split('\n')
    state = lines[0].split()[2]
    padding = '.' * 40
    state = padding + state + padding
    rules = lines[2: -1]
    rules = [(rule.split()[0], rule.split()[2]) for rule in rules]

    for generation in range(20):
        state = simulate_generation(state, rules)

    total = 0
    for i, c in enumerate(state):
        if c == '#':
            total += i - 40

    return total
