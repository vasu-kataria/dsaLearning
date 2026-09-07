"""
Problem 11 - Rotate Array by K Positions
Priority 4 - Array Manipulation
Difficulty: Medium
Pattern: Array manipulation / reversal trick

Right-rotate the array by k positions and return the result.
k can be 0 or larger than len(arr).

Solve it twice:
  1. with Python slicing
  2. without slicing -- reversal trick or an index formula

Example:
    arr = [1, 2, 3, 4, 5], k = 2   ->   [4, 5, 1, 2, 3]

Hints:
    - Normalise first: k %= len(arr), and bail out early on an empty array.
    - Slicing: arr[-k:] + arr[:-k]  (watch out, k == 0 breaks that -- handle it).
    - Reversal trick: reverse all, reverse first k, reverse the rest. O(1) extra space.
    - Index formula alternative: result[(i + k) % n] = arr[i].

Run this file:
    python3 04_array_manipulation/11_rotate_array_by_k.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def rotate_with_slicing(arr, k):
    """Return arr right-rotated by k, using slicing."""
    raise NotImplementedError("TODO: solve problem 11 -- rotate_with_slicing")


def rotate_without_slicing(arr, k):
    """Same result, no slicing -- reverse in place or use index math."""
    raise NotImplementedError("TODO: solve problem 11 -- rotate_without_slicing")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
    (([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3]),
    (([1, 2, 3], 0), [1, 2, 3]),
    (([1, 2, 3], 3), [1, 2, 3]),
    (([1, 2, 3], 4), [3, 1, 2]),
    (([], 2), []),
]

COMPARE = None

SOLUTIONS = [rotate_with_slicing, rotate_without_slicing]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
