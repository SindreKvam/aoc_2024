"""Day 09 Puzzle Solution"""

import numpy as np
from alive_progress import alive_bar


def get_block_size_free_space(data: str):
    """Get the block size and free space from the input data"""

    file_block_size = []
    free_space = []
    for i, char in enumerate(data[0]):

        # Every other value is a block size and free space
        if i % 2 == 0:

            idn = i // 2
            file_block_size.append([idn, int(char)])

        else:
            free_space.append(int(char))

    return file_block_size, free_space


def generate_data_array(file_block_size: list, free_space: list):
    """Generate a list indicating memory space where free space is represented by '.'"""

    data_array = []
    for i, block in enumerate(file_block_size):

        # Get id and size of the block
        idn, size = block

        # Get the free space
        try:
            free = free_space[i]
        except IndexError:
            free = 0

        for _ in range(size):
            data_array.append(idn)

        for _ in range(free):
            data_array.append(".")

        # data_array += str(idn) * size + "." * free

    return data_array


def move_individual_file_blocks(data_storage: list) -> list:
    """Move the file blocks one at a time,
    from the end of the disk to the leftmost free space block"""

    updated_data_storage = []
    for _, char in enumerate(data_storage):

        if char == ".":

            # Pop the last element and check if it is a file block
            last_element = data_storage.pop()
            while last_element == ".":
                last_element = data_storage.pop()

            # Move the file block to the leftmost free space block
            updated_data_storage.append(last_element)

            # If the last element after this is still a "." remove them
            while data_storage[-1] == ".":
                data_storage.pop()

        else:
            updated_data_storage.append(char)

    return updated_data_storage


def _consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0] + 1)


def move_bulk_file_blocks(data_storage: list) -> list:
    """Move the file blocks in bulk"""

    data_array = np.array(data_storage)

    id_indexes = []
    # Remove the "." from the data array
    # Sort by int, and not by string
    unique_ids = np.unique(data_array)
    unique_ids = np.delete(unique_ids, np.where(unique_ids == "."))
    unique_ids = unique_ids.astype(int)

    for idn in np.sort(unique_ids):

        id_indexes.append(np.where(data_array == str(idn))[0])

    # Iterate backwards and move the file blocks to the leftmost free space block
    with alive_bar(len(id_indexes)) as bar:
        for i in range(len(id_indexes) - 1, -1, -1):

            id_index = id_indexes[i]

            storage_length = len(id_index)

            free_space_index = np.where(data_array == ".")[0]
            free_space_index = _consecutive(free_space_index)
            # print("ID index: ", id_index)
            # print(data_array)

            for j, free_space in enumerate(free_space_index):
                free_space_length = len(free_space)

                # print("Free space: ", free_space)

                if storage_length <= free_space_length:

                    if id_index[0] > free_space[0]:
                        data_array[free_space[:storage_length]] = data_array[id_index]
                        data_array[id_index] = "."
                        free_space_index.pop(j)

                    break
            bar()

    return data_array


def calculate_checksum(data: list) -> int:
    """Calculate the checksum of the data"""

    # Iterate and multiply index with id
    checksum = 0
    for i, char in enumerate(data):

        if char == ".":
            continue

        checksum += i * int(char)

    return checksum


def solution1(data):
    """Solution to part 1"""

    file_block_size, free_space = get_block_size_free_space(data)
    data_storage = generate_data_array(file_block_size, free_space)
    ordered_storage = move_individual_file_blocks(data_storage)

    return calculate_checksum(ordered_storage)


def solution2(data):
    """Solution to part 2"""

    file_block_size, free_space = get_block_size_free_space(data)
    data_storage = generate_data_array(file_block_size, free_space)
    ordered_storage = move_bulk_file_blocks(data_storage)

    return calculate_checksum(ordered_storage)


if __name__ == "__main__":
    # Read the input file
    with open("day-09/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
