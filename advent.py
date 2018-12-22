#!/usr/bin/env python3

import sys
import importlib


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("python3 advent.py [DAY#] [PART#]")
        return 1

    try:
        day = int(sys.argv[1])
        part = int(sys.argv[2])
    except ValueError:
        print("Argument must be an integer")
        return 1

    with open('inputs/input{}.txt'.format(day)) as input_file:
        input_data = input_file.read()

    try:
        sol_module = importlib.import_module("solutions.sol{}p{}".format(day, part))
    except ModuleNotFoundError:
        print("Solution module not yet created")
        return 1

    try:
        res = sol_module.solve(input_data)
    except AttributeError:
        print("Solution not yet created in module")
        return 1

    print("Calculated solution:")
    print(res)

    return 0


if __name__ == '__main__':
    sys.exit(main())
