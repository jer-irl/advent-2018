from solutions.sol13p1 import initial_state, movement_deltas
import itertools


def num_carts(state):
    res = 0
    for row in state:
        for record in row:
            if record.cart is not None:
                res += 1
    return res


def last_pos(state):
    for y, row in enumerate(state):
        for x, record in enumerate(row):
            if record.cart is not None:
                return x, y


def solve(input_data):
    state = initial_state(input_data)
    carts = num_carts(state)

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

                # Crash
                if destination_record.cart is not None:
                    carts -= 2
                    destination_record.cart = None
                    record.cart = None

                # Otherwise, move the cart into the state
                else:
                    destination_record.cart = record.cart
                    record.cart = None
                    try:
                        destination_record.cart.turn(destination_record.track)
                    except Exception:
                        raise
                    destination_record.cart.last_turn_moved = turn

        if carts == 1:
            return "{},{}".format(*last_pos(state))
