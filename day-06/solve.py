"""Day 06 Puzzle Solution"""

import logging
import numpy as np
from alive_progress import alive_bar

logger = logging.getLogger(__name__)


grid_size = (0, 0)


def update_data_format(data):
    """Return the data in a nice format"""

    data = np.array([list(line.strip()) for line in data])
    global grid_size
    grid_size = data.shape

    return data


def get_start_coordinates(data: np.ndarray, start_value: str = "^") -> tuple:
    """Find the coordinates of the start point"""

    x_coord, y_coord = np.where(data == start_value)

    start_point = (int(x_coord[0]), int(y_coord[0]))

    return start_point


def get_obstacle_coordinates(data: np.ndarray, obstacle_value: str = "#") -> tuple:
    """Find the coordinates of the obstacle values"""

    x_coords, y_coords = np.where(data == obstacle_value)

    obstacle_points = [(int(x), int(y)) for x, y in zip(x_coords, y_coords)]

    return obstacle_points


def move_north(current_position: tuple, obstacles: tuple) -> tuple:
    """Move the guard north until it crashes into an obstacle

    Returns:
        tuple: The new position of the guard
        tuple: The points touched by the guard
    """

    # north is to decrease the x-coordinate
    relevant_obstacles = [
        obstacle
        for obstacle in obstacles
        if obstacle[0] < current_position[0] and obstacle[1] == current_position[1]
    ]

    logger.debug("relevant obstacles : %s", relevant_obstacles)

    if len(relevant_obstacles) != 0:
        # Fetch the one that is closest to the guard
        closest_obstacle = min(
            relevant_obstacles, key=lambda coord: np.abs(coord[0] - current_position[0])
        )
        logger.debug("closest obstacle : %s", closest_obstacle)

        new_position = (closest_obstacle[0] + 1, current_position[1])

    else:
        # Move to the end of the grid if there is no obstacle
        new_position = (0, current_position[1])

    points_touched = [
        (x, current_position[1])
        for x in range(new_position[0], current_position[0] + 1)
    ]

    logger.debug("points touched : %s", points_touched)
    logger.debug("new position : %s ", new_position)

    return new_position, points_touched


def move_south(current_position: tuple, obstacles: tuple) -> tuple:
    """Move the guard south until it crashes into an obstacle

    Returns:
        tuple: The new position of the guard
        tuple: The points touched by the guard
    """

    # south is to increase the x-coordinate
    relevant_obstacles = [
        obstacle
        for obstacle in obstacles
        if obstacle[0] > current_position[0] and obstacle[1] == current_position[1]
    ]

    logger.debug("relevant obstacles : %s", relevant_obstacles)

    if len(relevant_obstacles) != 0:
        # Fetch the one that is closest to the guard
        closest_obstacle = min(
            relevant_obstacles, key=lambda coord: np.abs(coord[0] - current_position[0])
        )
        logger.debug("closest obstacle : %s", closest_obstacle)

        new_position = (closest_obstacle[0] - 1, current_position[1])
    else:
        # Move to the end of the grid if there is no obstacle
        new_position = (grid_size[0] - 1, current_position[1])

    points_touched = [
        (x, current_position[1])
        for x in range(current_position[0], new_position[0] + 1)
    ]

    logger.debug("points touched : %s", points_touched)
    logger.debug("new position : %s ", new_position)

    return new_position, points_touched


def move_east(current_position: tuple, obstacles: tuple) -> tuple:
    """Move the guard east until it crashes into an obstacle

    Returns:
        tuple: The new position of the guard
        tuple: The points touched by the guard
    """

    # east is to increase the y-coordinate
    relevant_obstacles = [
        obstacle
        for obstacle in obstacles
        if obstacle[0] == current_position[0] and obstacle[1] > current_position[1]
    ]

    logger.debug("relevant obstacles : %s", relevant_obstacles)

    if len(relevant_obstacles) != 0:
        # Fetch the one that is closest to the guard
        closest_obstacle = min(
            relevant_obstacles, key=lambda coord: np.abs(coord[1] - current_position[1])
        )
        logger.debug("closest obstacle : %s", closest_obstacle)

        new_position = (current_position[0], closest_obstacle[1] - 1)

    else:
        # Move to the end of the grid if there is no obstacle
        new_position = (current_position[0], grid_size[1] - 1)

    points_touched = [
        (current_position[0], y)
        for y in range(current_position[1], new_position[1] + 1)
    ]

    logger.debug("points touched : %s", points_touched)
    logger.debug("new position : %s ", new_position)

    return new_position, points_touched


def move_west(current_position: tuple, obstacles: tuple) -> tuple:
    """Move the guard west until it crashes into an obstacle

    Returns:
        tuple: The new position of the guard
        tuple: The points touched by the guard
    """

    # west is to decrease the y-coordinate
    relevant_obstacles = [
        obstacle
        for obstacle in obstacles
        if obstacle[0] == current_position[0] and obstacle[1] < current_position[1]
    ]

    logger.debug("relevant obstacles : %s", relevant_obstacles)

    if len(relevant_obstacles) != 0:
        # Fetch the one that is closest to the guard
        closest_obstacle = min(
            relevant_obstacles, key=lambda x: np.abs(x[1] - current_position[1] + 1)
        )
        logger.debug("closest obstacle : %s", closest_obstacle)

        new_position = (current_position[0], closest_obstacle[1] + 1)
    else:
        # Move to the end of the grid if there is no obstacle
        new_position = (current_position[0], 0)

    points_touched = [
        (current_position[0], y) for y in range(new_position[1], current_position[1])
    ]

    logger.debug("points touched : %s", points_touched)
    logger.debug("new position : %s ", new_position)

    return new_position, points_touched


def solution1(data):
    """Solution to part 1"""

    distinct_positions = set()

    data = update_data_format(data)
    logger.info("Map :\n %s", data)
    # Fetch the coordinates of all interesting points
    guard_coordinates = get_start_coordinates(data)
    obstacles = get_obstacle_coordinates(data)

    # Start by adding the center coordinates
    distinct_positions.add(guard_coordinates)

    # Move the guard in directions until it crashes into the wall.
    # In the initial position, the guard is walking upwards.

    stop = False
    while stop is False:

        for func in [move_north, move_east, move_south, move_west]:

            logger.debug("Function : %s", func.__name__)
            logger.debug("Guard coordinates : %s", guard_coordinates)
            guard_coordinates, points_touched = func(guard_coordinates, obstacles)
            distinct_positions.update(points_touched)

            # if guard has reached the end of the grid
            if (guard_coordinates[0] in [0, grid_size[0] - 1]) or (
                guard_coordinates[1] in [0, grid_size[0] - 1]
            ):
                stop = True
                break

    num_distinct_positions = len(distinct_positions)
    logger.debug("Distinct positions : %s", distinct_positions)

    data2 = data.copy()
    for x, y in distinct_positions:
        data2[x, y] = "X"

    logger.info("Map with distinct positions :\n %s", data2)

    return num_distinct_positions


def solution2(data):
    """Solution to part 2"""

    data = update_data_format(data)
    # Fetch the coordinates of all interesting points
    initial_guard_coordinates = get_start_coordinates(data)
    initial_obstacles = get_obstacle_coordinates(data)

    number_of_times_stuck = 0
    with alive_bar(grid_size[0]) as bar:
        for x, row in enumerate(data):
            for y, _ in enumerate(row):

                if (x, y) == initial_guard_coordinates:
                    continue

                if (x, y) in initial_obstacles:
                    continue

                guard_coordinates = initial_guard_coordinates[:]
                obstacles = initial_obstacles[:]

                obstacles = list(obstacles)
                obstacles.append((x, y))
                obstacles = tuple(obstacles)

                stop = False
                guard_stops = []
                while stop is False:

                    for func in [move_north, move_east, move_south, move_west]:

                        logger.debug("Function : %s", func.__name__)
                        logger.debug("Guard coordinates : %s", guard_coordinates)
                        guard_coordinates, points_touched = func(
                            guard_coordinates, obstacles
                        )

                        if guard_coordinates in guard_stops and len(points_touched) > 1:
                            # Guard is stuck in a loop
                            stop = True
                            number_of_times_stuck += 1
                            break

                        guard_stops.append(guard_coordinates)

                        # if guard has reached the end of the grid
                        if (guard_coordinates[0] in [0, grid_size[0] - 1]) or (
                            guard_coordinates[1] in [0, grid_size[0] - 1]
                        ):
                            stop = True
                            break
            bar()

    return number_of_times_stuck


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    # Read the input file
    with open("day-06/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    logger.info("------ Solution 1 ------")

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    logger.info("------ Solution 2 ------")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
