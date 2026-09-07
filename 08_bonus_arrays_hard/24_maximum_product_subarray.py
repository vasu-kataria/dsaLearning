"""
Problem 24 - Maximum Product Subarray
Bonus - Harder Array Problems
Difficulty: Medium-Hard
Pattern: Kadane variant (track min and max)

Return the largest product obtainable from a contiguous, non-empty
subarray. Return 0 for an empty array.

Looks like problem 16, behaves nothing like it.

Example:
    arr = [2, 3, -2, 4]   ->   6   (2 * 3)

Hints:
    - Plain Kadane fails here: a negative number turns the SMALLEST product into
      the largest the moment you multiply by another negative.
    - So track both: max_so_far and min_so_far, and swap them when x < 0.
    - max_so_far = max(x, max_so_far * x, min_so_far * x) -- same for the min.
    - [-2, 3, -4] -> 24 is the case that proves you need the min.
    - Zeros reset both running products to start fresh at the next element.

Run this file:
    python3 08_bonus_arrays_hard/24_maximum_product_subarray.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def max_product_subarray(arr):
    """Return the maximum contiguous subarray product (0 for an empty array)."""
    raise NotImplementedError("TODO: solve problem 24 -- max_product_subarray")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([2, 3, -2, 4],), 6),
    (([-2, 3, -4],), 24),
    (([-2, 0, -1],), 0),
    (([0, 2],), 2),
    (([-2],), -2),
    (([],), 0),
]

COMPARE = None

SOLUTIONS = [max_product_subarray]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
