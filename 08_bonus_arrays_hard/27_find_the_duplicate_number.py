"""
Problem 27 - Find the Duplicate Number
Bonus - Harder Array Problems
Difficulty: Medium-Hard
Pattern: Floyd's cycle detection

The array holds n + 1 integers, every value in the range 1..n, and exactly
one value is repeated (possibly many times). Return that value.

Constraints that make it interesting: do not modify the array, and use
O(1) extra space -- so no set, no sorting.

Example:
    arr = [1, 3, 4, 2, 2]   ->   2

Hints:
    - Start with the easy version (a set) so you have something working, then
      tighten it -- knowing why the easy one is rejected is the point.
    - Trick: treat the array as a linked list where i points to arr[i]. Because
      values are in 1..n, following those pointers must eventually cycle,
      and the duplicate is the entry point of that cycle.
    - Floyd: slow = arr[slow], fast = arr[arr[fast]] until they meet.
    - Then reset slow to index 0 and advance both one step at a time -- they meet
      at the duplicate.
    - This is the same algorithm as detecting a cycle in a linked list. Learn it once.

Run this file:
    python3 08_bonus_arrays_hard/27_find_the_duplicate_number.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def find_duplicate(arr):
    """Return the single repeated value in arr, without modifying it."""
    raise NotImplementedError("TODO: solve problem 27 -- find_duplicate")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 3, 4, 2, 2],), 2),
    (([3, 1, 3, 4, 2],), 3),
    (([1, 3, 2, 2],), 2),
    (([2, 2, 2, 2, 2],), 2),
    (([1, 1],), 1),
]

COMPARE = None

SOLUTIONS = [find_duplicate]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
