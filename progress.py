"""Print how far through the 20 problems you are.

    python3 progress.py
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from checker import check, load_problem, problem_files  # noqa: E402


def main():
    done = pending = broken = 0
    current_folder = None

    for path in problem_files():
        module = load_problem(path)
        folder = os.path.basename(os.path.dirname(path))
        if folder != current_folder:
            current_folder = folder
            print(f"\n{folder}")

        compare = getattr(module, "COMPARE", None)
        statuses = [check(f, module.TEST_CASES, compare)[0] for f in module.SOLUTIONS]

        if all(s == "pending" for s in statuses):
            mark, state = "[ ]", "todo"
            pending += 1
        elif "fail" in statuses:
            mark, state = "[!]", "failing"
            broken += 1
        else:
            mark, state = "[x]", "solved"
            done += 1
        print(f"  {mark} {os.path.basename(path):<48} {state}")

    total = done + pending + broken
    print(f"\nsolved {done}/{total}   failing {broken}   todo {pending}\n")


if __name__ == "__main__":
    main()
