"""Day 10 Puzzle Solution"""

import numpy as np


def parse_data(data) -> np.ndarray:
    """Parse the data into a numpy array"""

    data = [list(x.strip()) for x in data]

    return np.array(data, dtype=int)


def find_highest_peaks_from_points(
    data, point: tuple, step_size: int = 1
) -> list[tuple]:
    """Recursively find the highest peaks from a point"""

    peaks = []

    x_coord, y_coord = point
    value_at_point = data[x_coord][y_coord]

    if value_at_point == 9:
        return [point]

    # Check neighbors horisontally and vertically
    for i in [-1, 1]:

        # Check if we walk out of bounds
        if 0 <= x_coord + i < data.shape[0]:

            if data[x_coord + i][y_coord] == value_at_point + step_size:
                peaks += find_highest_peaks_from_points(
                    data, (x_coord + i, y_coord), step_size
                )

        if 0 <= y_coord + i < data.shape[1]:

            if data[x_coord][y_coord + i] == value_at_point + step_size:
                peaks += find_highest_peaks_from_points(
                    data, (x_coord, y_coord + i), step_size
                )

    return peaks


def solution1(data):
    """Solution to part 1"""

    data = parse_data(data)
    valleys = np.where(data == 0)

    # peaks = []
    peaks_per_valley = []
    for valley_x, valley_y in zip(*valleys):

        reachable_peaks = find_highest_peaks_from_points(data, (valley_x, valley_y))
        peaks_per_valley.append(reachable_peaks)

    # Trailhead score is the number of unique peaks that can be reached per valley (trailhead)
    trailhead_score = np.sum([len(np.unique(x, axis=0)) for x in peaks_per_valley])

    return trailhead_score


def solution2(data):
    """Solution to part 2"""

    data = parse_data(data)
    valleys = np.where(data == 0)

    # peaks = []
    peaks_per_valley = []
    for valley_x, valley_y in zip(*valleys):

        reachable_peaks = find_highest_peaks_from_points(data, (valley_x, valley_y))
        # peaks += reachable_peaks
        peaks_per_valley.append(reachable_peaks)

    # Trailhead score is the number of peaks that can be reached per valley (trailhead)
    trailhead_score = np.sum([len(x) for x in peaks_per_valley])

    return trailhead_score


if __name__ == "__main__":
    # Read the input file
    with open("day-10/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
