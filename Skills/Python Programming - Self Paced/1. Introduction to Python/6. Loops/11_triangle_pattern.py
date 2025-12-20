# ======================================================
# MODULE: PRINTING TRIANGLE PATTERN IN PYTHON
# ======================================================
# THEORY:
# ------------------------------------------------------
# Pattern printing is an important topic in Python
# because it helps us understand:
# 1. Nested loops
# 2. Loop counters
# 3. Output formatting
# 4. Logical thinking for row-column relationships
#
# In a TRIANGLE PATTERN:
# - Number of rows = n
# - Number of stars in each row = row number
#
# Example (n = 4):
# *
# * *
# * * *
# * * * *
# ======================================================


# ======================================================
# PROBLEM STATEMENT:
# ------------------------------------------------------
# Given an integer n, print a triangular pattern of stars.
# Each row contains stars equal to the row number.
#
# Example:
# If n = 4
#
# *
# * *
# * * *
# * * * *
# ======================================================


# ======================================================
# APPROACH:
# ------------------------------------------------------
# We use NESTED LOOPS:
#
# 1. Outer loop → Controls number of rows
# 2. Inner loop → Controls number of stars in each row
#
# Relationship:
# Row 0 → 1 star
# Row 1 → 2 stars
# Row 2 → 3 stars
#
# Hence, inner loop runs (i + 1) times
# ======================================================


# ======================================================
# PYTHON IMPLEMENTATION
# ======================================================

n = 4   # Number of rows in the triangle

for i in range(n):              # Outer loop → rows
    for j in range(i + 1):      # Inner loop → stars
        print('*', end=' ')
    print()                     # Move to next line after each row


# ======================================================
# OUTPUT:
# ------------------------------------------------------
# *
# * *
# * * *
# * * * *
# ======================================================


# ======================================================
# STEP-BY-STEP EXECUTION:
# ------------------------------------------------------
# 1. n is set to 4
#
# 2. Outer loop runs 4 times:
#    i = 0, 1, 2, 3
#
# 3. Inner loop behavior:
#    i = 0 → runs 1 time → prints 1 star
#    i = 1 → runs 2 times → prints 2 stars
#    i = 2 → runs 3 times → prints 3 stars
#    i = 3 → runs 4 times → prints 4 stars
#
# 4. After each inner loop completes,
#    print() moves cursor to the next line
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ This is a RIGHT-ANGLED TRIANGLE pattern
# ✔ Outer loop controls rows
# ✔ Inner loop controls stars
# ✔ Stars per row = i + 1
# ✔ end=' ' keeps stars on the same line
# ✔ print() after inner loop creates new row
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ======================================================
