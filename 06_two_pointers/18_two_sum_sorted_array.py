"""
Problem 18 - Two Sum in Sorted Array
Priority 6 - Two Pointers
Difficulty: Easy-Medium
Pattern: Two pointers

The array is already sorted. Return the two VALUES that add up to the
target (not the indices). Return None when no pair exists.

Be ready to explain why `left` and `right` move the way they do.

Example:
    arr = [1, 2, 4, 6, 8, 9, 14], target = 10   ->   [4, 6]

    Careful: 1 + 9 and 2 + 8 also make 10, so that input has three valid
    answers and a two-pointer scan actually returns [1, 9] first. The test
    cases below deliberately use targets with exactly one valid pair, so any
    correct implementation passes.

Hints:
    - left = 0, right = len(arr) - 1; look at arr[left] + arr[right].
    - Sum too small -> left += 1 (only a bigger number can help).
    - Sum too big -> right -= 1. Sortedness is what makes that safe.
    - Stop when left >= right. O(n) time, O(1) space -- beats the hash map on memory.

Run this file:
    python3 06_two_pointers/18_two_sum_sorted_array.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def two_sum_sorted(arr, target):
    """Return the two values summing to target, or None."""
    raise NotImplementedError("TODO: solve problem 18 -- two_sum_sorted")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 4, 6, 8, 9, 14], 12), [4, 8]),
    (([1, 2, 4, 6, 8, 9, 14], 23), [9, 14]),
    (([2, 3, 5, 8], 10), [2, 8]),
    (([1, 5], 6), [1, 5]),
    (([1, 2, 3], 10), None),
    (([], 5), None),
]

COMPARE = 'sorted'

SOLUTIONS = [two_sum_sorted]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
