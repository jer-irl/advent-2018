from typing import List
import math


class Star:
    def __init__(self, line):
        self.x = int(line[10:16])
        self.y = int(line[18:24])
        self.vx = int(line[36:38])
        self.vy = int(line[40:42])

    def tick(self):
        self.x += self.vx
        self.y += self.vy

    def untick(self):
        self.x -= self.vx
        self.y -= self.vy


def bounds(stars: List[Star]):
    min_x = min(s.x for s in stars)
    max_x = max(s.x for s in stars)
    min_y = min(s.y for s in stars)
    max_y = max(s.y for s in stars)
    return min_x, max_x, min_y, max_y


def bounding_rect_area(stars: List[Star]):
    min_x, max_x, min_y, max_y = bounds(stars)
    return (max_y - min_y) * (max_x - min_x)


def stars_as_str(stars):
    min_x, max_x, min_y, max_y = bounds(stars)
    res = ""

    for row in range(min_y, max_y + 1):
        for col in range(min_x, max_x + 1):
            if any(star.x == col and star.y == row for star in stars):
                res += "#"
            else:
                res += "."
        res += "\n"

    return res


def solve(input_data):
    stars = [Star(line) for line in input_data.split('\n')[:-1]]

    prev_bounding_area = math.inf
    while True:
        for star in stars:
            star.tick()
        bounding_area = bounding_rect_area(stars)
        if bounding_area > prev_bounding_area:
            for star in stars:
                star.untick()
            break
        else:
            prev_bounding_area = bounding_area

    return stars_as_str(stars)
