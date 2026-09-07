"""
Problem 02 - Second Largest Element
Priority 1 - Array Basics
Difficulty: Easy-Medium
Pattern: Two variables / tracking maximums

Return the second largest DISTINCT value in the array.
Return None when there is no such value (e.g. [2, 2, 2] or [5]).

Constraint: solve it without sorting.

Example:
    arr = [10, 5, 20, 8, 15]   ->   15

Hints:
    - Track two variables: largest and second_largest.
    - When a new value beats largest, the old largest becomes second.
    - Skip values equal to largest -- 'distinct' is what makes [10, 10, 9] -> 9.
    - Start both at None rather than 0, or negative numbers will break you.

Run this file:
    python3 01_array_basics/02_second_largest_element.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def second_largest(arr):
    first_largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]
        elif arr[i] > second_largest and first_largest != arr[i]:
            second_largest = arr[i]
    return None if second_largest == float("-inf") else second_largest


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([10, 5, 20, 8, 15],), 15),
    (([10, 10, 9],), 9),
    (([1, 2],), 1),
    (([-1, -2, -3],), -2),
    (([2, 2, 2],), None),
    (([5],), None),
]

COMPARE = None

SOLUTIONS = [second_largest]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
