"""
Problem 26 - Merge Intervals
Bonus - Harder Array Problems
Difficulty: Medium
Pattern: Sort + sweep

Given a list of [start, end] intervals, merge every overlapping pair and
return the result sorted by start.

Touching counts as overlapping: [1, 4] and [4, 5] merge into [1, 5].

Example:
    [[1, 3], [2, 6], [8, 10], [15, 18]]   ->   [[1, 6], [8, 10], [15, 18]]

Hints:
    - Sort by start first -- everything else falls out of that. O(n log n).
    - Walk the sorted list keeping the last interval in the result.
    - Overlap test: current[0] <= last[1]. Then last[1] = max(last[1], current[1]).
    - The max() matters: [[1, 9], [2, 3]] must stay [1, 9], not become [1, 3].
    - Interval problems show up constantly -- calendars, bookings, rate limits.

Run this file:
    python3 08_bonus_arrays_hard/26_merge_intervals.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def merge_intervals(intervals):
    """Merge all overlapping intervals and return them sorted by start."""
    raise NotImplementedError("TODO: solve problem 26 -- merge_intervals")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[1, 9], [2, 3]],), [[1, 9]]),
    (([[5, 6], [1, 2]],), [[1, 2], [5, 6]]),
    (([[1, 2]],), [[1, 2]]),
    (([],), []),
]

COMPARE = None

SOLUTIONS = [merge_intervals]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
