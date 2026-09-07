"""
Problem 16 - Maximum Subarray Sum (Kadane)
Priority 5 - Maximum / Minimum Patterns
Difficulty: Medium *
Pattern: Kadane's Algorithm

Return the largest sum obtainable from a contiguous, non-empty subarray.
For an empty input array, return 0.

This one comes up in interviews constantly -- be able to explain it, not
just write it.

Example:
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]   ->   6   (4 + -1 + 2 + 1)

Hints:
    - Kadane: current = max(x, current + x) -- either extend the run or restart at x.
    - Keep best = max(best, current) on every step.
    - Start both at arr[0], not 0, or all-negative arrays return a wrong 0.
    - [-1, -2, -3] -> -1: the best subarray is the single least-bad element.
    - O(n) time, O(1) space.

Run this file:
    python3 05_max_min_patterns/16_maximum_subarray_sum.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def max_subarray_sum(arr):
    """Return the maximum contiguous subarray sum (0 for an empty array)."""
    raise NotImplementedError("TODO: solve problem 16 -- max_subarray_sum")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([5, 4, -1, 7, 8],), 23),
    (([-1, -2, -3],), -1),
    (([1],), 1),
    (([],), 0),
]

COMPARE = None

SOLUTIONS = [max_subarray_sum]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
