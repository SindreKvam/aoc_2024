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


def find_relevant_rules(pages: list, rules: list):
    """Find rules that contain digits found in the pages"""

    relevant_rules = []
    pages = set(pages)

    for rule in rules:

        rule_set = set(rule)
        # If the rule is a subset of the pages present (both rules apply)
        if rule_set <= pages:  # subset operator
            relevant_rules.append(rule)

    return relevant_rules


def solution1(data):
    """Solution to part 1"""

    rules = get_rules(data)
    page_numbers = get_page_numbers(data)

    middle_page_sum = 0

    for pages in page_numbers:

        relevant_rules = find_relevant_rules(pages, rules)
        valid = True

        for rule in relevant_rules:

            if np.where(pages == rule[0])[0][0] < np.where(pages == rule[1])[0][0]:
                # Valid line
                pass
            else:
                valid = False

        if valid:

            middle_page_sum += pages[len(pages) // 2]

    return middle_page_sum


def solution2(data):
    """Solution to part 2"""

    rules = get_rules(data)
    page_numbers = get_page_numbers(data)

    middle_page_sum = 0

    for pages in page_numbers:

        relevant_rules = find_relevant_rules(pages, rules)
        valid = True

        i = 0
        while i < len(relevant_rules):
            # for rule in relevant_rules:

            rule = relevant_rules[i]

            first_item = np.where(pages == rule[0])[0][0]
            last_item = np.where(pages == rule[1])[0][0]

            if first_item < last_item:
                i += 1
                continue

            valid = False

            # Last item was before expected first item
            # Move first item to the position before the last item
            # And continue until all rules are satisfied
            move_value = pages[first_item]
            pages = np.delete(pages, first_item)
            pages = np.insert(pages, last_item, move_value)
            i = 0

        # Only count the ones that originally was invalid
        if not valid:
            middle_page_sum += pages[len(pages) // 2]

    return middle_page_sum


if __name__ == "__main__":
    # Read the input file
    with open("day-05/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
