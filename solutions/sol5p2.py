from solutions.sol5p1 import same_type_opposite_polarity


def solve(input_data):
    input_data = input_data.strip()

    chars = set(list(input_data.lower()))

    results = {}
    for char in chars:
        polymer = ''.join([c for c in input_data if c.lower() != char])
        i = 0
        while i < len(polymer) - 1:
            c1, c2 = polymer[i], polymer[i + 1]
            if same_type_opposite_polarity(c1, c2):
                polymer = polymer[:i] + polymer[i + 2:]
                i = i if i == 0 else i - 1
            else:
                i += 1
        results[char] = len(polymer)

    return min(results.values())
