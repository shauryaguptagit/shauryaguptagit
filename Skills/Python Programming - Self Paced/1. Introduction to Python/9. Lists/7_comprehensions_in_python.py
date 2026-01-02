"""
========================================================
COMPREHENSIONS IN PYTHON
========================================================

Comprehensions in Python provide a concise and efficient
way to create new sequences from existing ones.

They reduce:
✔ Boilerplate code
✔ Long loops
✔ Temporary variables

And improve:
✔ Readability
✔ Performance
✔ Maintainability
"""

# ======================================================
# WHY DO WE NEED COMPREHENSIONS?
# ======================================================
"""
1. Encourages Modular Thinking
   - Logic is written in compact, reusable expressions

2. Widely Used in Real-World Code
   - Data science (filtering, transformations)
   - Web development
   - Automation scripts

3. Easier Debugging & Testing
   - Fewer lines → fewer bugs

4. Seamless Integration
   - Works well with zip(), enumerate(), lambda(), etc.
"""


# ======================================================
# TYPES OF COMPREHENSIONS IN PYTHON
# ======================================================
"""
1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Comprehension
"""


# ======================================================
# 1. LIST COMPREHENSION
# ======================================================
"""
Used to create lists in a single readable line.

Syntax:
-------
[expression for item in iterable if condition]

Components:
-----------
expression → operation on each item
item       → variable name
iterable   → source collection
condition  → optional filter
"""

# Example 1: Generating even numbers
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [num for num in a if num % 2 == 0]
print(res)

"""
Output:
-------
[2, 4, 6, 8]
"""

# Example 2: Creating a list of squares
res = [num**2 for num in range(1, 6)]
print(res)

"""
Output:
-------
[1, 4, 9, 16, 25]
"""

# Equivalent loop (for understanding)
squares = []
for num in range(1, 6):
    squares.append(num**2)


# ======================================================
# 2. DICTIONARY COMPREHENSION
# ======================================================
"""
Used to create dictionaries dynamically.

Syntax:
-------
{key_expression: value_expression for item in iterable if condition}
"""

# Example 1: Number → Cube mapping
res = {num: num**3 for num in range(1, 6)}
print(res)

"""
Output:
-------
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# Example 2: Mapping states to capitals using zip()
states = ["Texas", "California", "Florida"]
capitals = ["Austin", "Sacramento", "Tallahassee"]

res = {state: capital for state, capital in zip(states, capitals)}
print(res)

"""
Output:
-------
{'Texas': 'Austin', 'California': 'Sacramento', 'Florida': 'Tallahassee'}
"""

# Equivalent loop
mapping = {}
for state, capital in zip(states, capitals):
    mapping[state] = capital


# ======================================================
# 3. SET COMPREHENSION
# ======================================================
"""
Used to create sets.
Automatically removes duplicates.

Syntax:
-------
{expression for item in iterable if condition}
"""

# Example 1: Unique even numbers
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)

"""
Output:
-------
{2, 4, 6}
"""

# Example 2: Set of squares
res = {num**2 for num in range(1, 6)}
print(res)

"""
Output:
-------
{1, 4, 9, 16, 25}
"""

# Note:
# Order is not guaranteed in sets


# ======================================================
# 4. GENERATOR COMPREHENSION
# ======================================================
"""
Creates an iterator instead of storing all values at once.

Key Feature:
------------
✔ Lazy Evaluation (memory efficient)

Syntax:
-------
(expression for item in iterable if condition)
"""

# Example 1: Even numbers using generator
res = (num for num in range(10) if num % 2 == 0)
print(list(res))

"""
Output:
-------
[0, 2, 4, 6, 8]
"""

# Example 2: Squares using generator
res = (num**2 for num in range(1, 6))
print(tuple(res))

"""
Output:
-------
(1, 4, 9, 16, 25)
"""

# Generator values are exhausted after use
# Calling again will give empty result


# ======================================================
# MEMORY COMPARISON
# ======================================================
"""
List comprehension → Stores all values in memory
Generator          → Generates values one-by-one

Use Generators when:
✔ Large data
✔ Streaming data
✔ Memory efficiency matters
"""


# ======================================================
# COMPREHENSION COMPARISON TABLE
# ======================================================
"""
Type          | Output Type | Duplicates | Memory Efficient
--------------|-------------|------------|-----------------
List          | list        | Allowed    | No
Dictionary    | dict        | Keys unique| No
Set           | set         | Removed    | No
Generator     | iterator    | Allowed    | Yes
"""


# ======================================================
# COMMON INTERVIEW QUESTIONS
# ======================================================
"""
Q1. Can we nest comprehensions?
✔ Yes

Example:
---------
matrix = [[i*j for j in range(3)] for i in range(3)]

Q2. Can we use if-else?
✔ Yes

Example:
---------
res = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ Comprehensions make code concise and expressive
✔ List comprehension is the most commonly used
✔ Dictionary comprehension is great for mappings
✔ Set comprehension removes duplicates automatically
✔ Generator comprehension saves memory
✔ Prefer readability over over-compacting logic
"""

"""
End of Comprehensions Module
----------------------------
"""
