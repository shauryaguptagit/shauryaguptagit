"""
========================================
PYTHON LISTS
========================================

Overview:
---------
A list is a built-in data structure in Python used to store
an ordered collection of items.

Key Characteristics:
--------------------
✔ Ordered (maintains insertion order)
✔ Mutable (can be modified)
✔ Allows duplicate elements
✔ Index-based (0-based indexing)
✔ Can store mixed data types
✔ Can store nested lists

Lists are one of the MOST important data structures in Python.
"""

# ========================================
# CREATING A LIST
# ========================================

# ----------------------------------------
# 1. USING SQUARE BRACKETS
# ----------------------------------------
a = [1, 2, 3, 4, 5]                     # integers
b = ['apple', 'banana', 'cherry']       # strings
c = [1, 'hello', 3.14, True]            # mixed data types

print(a)
print(b)
print(c)

"""
Output:
-------
[1, 2, 3, 4, 5]
['apple', 'banana', 'cherry']
[1, 'hello', 3.14, True]
"""


# ----------------------------------------
# 2. USING list() CONSTRUCTOR
# ----------------------------------------
a = list((1, 2, 3, 'apple', 4.5))
print(a)

b = list("GFG")
print(b)

"""
Output:
-------
[1, 2, 3, 'apple', 4.5]
['G', 'F', 'G']
"""


# ----------------------------------------
# 3. CREATING LIST WITH REPEATED ELEMENTS
# ----------------------------------------
a = [2] * 5
b = [0] * 7

print(a)
print(b)

"""
Output:
-------
[2, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0]
"""


# ========================================
# ACCESSING LIST ELEMENTS
# ========================================
"""
Lists use 0-based indexing.
Negative indexing accesses elements from the end.
"""

a = [10, 20, 30, 40, 50]

print(a[0])       # first element
print(a[-1])      # last element
print(a[1:4])     # slicing (index 1 to 3)

"""
Output:
-------
10
50
[20, 30, 40]
"""


# ========================================
# ADDING ELEMENTS INTO LIST
# ========================================
"""
Methods:
--------
append() → add single element at end
insert() → add element at specific index
extend() → add multiple elements
clear()  → remove all elements
"""

a = []

a.append(10)
print("After append(10):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a.clear()
print("After clear():", a)

"""
Output:
-------
After append(10): [10]
After insert(0, 5): [5, 10]
After extend([15, 20, 25]): [5, 10, 15, 20, 25]
After clear(): []
"""


# ========================================
# UPDATING ELEMENTS IN LIST
# ========================================
"""
Lists are mutable → values can be updated using index.
"""

a = [10, 20, 30, 40, 50]
a[1] = 25
print(a)

"""
Output:
-------
[10, 25, 30, 40, 50]
"""


# ========================================
# REMOVING ELEMENTS FROM LIST
# ========================================
"""
remove(x) → removes first occurrence of x
pop(i)    → removes element at index i
del       → deletes element at index
"""

a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]
print("After del a[0]:", a)

"""
Output:
-------
After remove(30): [10, 20, 40, 50]
Popped element: 20
After pop(1): [10, 40, 50]
After del a[0]: [40, 50]
"""


# ========================================
# ITERATING OVER LISTS
# ========================================
"""
Lists can be traversed using loops.
"""

a = ['apple', 'banana', 'cherry']

for item in a:
    print(item)

"""
Output:
-------
apple
banana
cherry
"""


# ========================================
# NESTED LISTS
# ========================================
"""
A list inside another list is called a nested list.
Commonly used for matrices and tables.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])

"""
Output:
-------
6
"""


# ========================================
# LIST COMPREHENSION
# ========================================
"""
List comprehension provides a compact way
to create lists using expressions.
"""

squares = [x**2 for x in range(1, 6)]
print(squares)

"""
Output:
-------
[1, 4, 9, 16, 25]
"""

"""
Explanation:
------------
- range(1, 6) → 1 to 5
- x**2 → square of x
- [] collects results into a list
"""


# ========================================
# HOW PYTHON STORES LIST ELEMENTS
# ========================================
"""
Lists store REFERENCES to objects in memory,
not the actual values.

Mutable objects inside lists can be modified,
immutables cannot.
"""

a = [10, 20, "GfG", 40, True]

print(a)
print(a[0])
print(a[1])
print(a[2])

"""
Output:
-------
[10, 20, 'GfG', 40, True]
10
20
GfG
"""

"""
Explanation:
------------
- Integers, strings, booleans are separate objects
- List stores references to them
- Each element retains its original data type
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Lists are ordered and mutable
2. Can store mixed data types
3. Indexing starts from 0
4. Support slicing and iteration
5. Can grow and shrink dynamically
6. List comprehension is powerful and concise
7. Lists store references, not raw values

Lists are fundamental for:
✔ Data storage
✔ Algorithms
✔ Problem solving
✔ Real-world Python programs
"""

"""
End of Python Lists Module
--------------------------
"""
