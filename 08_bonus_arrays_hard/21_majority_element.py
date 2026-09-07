"""
Problem 21 - Majority Element
Bonus - Harder Array Problems
Difficulty: Medium
Pattern: Boyer-Moore voting

Return the element that appears MORE than len(arr) // 2 times.
You may assume such an element always exists.

Solve it twice:
  1. with a frequency map -- O(n) time, O(n) space
  2. with Boyer-Moore voting -- O(n) time, O(1) space

Example:
    arr = [2, 2, 1, 1, 1, 2, 2]   ->   2

Hints:
    - Voting: keep a candidate and a count. Same value -> count += 1, else count -= 1.
    - When count hits 0, adopt the current element as the new candidate.
    - Why it works: the majority element outnumbers everything else combined, so
      it survives the cancellation no matter how the array is ordered.
    - If the majority were not guaranteed, you would need a second pass to verify.

Run this file:
    python3 08_bonus_arrays_hard/21_majority_element.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def majority_element_counting(arr):
    """Return the majority element -- frequency map approach."""
    raise NotImplementedError("TODO: solve problem 21 -- majority_element_counting")


def majority_element_voting(arr):
    """Return the majority element -- Boyer-Moore voting, O(1) space."""
    raise NotImplementedError("TODO: solve problem 21 -- majority_element_voting")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([1, 1, 2, 2, 1],), 1),
    (([5, 5, 4],), 5),
    (([1],), 1),
]

COMPARE = None

SOLUTIONS = [majority_element_counting, majority_element_voting]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
