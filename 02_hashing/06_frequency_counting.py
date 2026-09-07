"""
Problem 06 - Frequency Counting
Priority 2 - Hashing
Difficulty: Easy
Pattern: Frequency map

Count how many times each element appears and return a dict.

Solve it twice:
  1. with a plain dict
  2. with collections.Counter

Example:
    arr = [1, 2, 2, 3, 1, 2, 4]   ->   {1: 2, 2: 3, 3: 1, 4: 1}

Hints:
    - Plain dict: freq[x] = freq.get(x, 0) + 1.
    - collections.defaultdict(int) removes the .get() dance.
    - Counter(arr) does the whole job -- and Counter == dict compares True.
    - This map is the building block for problems 7, 8 and 9.

Run this file:
    python3 02_hashing/06_frequency_counting.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def frequency_with_dict(arr):
    """Return {element: count} using a plain dict."""
    raise NotImplementedError("TODO: solve problem 06 -- frequency_with_dict")


def frequency_with_counter(arr):
    """Return {element: count} using collections.Counter."""
    raise NotImplementedError("TODO: solve problem 06 -- frequency_with_counter")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([1, 2, 2, 3, 1, 2, 4],), {1: 2, 2: 3, 3: 1, 4: 1}),
    ((['a', 'a', 'b'],), {'a': 2, 'b': 1}),
    (([9],), {9: 1}),
    (([],), {}),
]

COMPARE = None

SOLUTIONS = [frequency_with_dict, frequency_with_counter]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
