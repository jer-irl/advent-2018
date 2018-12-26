def same_type_opposite_polarity(c1: str, c2: str) -> bool:
    if c1.lower() != c2.lower():
        return False
    elif (c1.isupper() and c2.isupper()) or (c1.islower() and c2.islower()):
        return False
    return True


def solve(input_data):
    input_data = input_data.strip()

    polymer = input_data
    i = 0
    while i < len(polymer) - 1:
        c1, c2 = polymer[i], polymer[i + 1]
        if same_type_opposite_polarity(c1, c2):
            polymer = polymer[:i] + polymer[i + 2:]
            i = i if i == 0 else i - 1
        else:
            i += 1

    return len(polymer)
