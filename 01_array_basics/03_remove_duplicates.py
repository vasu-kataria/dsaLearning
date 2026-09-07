"""
Problem 03 - Remove Duplicates
Priority 1 - Array Basics
Difficulty: Easy
Pattern: Hashing / membership check

Remove duplicates from the array, keeping the FIRST occurrence order.

Solve it twice:
  1. using a set (or dict)
  2. without a set -- membership check against the result list

Example:
    arr = [1, 2, 2, 3, 4, 4, 5]   ->   [1, 2, 3, 4, 5]

Hints:
    - list(set(arr)) is NOT a correct answer: a set loses the order.
    - Set version: keep a `seen` set, append only when the value is new -- O(n).
    - No-set version: `if value not in result` -- correct but O(n^2). Know why.
    - Interview point: the set version trades O(n) memory for O(n) time.

Run this file:
    python3 01_array_basics/03_remove_duplicates.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def remove_duplicates_with_set(arr):
    """Return arr without duplicates (first-occurrence order), using a set."""
    result = []
    seen = set()
    for data in arr:
        if data not in seen:
            result.append(data)
            seen.add(data)

    return result


def remove_duplicates_without_set(arr):
    """Same result, but no set/dict allowed."""
    result = []
    for data in arr:
        if data not in result:
            result.append(data)
    return result


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 2, 3, 4, 4, 5],), [1, 2, 3, 4, 5]),
    (([3, 1, 3, 2, 1],), [3, 1, 2]),
    (([1, 1, 1],), [1]),
    (([],), []),
    ((["a", "b", "a"],), ["a", "b"]),
]

COMPARE = None

SOLUTIONS = [remove_duplicates_with_set, remove_duplicates_without_set]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
