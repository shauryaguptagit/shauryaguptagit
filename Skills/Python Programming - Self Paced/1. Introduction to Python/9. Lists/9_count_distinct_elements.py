"""
========================================================
COUNT DISTINCT ELEMENTS IN A LIST
========================================================

Problem Statement:
------------------
Given a list of elements, determine how many
distinct (unique) elements are present in it.

Example:
--------
Input  : [10, 20, 10, 30, 30, 20]
Distinct Elements : [10, 20, 30]
Output : 3

This problem tests:
✔ Understanding of duplicates
✔ Looping and slicing
✔ Set data structure
✔ Time complexity awareness
"""

# ======================================================
# METHOD 1: USING LOOP + LIST SLICING
# ======================================================
"""
This method manually checks uniqueness.

Approach:
---------
1. Assume first element is unique → count = 1
2. Traverse list from index 1 onward
3. For each element, check if it appeared before
4. If not, increment count

Best for:
✔ Understanding core logic
✔ Theory exams
✔ Viva explanations
"""

def count_distinct_elements_loop(input_list):
    if len(input_list) == 0:
        return 0

    count = 1  # first element is always unique

    for i in range(1, len(input_list)):
        if input_list[i] not in input_list[:i]:
            count += 1

    return count


numbers = [10, 20, 10, 30, 30, 20]
print(count_distinct_elements_loop(numbers))

"""
Output:
-------
3
"""

# ------------------------------------------------------
# EXPLANATION (DRY RUN)
# ------------------------------------------------------
"""
numbers = [10, 20, 10, 30, 30, 20]

i = 1 → 20 not in [10]          → count = 2
i = 2 → 10 already in [10,20]   → count unchanged
i = 3 → 30 not in [10,20,10]    → count = 3
i = 4 → 30 already exists       → count unchanged
i = 5 → 20 already exists       → count unchanged

Final count = 3
"""


# ======================================================
# METHOD 2: USING SET (BEST & PYTHONIC)
# ======================================================
"""
This is the most efficient and recommended approach.

Why?
----
✔ Sets store only unique values
✔ Duplicate elements are removed automatically
✔ Cleaner and faster code
"""

def count_distinct_elements_set(input_list):
    return len(set(input_list))


numbers = [10, 20, 10, 30, 30, 20]
print(count_distinct_elements_set(numbers))

"""
Output:
-------
3
"""

# ------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------
"""
set(numbers) → {10, 20, 30}
len({10, 20, 30}) → 3
"""


# ======================================================
# EDGE CASES
# ======================================================
"""
1. Empty list:
   [] → 0

2. All unique elements:
   [1, 2, 3, 4] → 4

3. All duplicates:
   [5, 5, 5, 5] → 1

4. Mixed data types:
   [1, "a", 1, "a"] → 2
"""

print(count_distinct_elements_set([]))
print(count_distinct_elements_set([1, 2, 3, 4]))
print(count_distinct_elements_set([5, 5, 5]))
print(count_distinct_elements_set([1, "a", 1, "a"]))


# ======================================================
# TIME & SPACE COMPLEXITY
# ======================================================
"""
METHOD 1 (Loop + slicing):
--------------------------
Time Complexity:
O(n²) → membership check inside loop

Space Complexity:
O(1)

METHOD 2 (Set):
---------------
Time Complexity:
O(n)

Space Complexity:
O(n) → extra set used
"""


# ======================================================
# METHOD COMPARISON
# ======================================================
"""
Method                | Speed | Readability | Exam Friendly
----------------------|-------|-------------|--------------
Loop + slicing        | Slow  | Medium      | Yes
Set-based             | Fast  | Very High   | Yes (best)
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ Distinct means unique elements
✔ Sets automatically remove duplicates
✔ Use loop-based logic to understand fundamentals
✔ Prefer set() in real-world and interviews
✔ Order does not matter for counting distinct elements

Used in:
✔ Data preprocessing
✔ Removing duplicates
✔ Frequency analysis
✔ Interview questions
"""

"""
End of Count Distinct Elements Module
-------------------------------------
"""
