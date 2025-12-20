# ======================================================
# MODULE: NESTED LOOPS IN PYTHON
# ======================================================
# THEORY:
# ------------------------------------------------------
# A loop is a programming construct that repeats a block
# of code as long as a specified condition is True.
#
# A NESTED LOOP is a loop placed inside another loop.
# - Outer loop controls the number of iterations
# - Inner loop runs completely for each iteration
#   of the outer loop
#
# Nested loops are commonly used for:
# ✔ Printing patterns
# ✔ Multiplication tables
# ✔ Traversing 2D lists (lists of lists)
# ✔ Matrix-like data processing
# ======================================================


# ======================================================
# PROBLEM STATEMENT:
# ------------------------------------------------------
# Print multiplication tables for numbers 1 to 10.
# Example:
# Table of 1 → 1 2 3 ... 10
# Table of 2 → 2 4 6 ... 20
# ...
# ======================================================


# ======================================================
# INITIAL APPROACH (NOT RECOMMENDED)
# ------------------------------------------------------
# Writing separate loops for each table
# This approach is lengthy and inflexible
# ======================================================

for i in range(1, 11, 1):
    print(i, end=" ")
print()

for i in range(2, 21, 2):
    print(i, end=" ")
print()

for i in range(3, 31, 3):
    print(i, end=" ")
print()

# Output:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30


# ======================================================
# PROBLEMS WITH THIS APPROACH:
# ------------------------------------------------------
# ❌ Code repetition
# ❌ Not scalable
# ❌ Difficult to modify
# ======================================================


# ======================================================
# SOLUTION: USING NESTED LOOPS
# ------------------------------------------------------
# Outer loop → selects the table number
# Inner loop → prints multiples of that number
# ======================================================

for i in range(1, 6):
    for j in range(i, i * 10 + 1, i):
        print(j, end=" ")
    print()

# Output:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Outer loop (i) runs from 1 to 5
# - Inner loop (j) starts from i
# - Ends at i*10
# - Step size is i
#
# Example:
# i = 2 → j = 2, 4, 6, 8 ... 20
# ======================================================


# ======================================================
# NESTED LOOPS: MIXING FOR AND WHILE
# ------------------------------------------------------
# A for loop can contain a while loop (and vice versa)
# ======================================================

for i in range(1, 3):
    j = 1
    while j < 3:
        print(i, j)
        j += 1
    print("GFG")

# Output:
# 1 1
# 1 2
# GFG
# 2 1
# 2 2
# GFG


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Outer for loop controls i
# - Inner while loop controls j
# - After while loop completes, "GFG" is printed
# ======================================================


# ======================================================
# APPLICATION: TRAVERSING A LIST OF LISTS
# ------------------------------------------------------
# Nested loops are extremely useful for 2D structures
# ======================================================

ll = [[10, 20, 30], [40, 50, 60], [70, 80]]

for sublist in ll:
    for element in sublist:
        print(element, end=" ")
    print()

# Output:
# 10 20 30
# 40 50 60
# 70 80


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Outer loop iterates over each sublist
# - Inner loop iterates over elements of sublist
# - Used in matrices, grids, tables
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ Inner loop completes fully for each outer loop cycle
# ✔ break exits only the nearest loop
# ✔ continue affects only the current loop
# ✔ Nested loops increase time complexity
# ✔ Common in pattern problems & tables
#
# Time Complexity Example:
# Outer loop → n times
# Inner loop → m times
# Total → O(n × m)
# ======================================================
