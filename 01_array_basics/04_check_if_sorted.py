"""
Problem 04 - Check if Array is Sorted
Priority 1 - Array Basics
Difficulty: Easy
Pattern: Adjacent comparison

Return True if the array is sorted in non-decreasing order, else False.
Equal neighbours are fine: [1, 1, 2] is sorted.

Example:
    arr = [1, 2, 3, 4, 5] -> True        arr = [1, 3, 2, 4] -> False

Hints:
    - Compare each element with the next one: arr[i] <= arr[i + 1].
    - Return False the moment one pair is out of order -- no need to keep looping.
    - Empty arrays and single elements are sorted by definition.
    - Pythonic one-liner to compare with after: all(a <= b for a, b in zip(arr, arr[1:])).

Run this file:
    python3 01_array_basics/04_check_if_sorted.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def is_sorted(arr):
    """Return True if arr is sorted in non-decreasing order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 3, 4, 5],), True),
    (([1, 3, 2, 4],), False),
    (([1, 1, 2],), True),
    (([3, 2, 1],), False),
    (([5],), True),
    (([],), True),
]

COMPARE = None

SOLUTIONS = [is_sorted]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
