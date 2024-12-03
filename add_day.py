"""Script to generate new day-xx folder and filling it with the basic files needed."""

import os


def get_python_file_content(day):
    """Return python file content"""

    return f"""\"\"\"Day {day} Puzzle Solution\"\"\"

import numpy as np


def solution1(data):
    \"\"\"Solution to part 1\"\"\"


def solution2(data):
    \"\"\"Solution to part 2\"\"\"
    

if __name__ == "__main__":
    # Read the input file
    with open("day-02/input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    answ1 = solution1(data)

    answ2 = solution2(data)
"""


if __name__ == "__main__":

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    subdirectories = next(os.walk(THIS_FOLDER))[1]

    day_counts = 0
    for folder in subdirectories:

        if "day" in folder:
            day_counts += 1

    day = str(day_counts + 1).zfill(2)

    new_foldername = f"day-{day}"
    os.mkdir(new_foldername)

    with open(f"{new_foldername}/solve.py", "w", encoding="utf-8") as f:
        f.writelines(get_python_file_content(day=day))

    with open(f"{new_foldername}/input.txt", "w", encoding="utf-8") as f:
        f.write("")

    with open(f"{new_foldername}/example_input.txt", "w", encoding="utf-8") as f:
        f.write("")
