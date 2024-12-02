"""Day 2 Puzzle Solution"""

import numpy as np

if __name__ == "__main__":

    # Read the input file
    with open("day-02/input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    # Format nicely
    lines = [line.strip().split() for line in data]

    # Make all lines the same size
    max_len = max(len(line) for line in lines)
    for line in lines:
        while len(line) < max_len:
            line.extend([0] * (max_len - len(line)))

    # Convert to numpy array
    np_lines = np.array(lines, dtype=int)
    print(np_lines)

    print("--- Part 1 ---")

    # Check each line to see if it is safe
    num_safe_lines: int = 0
    safe: bool
    increasing: bool

    for line in np_lines:
        safe = True

        for i in range(len(line) - 1):

            if line[i + 1] == 0:
                continue

            diff = line[i] - line[i + 1]

            if i == 0:
                # Check if values are increasing or decreasing
                increasing = diff < 0

            if np.abs(diff) > 3 or np.abs(diff) == 0:
                safe = False

            if increasing and diff > 0:
                safe = False

            elif not increasing and diff < 0:
                safe = False

        if safe:
            num_safe_lines += 1

    print(f"Number of safe lines: {num_safe_lines}")

    print("--- Part 2 ---")

    # Check each line to see if it is safe
    # Update: one fault is acceptable
    num_safe_lines: int = 0
    safe: bool
    increasing: bool
    increase_counter: bool
    decreasing: bool

    for line in np_lines:

        safe = True

        # Remove 0 values
        line = np.array(line, dtype=int)
        line = np.delete(line, np.where(line == 0))

        # Check duplicates
        duplicates = len(line) - len(set(line))

        # We can accept one error, but multiple duplicates is guaranteed unsafe
        if duplicates > 1:
            safe = False

        # TODO: There is an edge case here somewhere.
        # For the line 44 41 44 47 51 52 57
        # We have to figure out which 44 to delete.
        # Using a set will sort the list, which we do not want
        # I have gone down a rabbit hole. I know there are much better way to do this
        # But I am now tunnel visioned and cannot see it.

        # Remove duplicate if there is exactly 1
        elif duplicates == 1:
            # Remove consecutive duplicates
            for i in range(len(line) - 1):
                diff = line[i] - line[i + 1]

                if diff == 0:
                    line = np.delete(line, i)
                    break

        else:

            total_increase = bool(line[0] - line[-1] < 0)
            total_decrease = bool(line[0] - line[-1] > 0)

            for i in range(len(line) - 1):
                # Check if there is alternating increasing and decreasing values
                diff = line[i] - line[i + 1]
                delta_decrease = bool(diff > 0)
                delta_increase = bool(diff < 0)

                if total_increase and delta_decrease:
                    line = np.delete(line, i + 1)
                    break

                elif total_decrease and delta_increase:
                    line = np.delete(line, i + 1)
                    break

        # Check if values are sorted and increasing:
        increasing = all(line[x] < line[x + 1] for x in range(len(line) - 1))
        decreasing = all(line[x] > line[x + 1] for x in range(len(line) - 1))

        # If the list is still not exclusively increasing or decreasing, it is not safe.
        if not increasing and not decreasing:
            safe = False

        for i in range(len(line) - 1):
            diff = line[i] - line[i + 1]

            if np.abs(diff) > 3:
                safe = False

        if safe:
            num_safe_lines += 1

    print(f"Number of safe lines: {num_safe_lines}")


# Code below is stolen by Independent_Check_62 on Reddit.


def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


data = [
    [int(y) for y in x.split(" ")] for x in open("day-02/input.txt").read().split("\n")
]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum(
    [any([is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))]) for row in data]
)
print(safe_count)
