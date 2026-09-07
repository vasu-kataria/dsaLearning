"""
Problem 14 - Find Common Elements
Priority 4 - Array Manipulation
Difficulty: Easy
Pattern: Set / hashing

Return the elements that appear in BOTH arrays, each one only once.
Order does not matter -- the checker sorts before comparing.

Example:
    a = [1, 2, 3, 4], b = [3, 4, 5, 6]   ->   [3, 4]

Hints:
    - set(a) & set(b) is the whole solution -- but be ready to explain the cost.
    - Manual version: put a in a set, then scan b checking membership. O(n + m).
    - Nested loops would be O(n * m) -- the set is the point of the exercise.
    - Duplicates inside one array must not produce duplicates in the output.

Run this file:
    python3 04_array_manipulation/14_find_common_elements.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def common_elements(a, b):
    """Return the unique values present in both a and b."""
    raise NotImplementedError("TODO: solve problem 14 -- common_elements")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4]),
    (([1, 1, 2], [1]), [1]),
    (([1, 2], [3]), []),
    (([], [1]), []),
]

COMPARE = 'sorted'

SOLUTIONS = [common_elements]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
