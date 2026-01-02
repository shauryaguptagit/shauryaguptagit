"""
========================================
PYTHON LIST SLICING
========================================

Overview:
---------
List slicing is a fundamental concept in Python that allows
us to extract specific parts of a list easily and efficiently.

List slicing supports:
✔ Positive indexing
✔ Negative indexing
✔ Step / interval based access
✔ Safe out-of-bound access
✔ Reversing lists

Syntax:
-------
list_name[start : end : step]

Parameters:
-----------
start (optional) → starting index (inclusive), default = 0
end   (optional) → ending index (exclusive), default = len(list)
step  (optional) → jump between elements, default = 1
"""

# ========================================
# BASIC LIST SLICING EXAMPLE
# ========================================

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 1 to 4 (excluding 4)
print(a[1:4])

"""
Output:
-------
[2, 3, 4]
"""


# ========================================
# GET ALL ITEMS FROM A LIST
# ========================================
"""
Using [:] or [::] returns the entire list.
"""

print(a[:])
print(a[::])

"""
Output:
-------
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# ========================================
# GET ALL ITEMS AFTER / BEFORE A POSITION
# ========================================
"""
- a[start:] → from index start to end
- a[:end]   → from start to index end-1
"""

# From index 2 to end
b = a[2:]
print(b)

# From start to index 3 (excluding index 3)
c = a[:3]
print(c)

"""
Output:
-------
[3, 4, 5, 6, 7, 8, 9]
[1, 2, 3]
"""


# ========================================
# GET ITEMS BETWEEN TWO POSITIONS
# ========================================
"""
Specify both start and end.
"""

b = a[1:4]
print(b)

"""
Output:
-------
[2, 3, 4]
"""


# ========================================
# GET ITEMS AT SPECIFIED INTERVALS (STEP)
# ========================================
"""
Step controls how many elements to skip.
"""

# Every second element
b = a[::2]
print(b)

# Every third element from index 1 to 8 (excluding 8)
c = a[1:8:3]
print(c)

"""
Output:
-------
[1, 3, 5, 7, 9]
[2, 5, 8]
"""


# ========================================
# OUT-OF-BOUND SLICING
# ========================================
"""
Python slicing is safe.
Out-of-bound indices do NOT raise errors.
"""

print(a[7:15])   # indices beyond length

"""
Output:
-------
[8, 9]
"""


# ========================================
# NEGATIVE INDEXING IN LIST SLICING
# ========================================
"""
Negative indices count from the end:
-1 → last element
-2 → second last element
"""

# Last two elements
b = a[-2:]
print(b)

# All elements except last 3
c = a[:-3]
print(c)

# Elements from -4 to -1 (excluding -1)
d = a[-4:-1]
print(d)

# Every 2nd element using negative indices
e = a[-8:-1:2]
print(e)

"""
Output:
-------
[8, 9]
[1, 2, 3, 4, 5, 6]
[6, 7, 8]
[2, 4, 6, 8]
"""


# ========================================
# REVERSE A LIST USING SLICING
# ========================================
"""
Using step = -1 reverses the list.
Original list remains unchanged.
"""

b = a[::-1]
print(b)

"""
Output:
-------
[9, 8, 7, 6, 5, 4, 3, 2, 1]
"""

"""
Explanation:
------------
- start & end omitted → whole list
- step = -1 → traverse backwards
"""


# ========================================
# IMPORTANT NOTES
# ========================================
"""
1. Slicing always returns a NEW list
2. Original list remains unchanged
3. Slicing is faster and cleaner than loops
4. Negative indexing avoids length calculations
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. List slicing uses start:end:step
2. start is inclusive, end is exclusive
3. Negative indices access from end
4. Step controls skipping pattern
5. Out-of-bound slicing is safe
6. a[::-1] is the easiest way to reverse a list

List slicing is essential for:
✔ Data manipulation
✔ Algorithm design
✔ Clean Pythonic code
✔ Interviews & exams
"""

"""
End of Python List Slicing Module
---------------------------------
"""
