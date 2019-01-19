from solutions.sol12p1 import simulate_generation


def solve(input_data):
    lines = input_data.split('\n')
    state = lines[0].split()[2]
    padding = '.' * 100000000000
    state = padding + state + padding
    rules = lines[2: -1]
    rules = [(rule.split()[0], rule.split()[2]) for rule in rules]

    for generation in range(50000000000):
        print(generation)
        state = simulate_generation(state, rules)

    total = 0
    for i, c in enumerate(state):
        if c == '#':
            total += i - 100000000000

    return total
