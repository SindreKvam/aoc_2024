"""Day 07 Puzzle Solution"""

from dataclasses import dataclass
import itertools

import numpy as np


@dataclass
class Operators:
    """Class to store the operators"""

    ADD = 1
    MULTIPLY = 2
    CONCAT = 3


def parse_data(data):
    """Parse the data into a usable format

    Returns:
        np.array: list of test values
        np.ndarray: list of variables
    """

    test_values = np.array([line.split(":")[0] for line in data], dtype=int)

    test_variables = [line.split(":")[1].strip() for line in data]
    test_variables = [variables.split() for variables in test_variables]
    max_len = max(len(variables) for variables in test_variables)
    test_variables = [
        variables + ["0"] * (max_len - len(variables)) for variables in test_variables
    ]
    test_variables = np.array(test_variables, dtype=int)

    return test_values, test_variables


def calculate(
    expected_answer: int, variables: np.ndarray, operators: list[Operators]
) -> int:
    """Calculate the expected answer using the variables and operators

    Args:
        expected_answer (int): the expected answer
        variables (np.ndarray): the variables to use
        operators (list[Operators]): the operators to use

    Returns:
        int: The correct answer, 0 if test_values is not possible
    """

    variables = np.delete(variables, np.where(variables == 0))
    operator_permutations = [
        p for p in itertools.product(operators, repeat=len(variables) - 1)
    ]

    for operators in operator_permutations:
        answer = variables[0]

        for i, operator in enumerate(operators):

            match operator:
                case Operators.ADD:
                    answer += variables[i + 1]

                case Operators.MULTIPLY:
                    answer *= variables[i + 1]

                case Operators.CONCAT:
                    answer = int(str(answer) + str(variables[i + 1]))

                case _:
                    raise ValueError(f"Invalid operator: {operator}")

        if answer == expected_answer:
            return answer

    return 0


def solution1(data):
    """Solution to part 1"""

    test_values, test_variables = parse_data(data)

    total_sum = 0
    for i, test_value in enumerate(test_values):
        total_sum += calculate(
            test_value, test_variables[i], [Operators.ADD, Operators.MULTIPLY]
        )

    return total_sum


def solution2(data):
    """Solution to part 2"""

    test_values, test_variables = parse_data(data)

    total_sum = 0
    for i, test_value in enumerate(test_values):
        total_sum += calculate(
            test_value,
            test_variables[i],
            [Operators.ADD, Operators.MULTIPLY, Operators.CONCAT],
        )

    return total_sum


if __name__ == "__main__":
    # Read the input file
    with open("day-07/input.txt", "r", encoding="utf-8") as f:
        DATA = f.readlines()

    answ1 = solution1(DATA)
    print(f"Solution 1: {answ1}")

    answ2 = solution2(DATA)
    print(f"Solution 2: {answ2}")
