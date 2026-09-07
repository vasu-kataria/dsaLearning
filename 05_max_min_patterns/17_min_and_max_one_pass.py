"""
Problem 17 - Minimum and Maximum in One Pass
Priority 5 - Maximum / Minimum Patterns
Difficulty: Easy
Pattern: Single-pass tracking

Return (minimum, maximum) as a tuple.
Return (None, None) for an empty array.

Constraint: exactly one loop -- no calling min() and max() separately.

Example:
    arr = [5, 2, 8, 1, 9, 3]   ->   (1, 9)

Hints:
    - Seed both from arr[0], then compare each later element against both.
    - Two separate min()/max() calls means two passes -- that is what is banned.
    - Bonus: the pairwise trick compares elements two at a time to cut comparisons to ~1.5n.

Run this file:
    python3 05_max_min_patterns/17_min_and_max_one_pass.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def min_and_max(arr):
    """Return (min, max) in one pass, or (None, None) if arr is empty."""
    raise NotImplementedError("TODO: solve problem 17 -- min_and_max")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([5, 2, 8, 1, 9, 3],), (1, 9)),
    (([4],), (4, 4)),
    (([-3, -1, -7],), (-7, -1)),
    (([2, 2],), (2, 2)),
    (([],), (None, None)),
]

COMPARE = None

SOLUTIONS = [min_and_max]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
