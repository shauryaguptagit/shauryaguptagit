"""
=========================================================
                PYTHON map() FUNCTION
=========================================================

The map() function in Python applies a given function
to each element of an iterable (list, tuple, set, etc.)
and returns a map object (iterator).

✔ Higher-order function
✔ Performs element-wise transformation
✔ Returns an iterator (lazy evaluation)
✔ Commonly used with lambda functions
"""

# =========================================================
# BASIC EXAMPLE: STRING TO INTEGER CONVERSION
# =========================================================
s = ['1', '2', '3', '4']
res = map(int, s)

print("\n--- String to Integer using map() ---")
print(list(res))

"""
Explanation:
map(int, s) applies int() to each string element.
All elements are converted from str to int.
"""


# =========================================================
# SYNTAX OF map()
# =========================================================
"""
map(function, iterable1, iterable2, ...)

function  -> Function applied to each element
iterable  -> One or more iterable objects
Returns   -> map object (iterator)
"""


# =========================================================
# CONVERTING MAP OBJECT TO LIST
# =========================================================
def double(val):
    return val * 2

a = [1, 2, 3, 4]
res = list(map(double, a))

print("\n--- Converting map object to list ---")
print(res)

"""
Explanation:
map(double, a) applies double() to each element.
list() converts map object into list.
"""


# =========================================================
# map() WITH LAMBDA FUNCTION
# =========================================================
a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a))

print("\n--- map() with lambda ---")
print(res)

"""
Explanation:
lambda x: x ** 2 squares each element.
Shorter and more readable than defining a function.
"""


# =========================================================
# map() WITH MULTIPLE ITERABLES
# =========================================================
a = [1, 2, 3]
b = [4, 5, 6]

res = map(lambda x, y: x + y, a, b)

print("\n--- map() with multiple iterables ---")
print(list(res))

"""
Explanation:
map() takes one element from each iterable.
lambda receives x from a and y from b.
Stops when shortest iterable ends.
"""


# =========================================================
# CONVERT STRINGS TO UPPERCASE
# =========================================================
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)

print("\n--- Convert strings to uppercase ---")
print(list(res))

"""
Explanation:
str.upper is passed directly as function.
map() applies it to every string.
"""


# =========================================================
# EXTRACT FIRST CHARACTER FROM STRINGS
# =========================================================
words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)

print("\n--- Extract first character ---")
print(list(res))

"""
Explanation:
lambda s: s[0] returns first character.
map() applies it to all strings.
"""


# =========================================================
# REMOVE WHITESPACES FROM STRINGS
# =========================================================
s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)

print("\n--- Remove whitespaces ---")
print(list(res))

"""
Explanation:
str.strip removes leading and trailing spaces.
map() applies it to each string.
"""


# =========================================================
# CELSIUS TO FAHRENHEIT CONVERSION
# =========================================================
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)

print("\n--- Celsius to Fahrenheit ---")
print(list(fahrenheit))

"""
Explanation:
Formula: (C × 9/5) + 32
map() converts each temperature.
"""


# =========================================================
# IMPORTANT CHARACTERISTICS OF map()
# =========================================================
"""
✔ map() returns an iterator, not a list
✔ Results are computed lazily
✔ Faster than loops for large data
✔ Often combined with lambda
✔ Stops at shortest iterable (if multiple)
"""


# =========================================================
# map() VS LIST COMPREHENSION (EXAM)
# =========================================================
"""
map() Example:
res = map(lambda x: x*x, a)

List Comprehension:
res = [x*x for x in a]

✔ List comprehension is more Pythonic
✔ map() preferred for function-based logic
"""


# =========================================================
# ONE-LINE VIVA QUESTIONS
# =========================================================
"""
Q: What does map() return?
A: A map object (iterator).

Q: Can map() take multiple iterables?
A: Yes, if function accepts multiple arguments.

Q: Is map() lazy or eager?
A: Lazy (values computed on demand).

Q: map() vs for loop?
A: map() is shorter and functional-style.
"""
