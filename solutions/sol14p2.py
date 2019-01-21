def solve(input_data):
    target_recipe_sequence = [int(c) for c in list(input_data)]

    recipes = [3, 7]
    current_idxs = [0, 1]

    while True:
        ptr = 0
        for _ in range(100000):
            recipes += [int(c) for c in str(sum(recipes[idx] for idx in current_idxs))]
            current_idxs = [(idx + recipes[idx] + 1) % len(recipes) for idx in current_idxs]

        ptr += 100000

        for i in range(ptr - 100000, len(recipes) - len(target_recipe_sequence) + 1):
            okay = True
            for x1, x2 in zip(target_recipe_sequence, recipes[i: i + len(target_recipe_sequence)]):
                if x1 != x2:
                    okay = False
                    break
            if okay:
                return i
