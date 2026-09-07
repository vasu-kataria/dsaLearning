"""
Problem 28 - Trapping Rain Water
Bonus - Harder Array Problems
Difficulty: Hard *
Pattern: Two pointers / prefix maxima

Each number is the height of a bar of width 1. Return how many units of
water are trapped between the bars after rain.

The classic hard array question. Draw it on paper first -- seriously.

Example:
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]   ->   6

Hints:
    - Water above bar i = min(tallest on the left, tallest on the right) - height[i],
      floored at 0. Every solution is just a faster way to get those two maxima.
    - Version 1: precompute left_max[] and right_max[] arrays. O(n) time, O(n) space.
    - Version 2: two pointers with left_max / right_max as running scalars, always
      moving the side whose wall is shorter. O(n) time, O(1) space.
    - Why the shorter side is safe to process: its water level is already decided by
      the wall you can see -- the other side is at least that tall.
    - Try [3, 0, 2] by hand: answer 2. Then [4, 2, 0, 3, 2, 5]: answer 9.

Run this file:
    python3 08_bonus_arrays_hard/28_trapping_rain_water.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from checker import run_tests  # noqa: E402


def trap(height):
    """Return the units of rain water trapped between the bars."""
    raise NotImplementedError("TODO: solve problem 28 -- trap")



# ---------------------------------------------------------------------------
# Test cases: (arguments, expected)
# ---------------------------------------------------------------------------
TEST_CASES = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([3, 0, 2],), 2),
    (([1, 2],), 0),
    (([5],), 0),
    (([],), 0),
]

COMPARE = None

SOLUTIONS = [trap]

if __name__ == "__main__":
    run_tests(SOLUTIONS, TEST_CASES, COMPARE)
