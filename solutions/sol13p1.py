import itertools
import math


class Cart:
    intersection_turns = {
        '^': {0: '<', 1: '^', 2: '>'},
        '>': {0: '^', 1: '>', 2: 'v'},
        'v': {0: '>', 1: 'v', 2: '<'},
        '<': {0: 'v', 1: '<', 2: '^'}
    }

    forward_slash_turns = {
        '^': '>',
        '>': '^',
        'v': '<',
        '<': 'v'
    }

    back_slash_turns = {
        '^': '<',
        '>': 'v',
        'v': '>',
        '<': '^'
    }

    def __init__(self, c):
        self.c = c
        self.turn_counter = 0
        self.last_turn_moved = -math.inf

    def turn(self, track_char):
        if track_char == '|' or track_char == '-':
            return
        elif track_char == '/':
            self.c = self.forward_slash_turns[self.c]
        elif track_char == '\\':
            self.c = self.back_slash_turns[self.c]
        elif track_char == '+':
            self.c = self.intersection_turns[self.c][self.turn_counter % 3]
            self.turn_counter += 1
        else:
            raise RuntimeError("Off the track! Char: {}".format(track_char))


class CellRecord:
    def __init__(self, c):
        if c == '>' or c == '<':
            self.cart = Cart(c)
            self.track = '-'
        elif c == '^' or c == 'v':
            self.cart = Cart(c)
            self.track = '|'
        else:
            self.cart = None
            self.track = c


movement_deltas = {
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}


def state_as_str(state, highlighted_locs=[]):
    res = ""
    for y, row in enumerate(state):
        for x, col in enumerate(row):
            if (x, y) in highlighted_locs:
                res += "*"
            else:
                res += col.cart.c if col.cart is not None else col.track
        res += "\n"
    return res


def initial_state(input_data):
    state = []
    for line in input_data.split('\n'):
        row = []
        for c in line:
            row.append(CellRecord(c))
        state.append(row)
    return state


def solve(input_data):
    state = initial_state(input_data)

    for turn in itertools.count():
        for y, row in enumerate(state):
            for x, record in enumerate(row):
                if record.cart is None:
                    continue
                elif record.cart.last_turn_moved >= turn:
                    continue

                dx, dy = movement_deltas[record.cart.c]
                destination_idx = x + dx, y + dy
                destination_record = state[destination_idx[1]][destination_idx[0]]
                if destination_record.cart is not None:
                    return "{},{}".format(*destination_idx)

                # Otherwise, move the cart into the state
                destination_record.cart = record.cart
                record.cart = None
                try:
                    destination_record.cart.turn(destination_record.track)
                except Exception:
                    raise
                destination_record.cart.last_turn_moved = turn
