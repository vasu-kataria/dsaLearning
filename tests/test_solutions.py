"""Runs every problem file's own TEST_CASES through pytest.

    pytest -q            # solved problems pass, unsolved ones are skipped
    pytest -q -rs        # ... and lists what is still pending

Nothing here needs editing when you solve a problem: the suite discovers the
files, imports them, and reads their TEST_CASES / SOLUTIONS / COMPARE.
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from checker import call, load_problem, matches, problem_files  # noqa: E402


def collect():
    """Yield (test_id, function, args, expected, compare) for every case."""
    for path in problem_files():
        module = load_problem(path)
        rel = os.path.relpath(path, ROOT)
        compare = getattr(module, "COMPARE", None)
        for func in module.SOLUTIONS:
            for i, (args, expected) in enumerate(module.TEST_CASES):
                yield (f"{rel}::{func.__name__}[{i}]", func, args, expected, compare)


PARAMS = list(collect())


@pytest.mark.parametrize(
    "func,args,expected,compare",
    [(f, a, e, c) for _, f, a, e, c in PARAMS],
    ids=[i for i, *_ in PARAMS],
)
def test_case(func, args, expected, compare):
    try:
        got = call(func, args)
    except NotImplementedError:
        pytest.skip("not solved yet")
    assert matches(got, expected, compare), f"args={args!r} expected={expected!r} got={got!r}"
