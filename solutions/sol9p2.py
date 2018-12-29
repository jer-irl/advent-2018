from solutions.sol9p1 import solution


def solve(input_data):
    num_players = int(input_data.split()[0])
    max_marble_score = int(input_data.split()[6])
    return solution(num_players, 100 * max_marble_score)
