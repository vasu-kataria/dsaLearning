"""
Problem 23 - Product of Array Except Self
Bonus - Harder Array Problems
Difficulty: Medium
Pattern: Prefix / suffix products

Return an array where result[i] is the product of every element EXCEPT
arr[i].

Constraint: no division. (Ask yourself why -- what breaks when a zero is
in the array?) Aim for O(n) time.

The product of nothing is 1, so a single-element array returns [1].

Example:
    arr = [1, 2, 3, 4]   ->   [24, 12, 8, 6]

Hints:
    - result[i] = (product of everything left of i) * (product of everything right of i).
    - Pass 1 left to right filling in the prefix products.
    - Pass 2 right to left, multiplying each slot by a running suffix product.
    - Doing it with one running variable in each pass gives O(1) extra space
      (the output array does not count).
    - The zero cases are the ones that catch people: [-1, 1, 0, -3, 3].

Run this file:
    python3 08_bonus_arrays_hard/23_product_except_self.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def product_except_self(arr):
    """Return the product of all other elements for each index, no division."""
    raise NotImplementedError("TODO: solve problem 23 -- product_except_self")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 3, 4],), [24, 12, 8, 6]),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    (([2, 3],), [3, 2]),
    (([0, 0],), [0, 0]),
    (([5],), [1]),
]

COMPARE = None

SOLUTIONS = [product_except_self]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
