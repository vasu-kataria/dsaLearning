"""
Problem 19 - Check Palindrome
Priority 6 - Two Pointers
Difficulty: Easy
Pattern: Two pointers

Return True if the string reads the same forwards and backwards.

Solve it twice:
  1. the plain way (reverse and compare)
  2. with two pointers

Example:
    s = "madam" -> True        s = "hello" -> False

Hints:
    - Plain: s == s[::-1]. Correct, but it builds a whole second string.
    - Two pointers: left at 0, right at the end, walk inward while they match.
    - Mismatch -> return False immediately; pointers crossing -> True.
    - Two pointers is O(1) extra space, which is the reason to prefer it.

Run this file:
    python3 06_two_pointers/19_check_palindrome.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def is_palindrome_simple(s):
    """Return True if s is a palindrome -- reverse-and-compare."""
    raise NotImplementedError("TODO: solve problem 19 -- is_palindrome_simple")


def is_palindrome_two_pointers(s):
    """Return True if s is a palindrome -- two pointers, no slicing."""
    raise NotImplementedError("TODO: solve problem 19 -- is_palindrome_two_pointers")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (('madam',), True),
    (('hello',), False),
    (('abba',), True),
    (('abca',), False),
    (('a',), True),
    (('',), True),
]

COMPARE = None

SOLUTIONS = [is_palindrome_simple, is_palindrome_two_pointers]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
