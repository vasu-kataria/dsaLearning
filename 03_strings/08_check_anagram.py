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
    raise NotImplementedError("TODO: solve problem 08 -- is_anagram_sorting")


def is_anagram_frequency(s1, s2):
    """Return True if s1 and s2 are anagrams -- frequency map approach."""
    raise NotImplementedError("TODO: solve problem 08 -- is_anagram_frequency")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (('listen', 'silent'), True),
    (('hello', 'world'), False),
    (('aab', 'abb'), False),
    (('abc', 'ab'), False),
    (('', ''), True),
    (('anagram', 'nagaram'), True),
]

COMPARE = None

SOLUTIONS = [is_anagram_sorting, is_anagram_frequency]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
