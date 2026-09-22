"""
Problem 08 - Check Anagram
Priority 3 - Strings
Difficulty: Easy-Medium
Pattern: Sorting / frequency map

Return True if the two strings are anagrams of each other.

Solve it twice:
  1. by sorting both strings
  2. by comparing character frequency maps

Example:
    s1 = "listen", s2 = "silent" -> True        "hello" vs "world" -> False

Hints:
    - Different lengths -> False immediately, before doing any work.
    - Sorting: sorted(s1) == sorted(s2). Simple, O(n log n).
    - Frequency: build a map for s1, decrement for s2, everything must land on 0.
    - The frequency version is O(n) -- that is the answer they want.

Run this file:
    python3 03_strings/08_check_anagram.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def is_anagram_sorting(s1, s2):
    """Return True if s1 and s2 are anagrams -- sorting approach."""
    s2_data = sorted(s2)

    s1_data = list(s1)

    for i in range(len(s1_data)):
        for j in range(i + 1, len(s1_data)):
            if s1_data[i] > s1_data[j]:
                s1_data[i], s1_data[j] = s1_data[j], s1_data[i]

    return s1_data == s2_data

    raise NotImplementedError("TODO: solve problem 08 -- is_anagram_sorting")


def is_anagram_frequency(s1, s2):
    """Return True if s1 and s2 are anagrams -- frequency map approach."""
    s1_data = {}
    for data in s1:
        s1_data[data] = s1_data.get(data, 0) + 1

    s2_data = {}
    for data in s2:
        s2_data[data] = s2_data.get(data, 0) + 1

    return s1_data == s2_data

    raise NotImplementedError("TODO: solve problem 08 -- is_anagram_frequency")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (("listen", "silent"), True),
    (("hello", "world"), False),
    (("aab", "abb"), False),
    (("abc", "ab"), False),
    (("", ""), True),
    (("anagram", "nagaram"), True),
]

COMPARE = None

SOLUTIONS = [is_anagram_sorting, is_anagram_frequency]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
