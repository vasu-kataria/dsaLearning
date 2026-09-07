"""
Problem 15 - Maximum Difference
Priority 5 - Maximum / Minimum Patterns
Difficulty: Medium
Pattern: Track minimum + best difference

Find the maximum value of arr[j] - arr[i] where j > i.
If no such positive difference exists, return 0.

This is the 'best time to buy and sell stock' problem in disguise.

Example:
    arr = [7, 1, 5, 3, 6, 4]   ->   5   (6 - 1)

Hints:
    - One pass: track the smallest value seen so far (the best 'buy').
    - At each element, the candidate profit is current - min_so_far.
    - Update min_so_far AFTER computing the candidate, so j > i stays true.
    - [7, 6, 4, 3, 1] is strictly decreasing -> answer 0, not a negative number.

Run this file:
    python3 05_max_min_patterns/15_maximum_difference.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def max_difference(arr):
    """Return max arr[j] - arr[i] for j > i, or 0 if none is positive."""
    raise NotImplementedError("TODO: solve problem 15 -- max_difference")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([1, 2],), 1),
    (([2, 4, 1, 9],), 8),
    (([2],), 0),
    (([],), 0),
]

COMPARE = None

SOLUTIONS = [max_difference]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
