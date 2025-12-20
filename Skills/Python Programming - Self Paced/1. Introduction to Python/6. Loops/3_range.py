# ======================================================
# MODULE: PYTHON range() FUNCTION
# ======================================================
# THEORY:
# ------------------------------------------------------
# The range() function in Python is used to generate
# a sequence of numbers within a specified range.
#
# It is most commonly used with loops (especially for)
# to iterate a fixed number of times.
#
# range() DOES NOT return a list.
# It returns a range object (an iterable sequence).
# ======================================================


# ------------------------------------------------------
# BASIC EXAMPLE OF range()
# ------------------------------------------------------
# Printing numbers from 0 to 4
# ------------------------------------------------------

for i in range(5):
    print(i, end=" ")
print()

# Output:
# 0 1 2 3 4


# ======================================================
# SYNTAX OF range()
# ------------------------------------------------------
# range(start, stop, step)
#
# start → starting value (optional, default = 0)
# stop  → ending value (excluded, compulsory)
# step  → difference between numbers (optional, default = 1)
# ======================================================


# ======================================================
# 1️⃣ range(stop)
# ------------------------------------------------------
# Starts from 0
# Ends at stop - 1
# ------------------------------------------------------

# Printing first 6 whole numbers
for i in range(6):
    print(i, end=" ")
print()

# Output:
# 0 1 2 3 4 5


# ======================================================
# 2️⃣ range(start, stop)
# ------------------------------------------------------
# Starts from 'start'
# Ends at stop - 1
# ------------------------------------------------------

# Printing numbers from 5 to 19
for i in range(5, 20):
    print(i, end=" ")
print()

# Output:
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


# ======================================================
# 3️⃣ range(start, stop, step)
# ------------------------------------------------------
# Generates numbers with a fixed jump (step)
# ------------------------------------------------------

# Printing even numbers from 0 to 9
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Output:
# 0 2 4 6 8


# ======================================================
# POSITIVE STEP (INCREMENTING)
# ------------------------------------------------------

# Incrementing by 4
for i in range(0, 30, 4):
    print(i, end=" ")
print()

# Output:
# 0 4 8 12 16 20 24 28


# ======================================================
# NEGATIVE STEP (DECREMENTING)
# ------------------------------------------------------

# Decrementing by 2
for i in range(25, 2, -2):
    print(i, end=" ")
print()

# Output:
# 25 23 21 19 17 15 13 11 9 7 5 3


# ======================================================
# range() WITH FLOAT VALUES (NOT ALLOWED)
# ------------------------------------------------------
# range() only accepts integers
# ------------------------------------------------------

# ❌ This will raise TypeError
# for i in range(3.3):
#     print(i)

# Error:
# TypeError: 'float' object cannot be interpreted as an integer


# ======================================================
# CONCATENATING TWO range() OBJECTS
# ------------------------------------------------------
# Using itertools.chain()
# ------------------------------------------------------

from itertools import chain

print("Concatenating the result:")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=" ")
print()

# Output:
# 0 1 2 3 4 10 12 14 16 18


# ======================================================
# ACCESSING range() USING INDEX
# ------------------------------------------------------
# range supports indexing like lists
# ------------------------------------------------------

ele = range(10)[0]
print("First element:", ele)

ele = range(10)[-1]
print("Last element:", ele)

ele = range(10)[4]
print("Fifth element:", ele)

# Output:
# First element: 0
# Last element: 9
# Fifth element: 4


# ======================================================
# USING range() WITH LISTS
# ------------------------------------------------------
# Iterating list elements using index
# ------------------------------------------------------

fruits = ["apple", "banana", "cherry", "date"]

for i in range(len(fruits)):
    print(fruits[i])

# Output:
# apple
# banana
# cherry
# date


# ======================================================
# IMPORTANT POINTS TO REMEMBER (EXAM 🔥)
# ------------------------------------------------------
# ✔ range() works only with integers
# ✔ start, stop, step must be integers
# ✔ stop value is NOT included
# ✔ step cannot be zero (ValueError)
# ✔ range() returns a range object, not a list
# ✔ Supports positive & negative steps
# ✔ Supports indexing
# ======================================================
