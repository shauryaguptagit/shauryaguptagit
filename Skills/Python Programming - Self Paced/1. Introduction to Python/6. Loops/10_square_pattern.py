# ======================================================
# MODULE: SQUARE PATTERN IN PYTHON
# ======================================================
# THEORY:
# ------------------------------------------------------
# Pattern printing is a common programming exercise that
# helps in understanding:
# 1. Nested loops
# 2. Loop flow control
# 3. Output formatting
#
# In a SQUARE PATTERN:
# - Number of rows = n
# - Number of columns = n
#
# The pattern looks like:
# * * *
# * * *
# * * *
#
# for n = 3
# ======================================================


# ======================================================
# PROBLEM STATEMENT:
# ------------------------------------------------------
# Given an integer n, print a square pattern of stars (*)
# of size n x n.
#
# Example:
# If n = 4
#
# * * * *
# * * * *
# * * * *
# * * * *
# ======================================================


# ======================================================
# APPROACH:
# ------------------------------------------------------
# We use NESTED LOOPS:
#
# 1. Outer loop → Controls number of rows
# 2. Inner loop → Controls number of columns
#
# Each row prints n stars.
# After printing one row, move to the next line.
# ======================================================


# ======================================================
# PYTHON IMPLEMENTATION
# ======================================================

n = 4   # Size of the square pattern

for i in range(n):          # Outer loop → rows
    for j in range(n):      # Inner loop → columns
        print('*', end=' ')
    print()                 # Move to next line after each row


# ======================================================
# OUTPUT:
# ------------------------------------------------------
# * * * *
# * * * *
# * * * *
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
# 3. For each iteration of outer loop:
#    Inner loop runs 4 times:
#    j = 0, 1, 2, 3
#
# 4. Inner loop prints '* ' four times in one row
#
# 5. After inner loop finishes,
#    print() moves cursor to next line
#
# 6. Process repeats until all rows are printed
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ Square pattern uses nested loops
# ✔ Rows = columns = n
# ✔ Outer loop → rows
# ✔ Inner loop → stars in each row
# ✔ end=' ' keeps output on same line
# ✔ print() after inner loop creates new line
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
# ======================================================
