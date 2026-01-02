"""
========================================
TUPLE SLICING IN PYTHON
========================================

Overview:
---------
A tuple is an immutable, ordered sequence used to store
a collection of heterogeneous data.

Key Characteristics of Tuples:
------------------------------
✔ Ordered
✔ Immutable (cannot be modified after creation)
✔ Allows duplicate elements
✔ Supports indexing and slicing
✔ Faster and safer than lists in some cases

Tuple slicing allows us to extract a portion of a tuple
and create a NEW tuple from it.
"""

# ========================================
# WHAT IS TUPLE SLICING?
# ========================================
"""
Tuple slicing extracts a sub-part of a tuple using
a range of indices.

Important:
----------
✔ Slicing NEVER modifies the original tuple
✔ It always returns a NEW tuple
"""

# ========================================
# BASIC TUPLE SLICING EXAMPLES
# ========================================

# Define a tuple
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice from index 2 to 5 (excluding 6)
s1 = tup[2:6]
print(s1)

# Slice from beginning to index 3 (excluding 4)
s2 = tup[:4]
print(s2)

# Slice from index 5 to end
s3 = tup[5:]
print(s3)

# Slice the entire tuple
s4 = tup[:]
print(s4)

"""
Output:
-------
(2, 3, 4, 5)
(0, 1, 2, 3)
(5, 6, 7, 8, 9)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
"""


# ========================================
# TUPLE SLICING SYNTAX
# ========================================
"""
Syntax:
-------
tuple[start : stop : step]

Parameters:
-----------
start → starting index (inclusive), default = 0
stop  → ending index (exclusive)
step  → interval between elements, default = 1
"""


# ========================================
# USING NEGATIVE INDICES
# ========================================
"""
Negative indices access elements from the end of the tuple.

Indexing:
---------
-1 → last element
-2 → second last element
"""

# Slice from third last to end
s1 = tup[-3:]
print(s1)

# Slice from beginning to third last (excluding it)
s2 = tup[:-3]
print(s2)

# Slice from third last to second last
s3 = tup[-3:-1]
print(s3)

"""
Output:
-------
(7, 8, 9)
(0, 1, 2, 3, 4, 5, 6)
(7, 8)
"""


# ========================================
# USING STEP IN TUPLE SLICING
# ========================================
"""
Step controls how many elements to skip.
"""

# Slice with step = 2
s1 = tup[1:8:2]
print(s1)

# Slice with negative step (reverse tuple)
s2 = tup[::-1]
print(s2)

"""
Output:
-------
(1, 3, 5, 7)
(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
"""


# ========================================
# IMPORTANT NOTES ABOUT TUPLE SLICING
# ========================================
"""
1. Tuples are immutable → slicing cannot modify them
2. Slicing always creates a NEW tuple
3. Out-of-bound slicing is safe (no error)
4. Negative step reverses the tuple
"""


# ========================================
# LIST SLICING vs TUPLE SLICING
# ========================================
"""
Feature        | List               | Tuple
---------------|--------------------|-------------------
Mutability     | Mutable            | Immutable
Slicing        | Supported          | Supported
Modification   | Allowed            | Not allowed
Performance    | Slightly slower    | Slightly faster
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Tuple slicing extracts parts of a tuple
2. Syntax is same as list slicing
3. start is inclusive, stop is exclusive
4. Negative indices access from end
5. step controls skipping pattern
6. tup[::-1] reverses a tuple

Tuple slicing is useful for:
✔ Safe data access
✔ Functional-style programming
✔ Performance-sensitive code
✔ Read-only data structures
"""

"""
End of Tuple Slicing Module
---------------------------
"""
