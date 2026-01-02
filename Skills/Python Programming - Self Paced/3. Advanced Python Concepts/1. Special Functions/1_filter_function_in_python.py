"""
=========================================================
                filter() FUNCTION IN PYTHON
=========================================================

The filter() function is used to extract elements from an
iterable (list, tuple, set, etc.) that satisfy a condition.

It works by applying a function to each element:
✔ If function returns True  -> element is kept
✔ If function returns False -> element is discarded

filter() returns a FILTER OBJECT (iterator), so it is
usually converted to list(), tuple() or set().
"""

# =========================================================
# BASIC SYNTAX
# =========================================================
"""
filter(function, iterable)

Parameters:
function : A function that returns True or False
iterable : Any iterable (list, tuple, set, etc.)

Return:
filter object (iterator)
"""


# =========================================================
# BASIC EXAMPLE: WORDS STARTING WITH 'a'
# =========================================================
def starts_a(word):
    return word.startswith("a")


li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)

print("\n--- Words starting with 'a' ---")
print(list(res))

"""
Explanation:
starts_a() checks if a word starts with 'a'
filter() applies this function to each element
Only words returning True are kept
"""


# =========================================================
# EXAMPLE 1: filter() WITH A NAMED FUNCTION
# =========================================================
def even(n):
    return n % 2 == 0


a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

print("\n--- Even numbers using named function ---")
print(list(b))

"""
Explanation:
even() checks divisibility by 2
filter() keeps only even numbers
"""


# =========================================================
# EXAMPLE 2: filter() WITH LAMBDA FUNCTION
# =========================================================
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)

print("\n--- Even numbers using lambda ---")
print(list(b))

"""
Explanation:
Lambda replaces separate function definition
More concise and commonly used
"""


# =========================================================
# EXAMPLE 3: FILTER + MAP (FILTER THEN TRANSFORM)
# =========================================================
a = [1, 2, 3, 4, 5, 6]

b = filter(lambda x: x % 2 == 0, a)   # Filter even numbers
c = map(lambda x: x * 2, b)           # Double them

print("\n--- Filter even numbers and double them ---")
print(list(c))

"""
Explanation:
Step 1: filter() -> [2, 4, 6]
Step 2: map()    -> [4, 8, 12]
"""


# =========================================================
# EXAMPLE 4: FILTERING STRINGS BY LENGTH
# =========================================================
a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = filter(lambda w: len(w) > 5, a)

print("\n--- Words with length > 5 ---")
print(list(b))

"""
Explanation:
Keeps only words having more than 5 characters
"""


# =========================================================
# EXAMPLE 5: filter() WITH None (TRUTHINESS CHECK)
# =========================================================
"""
filter(None, iterable) removes all FALSY values

Falsy values include:
"", None, 0, False, [], {}, ()
"""

L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)

print("\n--- Removing falsy values ---")
print(list(A))

"""
Explanation:
Empty string -> False
None         -> False
0            -> False
Only truthy values remain
"""


# =========================================================
# IMPORTANT NOTES (EXAM / VIVA)
# =========================================================
"""
✔ filter() returns an iterator, not a list
✔ Must convert result using list(), tuple(), set()
✔ Commonly used with lambda functions
✔ Often combined with map()
✔ Alternative using list comprehension:

Example:
[x for x in a if x % 2 == 0]
"""


# =========================================================
# ONE-LINE VIVA ANSWERS
# =========================================================
"""
Q: What does filter() do?
A: It filters elements from an iterable based on a condition.

Q: What does filter() return?
A: A filter object (iterator).

Q: What happens when filter(None, iterable) is used?
A: It removes all falsy values.

Q: Is filter faster than loops?
A: Yes, it is optimized and memory efficient.
"""
