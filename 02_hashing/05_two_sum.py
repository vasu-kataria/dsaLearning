"""
Problem 05 - Two Sum
Priority 2 - Hashing
Difficulty: Easy-Medium
Pattern: Hash map

Given an array and a target, return the INDICES of the two numbers
that add up to the target. Return None when no pair exists.

Interview question to be ready for:
    Why is a dictionary better than nested loops?

Example:
    arr = [2, 7, 11, 15], target = 9   ->   [0, 1]   (2 + 7 = 9)

Hints:
    - One pass: for each num, ask whether target - num was already seen.
    - Store {value: index} as you go -- the lookup is O(1).
    - Nested loops are O(n^2); the dict turns it into O(n) time, O(n) memory.
    - Add the current number to the dict AFTER checking, or you may pair it with itself.

Run this file:
    python3 02_hashing/05_two_sum.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def two_sum(arr, target):
    """Return the two indices whose values sum to target, or None."""
    raise NotImplementedError("TODO: solve problem 05 -- two_sum")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([-1, 4, 2], 1), [0, 2]),
    (([1, 2, 3], 7), None),
]

COMPARE = 'sorted'

SOLUTIONS = [two_sum]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
