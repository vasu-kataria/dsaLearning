"""
Problem 20 - Longest Substring Without Repeating Characters
Priority 7 - Interview Favourites
Difficulty: Medium *
Pattern: Sliding window + set/dict

Return the LENGTH of the longest substring that contains no repeated
character. Substring means contiguous.

A classic. If you only drill one problem from this set, drill this one.

Example:
    s = "abcabcbb"   ->   3   ("abc")

Hints:
    - Sliding window: a `left` bound, a `right` that scans forward.
    - Set version: while s[right] is in the window set, drop s[left] and move left up.
    - Dict version: store {char: last_index} and jump left to last_index + 1 -- but
      only forward: left = max(left, last_index + 1), or old entries drag it back.
    - Test "dvdf" (answer 3) is exactly what catches that mistake.
    - Each character enters and leaves the window once -> O(n).

Run this file:
    python3 07_interview_favourites/20_longest_substring_without_repeating.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def longest_unique_substring(s):
    """Return the length of the longest substring with no repeated character."""
    raise NotImplementedError("TODO: solve problem 20 -- longest_unique_substring")


# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (('abcabcbb',), 3),
    (('bbbbb',), 1),
    (('pwwkew',), 3),
    (('dvdf',), 3),
    (('abcdef',), 6),
    (('',), 0),
]

COMPARE = None

SOLUTIONS = [longest_unique_substring]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
