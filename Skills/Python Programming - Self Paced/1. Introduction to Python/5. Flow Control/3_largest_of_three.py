# ======================================================
# PROGRAM: FIND MAXIMUM OF THREE NUMBERS IN PYTHON
# ======================================================
# THEORY:
# Finding the maximum of three numbers means comparing
# three values and determining which one is the largest.
#
# Example:
# If a = 10, b = 14, c = 12
# Maximum value = 14
#
# Python provides multiple ways to solve this problem:
# 1. Using built-in max() function
# 2. Using ternary conditional operator
# 3. Using sorted() function
# 4. Using heapq.nlargest()
# ======================================================


# ------------------------------------------------------
# INPUT VALUES
# ------------------------------------------------------
a = 10
b = 14
c = 12

print("Values are:", a, b, c)
print("-" * 40)


# ------------------------------------------------------
# METHOD 1: USING max() FUNCTION
# ------------------------------------------------------
# max() is a built-in Python function that returns the
# largest value among given inputs.
# It is the simplest, cleanest, and most recommended method.

res = max(a, b, c)
print("MAX USING max():", res)

# Explanation:
# max() compares all three values and directly returns
# the largest one.


# ------------------------------------------------------
# METHOD 2: USING TERNARY CONDITIONAL OPERATOR
# ------------------------------------------------------
# Ternary operator allows conditional logic in a single line.
# Syntax:
# value_if_true if condition else value_if_false

res = a if (a >= b and a >= c) else (b if b >= c else c)
print("MAX USING TERNARY OPERATOR:", res)

# Explanation:
# - First checks if a is greater than or equal to both b and c
# - If not, compares b and c
# - Assigns the largest value to res


# ------------------------------------------------------
# METHOD 3: USING sorted() FUNCTION
# ------------------------------------------------------
# sorted() arranges elements in ascending or descending order.
# By sorting in descending order, the largest element comes first.
# NOTE: This is not optimal for just 3 values but works well.

res = sorted([a, b, c], reverse=True)[0]
print("MAX USING sorted():", res)

# Explanation:
# - sorted([a, b, c], reverse=True) sorts numbers in descending order
# - Largest element appears at index 0


# ------------------------------------------------------
# METHOD 4: USING heapq.nlargest()
# ------------------------------------------------------
# heapq.nlargest() returns the top N largest elements.
# Useful for large datasets but overkill for 3 numbers.

import heapq

res = heapq.nlargest(1, [a, b, c])[0]
print("MAX USING heapq.nlargest():", res)

# Explanation:
# - heapq.nlargest(1, list) returns a list with 1 largest element
# - [0] extracts the value from the list


# ======================================================
# CONCLUSION:
# ------------------------------------------------------
# Best approach for this problem:
# ✔ max() → Simple, readable, efficient
#
# Other methods are useful for learning and understanding
# conditional logic, sorting, and heap-based operations.
# ======================================================