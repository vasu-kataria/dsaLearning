"""
Problem 07 - Most Frequent Element
Priority 2 - Hashing
Difficulty: Easy
Pattern: Frequency counting

Return the element that appears most often.
Return None for an empty array. (No ties in the test cases.)

Example:
    arr = [1, 2, 2, 3, 2, 4, 4]   ->   2

Hints:
    - Build the frequency map first, then take the key with the biggest value.
    - max(freq, key=freq.get) is the compact way to say that.
    - Counter(arr).most_common(1) is the library way -- know both.
    - Worth asking the interviewer: what should happen on a tie?

Run this file:
    python3 02_hashing/07_most_frequent_element.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def most_frequent(arr):
    """Return the most frequently occurring element, or None."""
    raise NotImplementedError("TODO: solve problem 07 -- most_frequent")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 2, 3, 2, 4, 4],), 2),
    (([7, 7, 7, 1, 2],), 7),
    ((['x', 'y', 'x'],), 'x'),
    (([5],), 5),
    (([],), None),
]

COMPARE = None

SOLUTIONS = [most_frequent]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
