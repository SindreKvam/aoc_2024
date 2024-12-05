"""Day 05 Puzzle Solution"""

import re
import numpy as np


def get_rules(data):
    """Get the rules from the input data"""

    data = "".join(data)
    rules = re.findall(r"(\d+)\|(\d+)", data)
    rules = [(int(rule[0]), int(rule[1])) for rule in rules]

    return rules


def get_page_numbers(data):
    """Get the page numbers from the input data"""

    page_numbers = []
    for line in data:
        if "," not in line:
            continue

        page_numbers.append(line.strip().split(","))

    page_numbers = [np.array(page_number, dtype=int) for page_number in page_numbers]

    return page_numbers


def solution1(data):
    """Solution to part 1"""

    rules = get_rules(data)
    page_numbers = get_page_numbers(data)

    print(rules)
    for pages in page_numbers:
        print(pages)

    return


def solution2(data):
    """Solution to part 2"""

    return


if __name__ == "__main__":
    # Read the input file
    with open("day-05/example_input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
