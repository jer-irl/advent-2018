from solutions.sol10p1 import Star, bounding_rect_area
import itertools
import math


def solve(input_data):
    stars = [Star(line) for line in input_data.split('\n')[:-1]]

    prev_bounding_area = math.inf
    for second in itertools.count():
        new_area = bounding_rect_area(stars)
        if new_area > prev_bounding_area:
            return second - 1

        prev_bounding_area = new_area

        for star in stars:
            star.tick()
