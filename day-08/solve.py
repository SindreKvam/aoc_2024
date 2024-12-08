"""Day 08 Puzzle Solution"""

from itertools import combinations
import logging
import numpy as np


logger = logging.getLogger(__name__)


def _parse_data(data) -> np.ndarray:

    data = [np.array(list(line.strip())) for line in data]
    data = np.array(data)

    return data


def find_all_antenna_pairs(data) -> dict:
    """Find all antennas and create a dict"""

    antennas = {}

    for x, line in enumerate(data):
        for y, value in enumerate(line):

            if value == ".":
                continue

            antennas.setdefault(value, []).append(np.array([x, y]))

    return antennas


def find_antinodes_from_antennas(antennas: dict, num_antinodes: int = 1) -> np.ndarray:
    """An antinode occurs at any point that is perfectly
    in line with two antennas of the same frequency"""
    antinodes = []

    for _, coordinates in antennas.items():

        coords = list(combinations(coordinates, r=2))

        for coord in coords:
            distances = coord[0] - coord[1]

            for i in range(1, num_antinodes + 1):
                antinodes.append(coord[0] + distances * i)
                antinodes.append(coord[1] - distances * i)

    return np.array(antinodes)


def remove_antinodes_outside_grid(antinodes: np.ndarray, grid_shape: tuple):
    """Remove all antinodes outside the grid"""

    nodes = []

    for node in antinodes:

        if not np.all(node >= np.array([0, 0])):
            continue

        if not np.all(node < np.array([grid_shape[0], grid_shape[1]])):
            continue

        nodes.append(node)

    return np.array(nodes)


def solution1(data: np.ndarray):
    """Solution to part 1"""
    logger.debug(data)

    antennas = find_all_antenna_pairs(data)
    logger.debug(antennas)

    antinodes = find_antinodes_from_antennas(antennas)

    antinodes = remove_antinodes_outside_grid(antinodes, data.shape)
    logger.debug(antinodes)

    # Remove all duplicate coordinates inside list
    antinodes = np.unique(antinodes, axis=0)

    return len(antinodes)


def solution2(data: np.ndarray):
    """Solution to part 2"""

    logger.debug(data)

    antennas = find_all_antenna_pairs(data)
    logger.debug(antennas)

    antinodes = find_antinodes_from_antennas(antennas, num_antinodes=data.shape[0])

    # Antinodes also apppear on the same point as the antenna
    for _, coordinates in antennas.items():
        antinodes = np.append(antinodes, coordinates, axis=0)

    antinodes = remove_antinodes_outside_grid(antinodes, data.shape)
    logger.debug(antinodes)

    # Remove all duplicate coordinates inside list
    antinodes = np.unique(antinodes, axis=0)

    return len(antinodes)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    # Read the input file
    with open("day-08/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    DATA = _parse_data(DATA)

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
