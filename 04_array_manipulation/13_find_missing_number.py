"""
Problem 13 - Find Missing Number
Priority 4 - Array Manipulation
Difficulty: Easy
Pattern: Mathematical / XOR

The array holds the numbers 1..n with exactly one missing, in any order,
so n == len(arr) + 1. Return the missing number.

Solve it twice:
  1. with the sum formula
  2. with XOR

Example:
    arr = [1, 2, 4, 5, 6]   (numbers 1..6)   ->   3

Hints:
    - Sum formula: expected = n * (n + 1) // 2, answer = expected - sum(arr).
    - XOR: a ^ a == 0, so XOR-ing 1..n together with every element cancels all pairs.
    - XOR avoids the integer-overflow worry that the sum trick has in C++/Java.
    - Both are O(n) time and O(1) space -- no sorting, no set.

Run this file:
    python3 04_array_manipulation/13_find_missing_number.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def missing_number_sum(arr):
    """Return the missing number from 1..len(arr)+1 -- sum formula."""
    raise NotImplementedError("TODO: solve problem 13 -- missing_number_sum")


def missing_number_xor(arr):
    """Same answer, using XOR."""
    raise NotImplementedError("TODO: solve problem 13 -- missing_number_xor")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 4, 5, 6],), 3),
    (([2, 3, 4],), 1),
    (([1, 2, 3],), 4),
    (([2],), 1),
    (([1],), 2),
]

COMPARE = None

SOLUTIONS = [missing_number_sum, missing_number_xor]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
