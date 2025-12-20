# ======================================================
# MODULE: LOOPS IN PYTHON
# ======================================================
# THEORY:
# ------------------------------------------------------
# Loops are used in Python to execute a block of code
# repeatedly until a certain condition is satisfied.
#
# Loops help us:
# 1. Avoid writing repetitive code
# 2. Make programs shorter and more readable
# 3. Handle flexible user requirements
#
# Common use cases of loops:
# - Printing patterns
# - Iterating over collections (list, tuple, string)
# - Repeating calculations (tables, sums, factorials)
# - Running continuous services
# ======================================================


# ------------------------------------------------------
# PROBLEM STATEMENT:
# ------------------------------------------------------
# Take a number 'n' from the user
# Print the multiplication table of n
# (First 10 multiples of n)
#
# Example:
# If n = 3
# Output: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
# ======================================================


# ------------------------------------------------------
# BASIC APPROACH (WITHOUT LOOP) - NOT RECOMMENDED
# ------------------------------------------------------
# This approach is lengthy and inflexible
# If user wants more multiples, code must be rewritten
# ------------------------------------------------------

# n = int(input("Enter a number: "))
# print(n * 1)
# print(n * 2)
# print(n * 3)
# print(n * 4)
# print(n * 5)
# print(n * 6)
# print(n * 7)
# print(n * 8)
# print(n * 9)
# print(n * 10)


# ======================================================
# WHY LOOPS ARE NEEDED
# ------------------------------------------------------
# - Removes repetition
# - Makes code flexible
# - Allows dynamic control over iterations
# - Improves readability and maintainability
# ======================================================


# ------------------------------------------------------
# SOLUTION USING FOR LOOP
# ------------------------------------------------------
# Using a for loop to print multiplication table
# ------------------------------------------------------

n = int(input("Enter a number: "))

print(f"Multiplication table of {n}:")

for i in range(1, 11):
    print(n * i)


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# range(1, 11) generates numbers from 1 to 10
# 'i' takes one value at a time from the range
# Each iteration prints n multiplied by i
#
# This loop automatically handles repetition
# and works for any value of n
# ======================================================


# ------------------------------------------------------
# APPLICATIONS OF LOOPS
# ------------------------------------------------------
# 1. Repeating tasks (printing, calculations)
# 2. Traversing data structures (lists, strings)
# 3. Handling user-defined limits
# 4. Running background or continuous programs
# ======================================================
