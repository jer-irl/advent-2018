import collections


def solve(input_data):
    box_ids = input_data.split()

    num3 = 0
    num2 = 0

    for box_id in box_ids:
        letters = [l for l in box_id]
        counts = collections.Counter(letters)

        has3 = False
        has2 = False
        for _, count in counts.items():
            if count == 3:
                has3 = True
            elif count == 2:
                has2 = True
        if has3:
            num3 += 1
        if has2:
            num2 += 1

    return num3 * num2
