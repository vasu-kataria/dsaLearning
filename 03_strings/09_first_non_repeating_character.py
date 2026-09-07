"""
Problem 09 - First Non-Repeating Character
Priority 3 - Strings
Difficulty: Medium
Pattern: Two-pass frequency map

Return the first character that appears exactly once in the string.
Return None when every character repeats.

Example:
    s = "aabbcddee"   ->   "c"

Hints:
    - Pass 1: count every character. Pass 2: walk the string again in order.
    - Return the first character whose count is 1 -- the second pass is what keeps it 'first'.
    - Scanning the counts dict works too, because dicts keep insertion order in Python 3.7+.
    - O(n) time, O(k) space where k is the alphabet size.

Run this file:
    python3 03_strings/09_first_non_repeating_character.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def first_non_repeating(s):
    """Return the first character occurring exactly once, or None."""
    raise NotImplementedError("TODO: solve problem 09 -- first_non_repeating")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (('aabbcddee',), 'c'),
    (('swiss',), 'w'),
    (('x',), 'x'),
    (('aabb',), None),
    (('',), None),
]

COMPARE = None

SOLUTIONS = [first_non_repeating]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
