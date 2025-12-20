# ======================================================
# MODULE: INVERTED TRIANGLE PATTERN IN PYTHON
# ======================================================
# THEORY:
# ------------------------------------------------------
# Pattern printing helps in understanding:
# 1. Nested loops
# 2. Control of rows and columns
# 3. Loop-based logic
#
# In an INVERTED TRIANGLE PATTERN:
# - Number of rows = n
# - Number of stars starts from n
# - Number of stars decreases by 1 in each next row
#
# Example (n = 4):
# * * * *
# * * *
# * *
# *
# ======================================================


# ======================================================
# PROBLEM STATEMENT:
# ------------------------------------------------------
# Given an integer n, print an inverted triangular
# pattern of stars.
#
# The first row contains n stars.
# Each next row contains one star less than the previous.
# ======================================================


# ======================================================
# APPROACH:
# ------------------------------------------------------
# We use NESTED LOOPS:
#
# 1. Outer loop → Controls number of rows
# 2. Inner loop → Controls number of stars per row
#
# Relationship:
# Row 0 → n stars
# Row 1 → n-1 stars
# Row 2 → n-2 stars
#
# Hence, inner loop runs (n - i) times
# ======================================================


# ======================================================
# PYTHON IMPLEMENTATION
# ======================================================

n = 4   # Number of rows in inverted triangle

for i in range(n):              # Outer loop → rows
    for j in range(n - i):      # Inner loop → stars
        print('*', end=' ')
    print()                     # Move to next line after each row


# ======================================================
# OUTPUT:
# ------------------------------------------------------
# * * * *
# * * *
# * *
# *
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
#    i = 0 → prints 4 stars
#    i = 1 → prints 3 stars
#    i = 2 → prints 2 stars
#    i = 3 → prints 1 star
#
# 4. After each inner loop,
#    print() moves to the next line
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ This is an INVERTED RIGHT-ANGLED TRIANGLE
# ✔ Outer loop controls rows
# ✔ Inner loop controls stars
# ✔ Stars per row = n - i
# ✔ end=' ' keeps stars on same line
# ✔ print() after inner loop creates next row
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ======================================================
