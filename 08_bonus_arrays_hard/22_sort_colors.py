"""
Problem 22 - Sort Colors (Dutch National Flag)
Bonus - Harder Array Problems
Difficulty: Medium
Pattern: Three pointers / one pass

The array holds only 0s, 1s and 2s. Sort it in place and return it.

Constraints: one pass, no sorted() and no counting-then-rewriting.
This is the grown-up version of 'move all zeros to end'.

Example:
    arr = [2, 0, 2, 1, 1, 0]   ->   [0, 0, 1, 1, 2, 2]

Hints:
    - Three pointers: low, mid, high. Everything before low is 0, after high is 2.
    - Walk mid: value 0 -> swap with low, advance both; value 1 -> just advance mid.
    - Value 2 -> swap with high, decrement high, and do NOT advance mid: the value
      you just swapped in is unexamined.
    - That last detail is the whole problem -- get it wrong and [2, 0, 1] breaks.

Run this file:
    python3 08_bonus_arrays_hard/22_sort_colors.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def sort_colors(arr):
    """Sort an array of 0s, 1s and 2s in one pass and return it."""
    raise NotImplementedError("TODO: solve problem 22 -- sort_colors")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([2, 0, 2, 1, 1, 0],), [0, 0, 1, 1, 2, 2]),
    (([2, 0, 1],), [0, 1, 2]),
    (([1, 0],), [0, 1]),
    (([2, 2],), [2, 2]),
    (([0],), [0]),
    (([],), []),
]

COMPARE = None

SOLUTIONS = [sort_colors]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
