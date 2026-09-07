"""Tiny test runner shared by every problem file.

Each problem file defines:
    SOLUTIONS   - list of functions to test (one per approach)
    TEST_CASES  - list of (args_tuple, expected)
    COMPARE     - optional: None | "sorted" | "set"

Then calls run_tests(SOLUTIONS, TEST_CASES, COMPARE) under __main__.

A function that still raises NotImplementedError is reported as PENDING,
not as a failure -- that is how the file ships before you solve it.
"""

import copy
import importlib.util
import os


class Pending(Exception):
    """Raised internally when a solution is still a stub."""


def normalize(value, compare=None):
    """Make a result comparable, so [1, 2] == (1, 2) and order can be ignored."""
    if compare == "sorted" and isinstance(value, (list, tuple, set)):
        return sorted(value)
    if compare == "set" and isinstance(value, (list, tuple, set)):
        return set(value)
    if isinstance(value, tuple):
        return list(value)
    return value


def matches(got, expected, compare=None):
    return normalize(got, compare) == normalize(expected, compare)


def call(func, args):
    """Call func with deep-copied args so in-place solutions cannot leak state."""
    return func(*[copy.deepcopy(a) for a in args])


def check(func, cases, compare=None):
    """Run every case against func.

    Returns (status, results) where status is "pending", "pass" or "fail" and
    results is a list of (ok, args, expected, got_or_error) tuples.
    """
    results = []
    for args, expected in cases:
        try:
            got = call(func, args)
        except NotImplementedError:
            return "pending", []
        except Exception as exc:  # a crash is a failed case, not a crashed run
            results.append((False, args, expected, f"{type(exc).__name__}: {exc}"))
            continue
        results.append((matches(got, expected, compare), args, expected, got))
    status = "pass" if all(ok for ok, *_ in results) else "fail"
    return status, results


def run_tests(solutions, cases, compare=None):
    """Print a report for each solution. Returns True if nothing failed."""
    failed = False
    for func in solutions:
        name = func.__name__
        status, results = check(func, cases, compare)

        if status == "pending":
            print(f"\n... {name}: not implemented yet -- your turn")
            continue

        passed = sum(1 for ok, *_ in results if ok)
        mark = "PASS" if status == "pass" else "FAIL"
        print(f"\n[{mark}] {name}  ({passed}/{len(results)} cases)")
        for ok, args, expected, got in results:
            if ok:
                continue
            failed = True
            shown = ", ".join(repr(a) for a in args)
            print(f"    input:    {shown}")
            print(f"    expected: {expected!r}")
            print(f"    got:      {got!r}")
    print()
    return not failed



# ---------------------------------------------------------------------------
# Discovery: find and import the problem files (used by progress.py and tests/)
# ---------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.abspath(__file__))


def problem_files():
    """Yield the path of every problem file, in problem order."""
    for folder in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, folder)
        if not os.path.isdir(full) or not folder[0].isdigit():
            continue
        for name in sorted(os.listdir(full)):
            if name.endswith(".py"):
                yield os.path.join(full, name)


def load_problem(path):
    """Import a problem file by path and return the module."""
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
