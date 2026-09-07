"""
Problem 25 - Next Permutation
Bonus - Harder Array Problems
Difficulty: Medium-Hard
Pattern: Scan from the right + reverse

Rearrange the array into the next lexicographically greater permutation
and return it. If no greater permutation exists (the array is in
descending order), wrap around to the smallest one -- sorted ascending.

Constraint: in place, O(1) extra space, no sorted() on the whole array.

Example:
    arr = [1, 2, 3] -> [1, 3, 2]        arr = [3, 2, 1] -> [1, 2, 3]

Hints:
    - Step 1: from the right, find the first index i where arr[i] < arr[i + 1].
      That is the 'pivot' -- everything to its right is descending.
    - Step 2: from the right, find the last index j where arr[j] > arr[i]. Swap them.
    - Step 3: reverse everything after i -- it was descending, so reversing makes it
      the smallest possible tail.
    - No pivot exists -> the array is fully descending -> just reverse the whole thing.
    - Work [1, 3, 2] through by hand before coding: pivot is 1, swap gives [2, 3, 1],
      reverse the tail gives [2, 1, 3].

Run this file:
    python3 08_bonus_arrays_hard/25_next_permutation.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def next_permutation(arr):
    """Rearrange arr into the next lexicographic permutation and return it."""
    raise NotImplementedError("TODO: solve problem 25 -- next_permutation")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 3],), [1, 3, 2]),
    (([3, 2, 1],), [1, 2, 3]),
    (([1, 1, 5],), [1, 5, 1]),
    (([1, 3, 2],), [2, 1, 3]),
    (([2, 3, 1],), [3, 1, 2]),
    (([1],), [1]),
    (([],), []),
]

COMPARE = None

SOLUTIONS = [next_permutation]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
