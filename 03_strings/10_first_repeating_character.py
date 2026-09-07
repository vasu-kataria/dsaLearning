"""
Problem 10 - First Repeating Character
Priority 3 - Strings
Difficulty: Easy
Pattern: Set

Scanning left to right, return the first character you meet that you
have ALREADY seen earlier. Return None if every character is unique.

Careful: for "abcdeda" the answer is "d", not "a" -- "d" is where the
scan first bumps into a character it has seen before.

Example:
    s = "abcdeda"   ->   "d"

Hints:
    - Keep a `seen` set; for each char, check membership before adding it.
    - The first hit is the answer -- return straight away.
    - Contrast with problem 9: that one needs two passes, this one needs one.

Run this file:
    python3 03_strings/10_first_repeating_character.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def first_repeating(s):
    """Return the first character seen twice while scanning, or None."""
    raise NotImplementedError("TODO: solve problem 10 -- first_repeating")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (('abcdeda',), 'd'),
    (('abca',), 'a'),
    (('aa',), 'a'),
    (('abc',), None),
    (('',), None),
]

COMPARE = None

SOLUTIONS = [first_repeating]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
