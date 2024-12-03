"""Day 03 Puzzle Solution"""

import re

import numpy as np


def solution1(data: str):
    """Solution to part 1"""

    non_corrupt_commands = re.findall(r"mul\((\d*),(\d*)\)", data)

    return np.sum([int(x[0]) * int(x[1]) for x in non_corrupt_commands])


def solution2(data: str):
    """Solution to part 2"""

    do_data = data.split("do()")

    # There has just been a do(),
    # remove everything after don't() that are introduced
    do_data = [line.split("don't()")[0] for line in do_data]

    return solution1(str(do_data))


if __name__ == "__main__":
    # Read the input file
    with open("day-03/input.txt", "r", encoding="utf-8") as f:
        DATA = str(f.readlines())

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
