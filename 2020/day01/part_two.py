"""
Answer for Advent of Code challenge 2020 Day 1 Part 2.
"""

from itertools import combinations
from math import prod
from part_one import parse_input


def find_sum(values, target, n=2):
    """Find the n values in the list that sum to the target and return their product"""
    for tup in combinations(values, n):
        if sum(tup) == target:
            return prod(tup)


def solution():
    """Find the two values in the input that sum to 2020 and print their product"""
    values = parse_input('input.txt')
    answer = find_sum(values, 2020, 3)
    print(answer)

def main():
    """Execute the solution"""
    solution()

if __name__ == '__main__':
    main()
