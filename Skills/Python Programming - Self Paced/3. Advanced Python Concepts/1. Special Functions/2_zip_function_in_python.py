"""
=========================================================
                    zip() FUNCTION IN PYTHON
=========================================================

The zip() function is used to combine two or more iterables
(lists, tuples, strings, dictionaries, etc.) into a single
iterator of tuples.

Each tuple contains elements from the input iterables
that share the same index position.

Example:
a = ["Liam", "Emma", "Noah"]
b = [90, 85, 88]

Result:
[("Liam", 90), ("Emma", 85), ("Noah", 88)]
"""

# =========================================================
# SYNTAX
# =========================================================
"""
zip(*iterables)

Parameters:
*iterables : One or more iterable objects

Return Value:
An iterator of tuples
"""


# =========================================================
# BASIC WORKING OF zip()
# =========================================================
a = [1, 2, 3]
b = ['a', 'b', 'c']

# No iterable passed
res = zip()
print("\n--- No iterable passed ---")
print(list(res))

# One iterable passed
res = zip(a)
print("\n--- One iterable passed ---")
print(list(res))

# Two iterables passed
res = zip(a, b)
print("\n--- Two iterables passed ---")
print(list(res))

"""
Explanation:
1) No iterable -> empty iterator
2) One iterable -> each element wrapped in a single-element tuple
3) Two iterables -> elements paired by index
"""


# =========================================================
# ITERABLES OF DIFFERENT LENGTHS
# =========================================================
names = ['Hiro', 'Mila', 'Tariq']
scores = [88, 94]

res = zip(names, scores)
print("\n--- Iterables of different lengths ---")
print(list(res))

"""
Explanation:
zip() stops when the shortest iterable ends.
'Tariq' is ignored because there is no matching score.
"""


# =========================================================
# UNZIPPING DATA USING zip()
# =========================================================
a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]

fruits, quantities = zip(*a)

print("\n--- Unzipping data ---")
print("Fruits:", fruits)
print("Quantities:", quantities)

"""
Explanation:
* operator unpacks the list of tuples.
zip(*a) separates first elements and second elements.
Resulting outputs are tuples.
"""


# =========================================================
# COMBINING DICTIONARY KEYS AND VALUES
# =========================================================
d = {'name': 'Felix', 'age': 27, 'grade': 'A'}

keys = d.keys()
values = d.values()

res = zip(keys, values)

print("\n--- Dictionary keys and values ---")
print(list(res))

"""
Explanation:
zip() pairs each key with its corresponding value.
Useful for iteration and data transformation.
"""


# =========================================================
# COMMON PRACTICAL USE CASES
# =========================================================
"""
1) Iterating over multiple lists together
2) Creating dictionaries from two lists
3) Unzipping paired data
4) Data processing and alignment
"""


# =========================================================
# CREATE DICTIONARY USING zip()
# =========================================================
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 88]

student_dict = dict(zip(names, marks))

print("\n--- Creating dictionary using zip() ---")
print(student_dict)


# =========================================================
# IMPORTANT NOTES (EXAM / VIVA)
# =========================================================
"""
✔ zip() returns an iterator, not a list
✔ Must convert result using list(), tuple(), dict()
✔ Stops at shortest iterable
✔ Supports any iterable type
✔ Very memory efficient
"""


# =========================================================
# ONE-LINE VIVA ANSWERS
# =========================================================
"""
Q: What does zip() do?
A: Combines multiple iterables into tuples based on index.

Q: What happens if iterables have different lengths?
A: zip() stops at the shortest iterable.

Q: What does zip() return?
A: An iterator of tuples.

Q: How do you unzip data?
A: Use zip(*iterable_of_tuples)
"""
