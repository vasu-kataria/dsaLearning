"""
Problem 01 - Largest Element
Priority 1 - Array Basics
Difficulty: Easy
Pattern: Linear scan

Given an array of numbers, return the largest element.

Example:
    arr = [10, 5, 20, 8, 15]   ->   20

Hints:
    - One pass, one variable: keep the biggest value seen so far.
    - O(n) time, O(1) space. Sorting would be O(n log n) -- overkill here.
    - Decide up front what an empty array should return (here: None).

Run this file:
    python3 01_array_basics/01_largest_element.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def largest_element(arr):
    """Return the largest element of arr, or None if arr is empty."""
    largetst_num = float("-inf")
    if len(arr) == 0:
        return None
    for data in range(len(arr)):
        if arr[data] > largetst_num:
            largetst_num = arr[data]
    return largetst_num


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([10, 5, 20, 8, 15],), 20),
    (([7],), 7),
    (([-5, -2, -9],), -2),
    (([3, 3, 3],), 3),
    (([],), None),
]

COMPARE = None

SOLUTIONS = [largest_element]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
