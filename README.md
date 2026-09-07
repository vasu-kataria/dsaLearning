# dsaLearning

20 core Python DSA problems plus 8 harder array problems, one file each, with
the statement, hints and test cases already written. The solutions are yours to
fill in.

Every problem file is standalone: open it, replace the `raise NotImplementedError`
with your solution, run the file, and it tells you which cases pass.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The `.venv` is only needed for `pytest`. Individual problem files run on plain
`python3` with no dependencies at all.

## Daily loop

```bash
python3 01_array_basics/01_largest_element.py   # run one problem
pytest -q                                       # run everything solved so far
pytest -q -rs                                   # ... and list what is still pending
python3 progress.py                             # scoreboard: solved / failing / todo
```

Unsolved problems are **skipped**, not failed, so `pytest` stays green while you
work through the list.

Output of a run looks like:

```
[FAIL] second_largest  (5/6 cases)
    input:    [10, 10, 9]
    expected: 9
    got:      10
```

## Problems

### Priority 1 - Array Basics

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 1 | [Largest Element](01_array_basics/01_largest_element.py) | Easy | Linear scan | [ ] |
| 2 | [Second Largest Element](01_array_basics/02_second_largest_element.py) | Easy-Medium | Two variables / tracking maximums | [ ] |
| 3 | [Remove Duplicates](01_array_basics/03_remove_duplicates.py) | Easy | Hashing / membership check | [ ] |
| 4 | [Check if Array is Sorted](01_array_basics/04_check_if_sorted.py) | Easy | Adjacent comparison | [ ] |

### Priority 2 - Hashing

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 5 | [Two Sum](02_hashing/05_two_sum.py) | Easy-Medium | Hash map | [ ] |
| 6 | [Frequency Counting](02_hashing/06_frequency_counting.py) | Easy | Frequency map | [ ] |
| 7 | [Most Frequent Element](02_hashing/07_most_frequent_element.py) | Easy | Frequency counting | [ ] |

### Priority 3 - Strings

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 8 | [Check Anagram](03_strings/08_check_anagram.py) | Easy-Medium | Sorting / frequency map | [ ] |
| 9 | [First Non-Repeating Character](03_strings/09_first_non_repeating_character.py) | Medium | Two-pass frequency map | [ ] |
| 10 | [First Repeating Character](03_strings/10_first_repeating_character.py) | Easy | Set | [ ] |

### Priority 4 - Array Manipulation

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 11 | [Rotate Array by K Positions](04_array_manipulation/11_rotate_array_by_k.py) | Medium | Array manipulation / reversal trick | [ ] |
| 12 | [Move All Zeros to End](04_array_manipulation/12_move_zeros_to_end.py) | Easy-Medium | Two pointers | [ ] |
| 13 | [Find Missing Number](04_array_manipulation/13_find_missing_number.py) | Easy | Mathematical / XOR | [ ] |
| 14 | [Find Common Elements](04_array_manipulation/14_find_common_elements.py) | Easy | Set / hashing | [ ] |

### Priority 5 - Maximum / Minimum Patterns

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 15 | [Maximum Difference](05_max_min_patterns/15_maximum_difference.py) | Medium | Track minimum + best difference | [ ] |
| 16 | [Maximum Subarray Sum (Kadane)](05_max_min_patterns/16_maximum_subarray_sum.py) | Medium * | Kadane's Algorithm | [ ] |
| 17 | [Minimum and Maximum in One Pass](05_max_min_patterns/17_min_and_max_one_pass.py) | Easy | Single-pass tracking | [ ] |

### Priority 6 - Two Pointers

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 18 | [Two Sum in Sorted Array](06_two_pointers/18_two_sum_sorted_array.py) | Easy-Medium | Two pointers | [ ] |
| 19 | [Check Palindrome](06_two_pointers/19_check_palindrome.py) | Easy | Two pointers | [ ] |

### Priority 7 - Interview Favourites

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 20 | [Longest Substring Without Repeating Characters](07_interview_favourites/20_longest_substring_without_repeating.py) | Medium * | Sliding window + set/dict | [ ] |

### Bonus - Harder Array Problems

Do these once the core arrays feel easy -- they are the array questions that
actually get asked in interviews. Not a prerequisite for anything below them.

| # | Problem | Difficulty | Pattern | Done |
|---|---------|------------|---------|------|
| 21 | [Majority Element](08_bonus_arrays_hard/21_majority_element.py) | Medium | Boyer-Moore voting | [ ] |
| 22 | [Sort Colors (Dutch National Flag)](08_bonus_arrays_hard/22_sort_colors.py) | Medium | Three pointers / one pass | [ ] |
| 23 | [Product of Array Except Self](08_bonus_arrays_hard/23_product_except_self.py) | Medium | Prefix / suffix products | [ ] |
| 24 | [Maximum Product Subarray](08_bonus_arrays_hard/24_maximum_product_subarray.py) | Medium-Hard | Kadane variant (track min and max) | [ ] |
| 25 | [Next Permutation](08_bonus_arrays_hard/25_next_permutation.py) | Medium-Hard | Scan from the right + reverse | [ ] |
| 26 | [Merge Intervals](08_bonus_arrays_hard/26_merge_intervals.py) | Medium | Sort + sweep | [ ] |
| 27 | [Find the Duplicate Number](08_bonus_arrays_hard/27_find_the_duplicate_number.py) | Medium-Hard | Floyd's cycle detection | [ ] |
| 28 | [Trapping Rain Water](08_bonus_arrays_hard/28_trapping_rain_water.py) | Hard * | Two pointers / prefix maxima | [ ] |

Problems marked with a `*` (16, 20 and 28) are the ones that come up most often
in interviews -- do those twice.

Several problems ask for more than one approach (with/without a set, with/without
slicing, sorting vs frequency map). Each approach is a separate stub in the file
and each is tested separately, so you can solve one and come back for the other.

## Repo layout

```
checker.py     shared test runner used by every problem file
progress.py    prints how many problems are solved
tests/         pytest wrapper that collects every file's TEST_CASES
0X_*/          the problems, grouped by pattern
```

## Pushing to GitHub

```bash
git add .
git commit -m "Solve problem 01 - largest element"
git push
```

One commit per solved problem keeps the history readable as a study log.
