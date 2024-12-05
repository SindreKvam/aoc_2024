"""Day 04 Puzzle Solution"""

import numpy as np


def _diagonal_matrix_to_string(data):
    return "".join([str(data[i][i]) for i in range(len(data))])


def _get_diagonal_words(data: list):
    """Get all the values that are on the diagonal
    This function expects square matrix input"""

    data_arr = [list(line) for line in data]
    data_arr_reverse = np.array([row[::-1] for row in data_arr])

    data_arr = np.array(data_arr)

    diagonal_words = []
    # Along identity matrix diagonal
    diagonal_words.append(_diagonal_matrix_to_string(data_arr))
    # Along reverse identity matrix diagonal
    diagonal_words.append(_diagonal_matrix_to_string(data_arr_reverse))

    for i in range(1, len(data_arr)):

        small_data_arr1 = data_arr[:-i, i:]
        small_data_arr_reverse1 = data_arr_reverse[:-i, i:]
        small_data_arr2 = data_arr[i:, :-i]
        small_data_arr_reverse2 = data_arr_reverse[i:, :-i]

        diagonal_words.append(_diagonal_matrix_to_string(small_data_arr1))
        diagonal_words.append(_diagonal_matrix_to_string(small_data_arr_reverse1))
        diagonal_words.append(_diagonal_matrix_to_string(small_data_arr2))
        diagonal_words.append(_diagonal_matrix_to_string(small_data_arr_reverse2))

    return diagonal_words


def find_diagonal_words(word: str, data: list):
    """Find all diagonal occurrences of the word"""

    diagonal_words = _get_diagonal_words(data)

    return find_horizontal_word(word, diagonal_words)


def rotate_data(data: np.array) -> list:
    """Rotate the data matrix"""

    new_data = np.array([list(line) for line in data])
    rotated_data = new_data.transpose()

    return ["".join(line) for line in rotated_data]


def find_horizontal_word(word: str, data: list):
    """Find all horizontal occurrences of the word"""

    num_occurrences = 0

    for line in data:
        num_occurrences += line.count(word)
        num_occurrences += line.count(word[::-1])

    return num_occurrences


def find_vertical_word(word: str, data: list):
    """Find all vertical occurrences of the word"""

    rotated_data = rotate_data(data)

    return find_horizontal_word(word, rotated_data)


def solution1(data, word: str = "XMAS"):
    """Solution to part 1"""

    num_occurrences = 0
    num_occurrences += find_horizontal_word(word, data)
    num_occurrences += find_vertical_word(word, data)
    num_occurrences += find_diagonal_words(word, data)

    return num_occurrences


def find_cross_words(word: str, data: list):
    """Get all the values that are on the diagonal
    This function expects square matrix input"""

    center_letter_distance = len(word) // 2
    center_letter = word[center_letter_distance]

    center_pos = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):

            if data[i][j] == center_letter:
                center_pos.append((i, j))

    num_occurrences = 0
    for pos in center_pos:
        top_left = (pos[0] - center_letter_distance, pos[1] - center_letter_distance)
        top_right = (pos[0] - center_letter_distance, pos[1] + center_letter_distance)
        bottom_left = (pos[0] + center_letter_distance, pos[1] - center_letter_distance)
        bottom_right = (
            pos[0] + center_letter_distance,
            pos[1] + center_letter_distance,
        )

        if (
            (
                (data[top_left[0]][top_left[1]] in (word[-1]))
                and (data[bottom_right[0]][bottom_right[1]] in (word[0]))
            )
            or (
                (data[top_left[0]][top_left[1]] in (word[0]))
                and (data[bottom_right[0]][bottom_right[1]] in (word[-1]))
            )
        ) and (
            (
                (data[top_right[0]][top_right[1]] in (word[-1]))
                and (data[bottom_left[0]][bottom_left[1]] in (word[0]))
            )
            or (
                (data[top_right[0]][top_right[1]] in (word[0]))
                and (data[bottom_left[0]][bottom_left[1]] in (word[-1]))
            )
        ):
            num_occurrences += 1

    return num_occurrences


def solution2(data):
    """Solution to part 2"""

    count = find_cross_words("MAS", data)

    return count


if __name__ == "__main__":
    # Read the input file
    with open("day-04/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    DATA = [line.strip() for line in DATA]
    DATA = np.array(DATA)

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
