"""
Answer for Advent of Code challenge 2020 Day 1 Part 1.
"""

from inspect import currentframe, getframeinfo
from pathlib import Path


def parse_input(input_file):
    """Parse the input file and return a list of integers"""
    filename = getframeinfo(currentframe()).filename
    parent = Path(filename).resolve().parent
    path = parent / input_file

    with path.open() as file:
        lines = file.readlines()
        return [int(line) for line in lines]


def find_sum(values, target):
    """Find the two values in the list that sum to the target and return their product"""
    for left_value in values:
        for right_value in values:
            if left_value + right_value == target:
                return left_value * right_value


def solution():
    """Find the two values in the input that sum to 2020 and print their product"""
    values = parse_input('input.txt')
    answer = find_sum(values, 2020)
    print(answer)

def main():
    """Execute the solution"""
    solution()

if __name__ == '__main__':
    main()
