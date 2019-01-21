def solve(input_data):
    target_recipe_start = int(input_data)

    recipes = [3, 7]
    current_idxs = [0, 1]

    for _ in range(target_recipe_start + 10):
        recipes += [int(c) for c in str(sum(recipes[idx] for idx in current_idxs))]
        current_idxs = [(idx + recipes[idx] + 1) % len(recipes) for idx in current_idxs]

    return ''.join(str(i) for i in recipes[target_recipe_start: target_recipe_start + 10])
