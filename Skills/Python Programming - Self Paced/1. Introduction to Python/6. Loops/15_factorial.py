# =========================================================
# MODULE: FACTORIAL OF A NUMBER
# =========================================================
# PROBLEM STATEMENT:
# ---------------------------------------------------------
# Given an integer n, compute its factorial.
#
# Factorial of n is represented as n! and defined as:
# n! = n × (n-1) × (n-2) × ... × 2 × 1
#
# Example:
# Input:  n = 6
# Output: 720
#
# Explanation:
# 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720
#
# =========================================================
# APPLICATIONS OF FACTORIAL:
# ---------------------------------------------------------
# - Permutations and combinations
# - Probability and statistics
# - Mathematical series
# - Algorithm complexity analysis
# =========================================================
#
# APPROACHES COVERED:
# 1. Using math.factorial()
# 2. Using NumPy np.prod()
# 3. Iterative (for loop)
# 4. Recursive function
# =========================================================


# =========================================================
# APPROACH 1: USING math.factorial()
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Python provides a built-in function factorial() in the
# math module that directly computes factorial.
#
# Pros:
# - Fast
# - Reliable
# - Internally optimized
#
# Cons:
# - Logic is hidden (not good for learning basics)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# =========================================================

import math

def factorial_math(n):
    return math.factorial(n)


# =========================================================
# APPROACH 2: USING NumPy np.prod()
# =========================================================
# THEORY:
# ---------------------------------------------------------
# NumPy can multiply all values in a range using vectorized
# operations at C-level, which is very efficient.
#
# Steps:
# - Generate numbers from 1 to n
# - Multiply all numbers using np.prod()
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# NOTE:
# - Requires NumPy library
# - Not recommended in exams unless NumPy is allowed
# =========================================================

import numpy as np

def factorial_numpy(n):
    return np.prod(range(1, n + 1))


# =========================================================
# APPROACH 3: ITERATIVE METHOD (FOR LOOP)
# =========================================================
# THEORY:
# ---------------------------------------------------------
# This is the most commonly used and recommended approach
# in exams and interviews.
#
# Logic:
# - Initialize result as 1
# - Multiply result by numbers from 1 to n
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# =========================================================

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# =========================================================
# APPROACH 4: RECURSIVE METHOD
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Factorial follows a recursive definition:
#
# fact(n) = n × fact(n-1)
# fact(0) = fact(1) = 1
#
# Base Case:
# - n <= 1 → return 1
#
# Recursive Case:
# - n × factorial(n-1)
#
# Time Complexity: O(n)
# Space Complexity: O(n)  (due to recursion stack)
#
# NOTE:
# - Not recommended for very large n
# =========================================================

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":
    n = 6

    print("Number:", n)
    print("Factorial using math.factorial():", factorial_math(n))
    print("Factorial using NumPy:", factorial_numpy(n))
    print("Factorial using Iterative method:", factorial_iterative(n))
    print("Factorial using Recursive method:", factorial_recursive(n))


# =========================================================
# KEY EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ Factorial of 0 is 1
# ✔ Iterative approach is most preferred
# ✔ Recursive approach uses stack memory
# ✔ math.factorial() is fastest and safest
# ✔ NumPy approach is not ideal for exams
#
# INTERVIEW TIP:
# - Use Iterative method unless recursion is required
# =========================================================
