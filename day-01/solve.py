
"""Day 1 Puzzle Solution"""

import numpy as np


if __name__ == "__main__":

    # Read input data
    with open("day-01/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        len_lines = len(lines)
        
    # Format nicely
    lines = [line.strip().split() for line in lines]
    np_lines = np.array(lines, dtype=int)

    print("--- Part 1 ---")

    print(np_lines.T)
    for i, val in enumerate(np_lines.T):
        # Sort list and put them back into the transposed list
        np_lines.T[i] = np.sort(val)

    print(np_lines)
    distances = np.abs(np_lines.T[0] - np_lines.T[1])

    print(np.sum(distances))

    print("--- Part 2 ---")

    # Find similarity scores
    print(np_lines.T.shape)
    
    # Add extra column to store the similarity scores
    np_lines = np.append(np_lines, np.zeros((len_lines, 1), dtype=int), axis=1)

    # Iterate through all values in the left column
    for i, val in enumerate(np_lines.T[0]):

        common_counter = 0
        for j, val2 in enumerate(np_lines.T[1]):
            # Compute similarity score

            if val == val2:
                common_counter += 1
        
        # Similarity score -> times the value occurs in the second column
        np_lines.T[2, i] = common_counter * val

    print(np.sum(np_lines.T[2]))
