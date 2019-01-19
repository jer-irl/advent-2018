import math


def calc_power(serial_num, row, col):
    rack_id = col + 10
    res = rack_id * row
    res += serial_num
    res *= rack_id
    res = int(list(reversed(str(res).zfill(3)))[2])
    res -= 5
    return res


def get_grid(serial_num):
    res = []
    for i in range(300):
        row = []
        row_idx = i + 1
        for j in range(300):
            col_idx = j + 1
            row.append(calc_power(serial_num, row_idx, col_idx))
        res.append(row)

    return res


def best_cell(grid):
    best_power = -math.inf
    best_coord = None
    for row_idx in range(len(grid) - 2):
        for col_idx in range(len(grid[row_idx]) - 2):
            coord_power = 0
            for i in range(3):
                for j in range(3):
                    coord_power += grid[row_idx + i][col_idx + j]
            if coord_power > best_power:
                best_power = coord_power
                best_coord = row_idx + 1, col_idx + 1

    return best_coord


def solve(input_data):
    serial_num = int(input_data)
    grid = get_grid(serial_num)
    row, col = best_cell(grid)
    return "{},{}".format(row, col)
