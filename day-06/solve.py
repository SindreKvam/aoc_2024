"""Day 06 Puzzle Solution"""

import numpy as np


def update_data_format(data):
    """Return the data in a nice format"""

    data = np.array([list(line.strip()) for line in data])

    return data


def get_start_coordinates(data: np.ndarray, start_value: str = "^"):
    """Find the coordinates of the start point"""

    start_point = np.where(data == start_value)

    return start_point


def get_obstacle_coordinates(data: np.ndarray, obstacle_value: str = "#"):
    """Find the coordinates of the obstacle values"""

    obstacle_points = np.where(data == obstacle_value)

    return obstacle_points


def solution1(data):
    """Solution to part 1"""

    distinct_positions = set()

    data = update_data_format(data)
    print(data)
    # Fetch the coordinates of all interesting points
    center_coords = get_start_coordinates(data)
    print(center_coords)
    obstacles = get_obstacle_coordinates(data)
    print(obstacles)

    # Start by adding the center coordinates
    distinct_positions.add(center_coords)

    # Move the guard in directions until it crashes into the wall.
    # In the initial position, the guard is walking upwards.

    num_distinct_positions = len(distinct_positions)
    print(distinct_positions)

    return num_distinct_positions


def solution2(data):
    """Solution to part 2"""

    return


if __name__ == "__main__":
    # Read the input file
    with open("day-06/example_input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
