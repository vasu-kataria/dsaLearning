"""
Problem 12 - Move All Zeros to End
Priority 4 - Array Manipulation
Difficulty: Easy-Medium
Pattern: Two pointers

Move every 0 to the end of the array and return it.

Constraint: the relative order of the non-zero elements must be preserved.

Example:
    arr = [0, 1, 0, 3, 12]   ->   [1, 3, 12, 0, 0]

Hints:
    - Two pointers: `insert_pos` marks where the next non-zero belongs.
    - Walk with a read pointer; on a non-zero, write it to insert_pos and advance it.
    - Afterwards, fill from insert_pos to the end with zeros.
    - The swap variant does it in a single pass with no fill-up step.

Run this file:
    python3 04_array_manipulation/12_move_zeros_to_end.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def move_zeros(arr):
    """Return arr with all zeros moved to the end, other values in order."""
    raise NotImplementedError("TODO: solve problem 12 -- move_zeros")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    (([0, 0, 1],), [1, 0, 0]),
    (([1, 2],), [1, 2]),
    (([0, 0],), [0, 0]),
    (([],), []),
]

COMPARE = None

SOLUTIONS = [move_zeros]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
