"""
========================================================
CHECK IF A LIST IS SORTED OR NOT (PYTHON)
========================================================

Problem Statement:
------------------
Given a list of numbers, check whether the list is:
✔ Sorted in increasing (ascending) order
✔ Sorted in decreasing (descending) order

Examples:
---------
[1, 2, 3, 4]  → True  (sorted)
[5, 4, 3, 2]  → True  (sorted)
[3, 1, 2]     → False (not sorted)

This problem tests:
✔ Comparisons
✔ Iteration
✔ Built-in functions
✔ Logical thinking
"""

# ======================================================
# METHOD 1: USING all() FUNCTION (BEST & PYTHONIC)
# ======================================================
"""
all() returns True only if ALL conditions are True.

Logic:
------
Compare every element with the next element.
"""

# Checking ascending order
a = [1, 2, 3, 4, 5]
print(all(a[i] <= a[i + 1] for i in range(len(a) - 1)))

# Checking descending order
b = [5, 4, 3, 2, 1]
print(all(b[i] >= b[i + 1] for i in range(len(b) - 1)))

"""
Output:
-------
True
True
"""

# ------------------------------------------------------
# Explanation:
# ------------------------------------------------------
"""
For ascending:
a[i] <= a[i+1] must be True for all i

For descending:
b[i] >= b[i+1] must be True for all i

If any comparison fails → all() returns False
"""

# Note:
# Remove '=' to check strictly increasing/decreasing order


# ======================================================
# METHOD 2: USING sorted() FUNCTION
# ======================================================
"""
sorted() returns a NEW sorted list.

Logic:
------
If original list == sorted list
→ list is already sorted
"""

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(a == sorted(a))          # Ascending check
print(b == sorted(b))          # Ascending check only

"""
Output:
-------
True
False
"""

# ------------------------------------------------------
# Descending order using sorted()
# ------------------------------------------------------
print(b == sorted(b, reverse=True))

"""
Output:
-------
True
"""

# Note:
# sorted() does NOT modify the original list


# ======================================================
# METHOD 3: USING FOR LOOP (EXAM & VIVA FRIENDLY)
# ======================================================
"""
This is the most basic and easy-to-explain approach.

Logic:
------
If any element is greater than the next one,
the list is NOT sorted.
"""

a = [1, 2, 3, 4]
res = True

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        res = False
        break

print(res)

"""
Output:
-------
True
"""

# ------------------------------------------------------
# Dry Run:
# ------------------------------------------------------
"""
a = [1, 2, 3, 4]

1 <= 2 → OK
2 <= 3 → OK
3 <= 4 → OK

Loop finishes → list is sorted
"""


# ======================================================
# FUNCTION IMPLEMENTATION (REUSABLE)
# ======================================================
"""
A reusable function to check both ascending
and descending order.
"""

def is_sorted(lst):
    if len(lst) < 2:
        return True

    asc = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    desc = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    return asc or desc


print(is_sorted([1, 2, 3, 4]))
print(is_sorted([4, 3, 2, 1]))
print(is_sorted([1, 3, 2]))

"""
Output:
-------
True
True
False
"""


# ======================================================
# EDGE CASES
# ======================================================
"""
1. Empty list:
   [] → True (no elements to violate order)

2. Single element:
   [5] → True

3. All equal elements:
   [2, 2, 2] → True

4. Mixed order:
   [1, 3, 2] → False
"""


# ======================================================
# TIME & SPACE COMPLEXITY
# ======================================================
"""
Method        | Time Complexity | Space Complexity
--------------|-----------------|-----------------
all()         | O(n)            | O(1)
sorted()      | O(n log n)      | O(n)
for loop      | O(n)            | O(1)
"""


# ======================================================
# METHOD COMPARISON
# ======================================================
"""
Method        | Speed | Readability | Best Use Case
--------------|-------|-------------|----------------
all()         | Fast  | High        | Pythonic code
sorted()      | Slow  | Very High   | Quick check
for loop      | Fast  | Very High   | Exams & viva
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ Sorted list means ordered elements
✔ all() is the cleanest and fastest approach
✔ sorted() is easy but less efficient
✔ for-loop is best for understanding logic
✔ Always compare adjacent elements

Used in:
✔ Data validation
✔ Preprocessing
✔ Interview questions
✔ Algorithm optimization
"""

"""
End of Check List Sorted Module
--------------------------------
"""
