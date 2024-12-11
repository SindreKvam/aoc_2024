"""Day 11 Puzzle Solution"""

from collections import defaultdict


def parse_data(data: str) -> dict:
    """Parse the data into a dictionary"""

    stones = [int(value) for value in data.split(" ")]
    stones = {stone: stones.count(stone) for stone in stones}

    return stones


def update_stones_on_blink(stones: dict) -> list[int]:
    """Update stones on blink based on rules

    If 0 is engraved on the stone, replace by 1
    Number with even number of digits, split it in half
    If no other rule apply, multiply by 2024
    """
    new_stones = defaultdict(int)
    for stone in stones:
        number_of_equal_stones = stones[stone]

        if stone == 0:
            new_stones[1] += number_of_equal_stones

        elif len(str(stone)) % 2 == 0:
            firstpart = int(str(stone)[: len(str(stone)) // 2])
            lastpart = int(str(stone)[len(str(stone)) // 2 :])
            new_stones[firstpart] += number_of_equal_stones
            new_stones[lastpart] += number_of_equal_stones

        else:
            new_stones[int(stone * 2024)] += number_of_equal_stones

    return new_stones


def solution1(data, number_of_blinks=25):
    """Solution to part 1"""

    stones = parse_data(data)

    for _ in range(number_of_blinks):
        stones = update_stones_on_blink(stones)

    return sum(stones.values())


def solution2(data):
    """Solution to part 2"""

    return solution1(data, number_of_blinks=75)


if __name__ == "__main__":
    # Read the input file
    with open("day-11/example_input.txt", "r", encoding="utf-8") as f:
        DATA = f.readline()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
