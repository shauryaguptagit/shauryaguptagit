# =========================================================
# MODULE: COUNT DIGITS IN A NUMBER
# =========================================================
# PROBLEM STATEMENT:
# ---------------------------------------------------------
# Given a number n, count how many digits are present in it.
#
# Example:
# Input:  n = 1567
# Output: 4
#
# Input:  n = 255
# Output: 3
#
# =========================================================
# APPROACHES COVERED:
# 1. Iterative Division Method
# 2. Recursive Digit Removal
# 3. Logarithmic Method (log10)
# 4. String Conversion Method
# =========================================================


# =========================================================
# APPROACH 1: ITERATIVE SOLUTION (DIVISION BY 10)
# =========================================================
# THEORY:
# ---------------------------------------------------------
# We repeatedly remove the last digit of the number by
# dividing it by 10 (integer division).
#
# Example:
# n = 1567
# 1567 // 10 = 156
# 156  // 10 = 15
# 15   // 10 = 1
# 1    // 10 = 0  (stop)
#
# Each division removes one digit.
#
# Time Complexity: O(log10(n))
# Space Complexity: O(1)
# =========================================================

def count_digits_iterative(n):
    if n == 0:
        return 1  # Edge case: 0 has 1 digit

    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count


# =========================================================
# APPROACH 2: RECURSIVE DIGIT REMOVAL
# =========================================================
# THEORY:
# ---------------------------------------------------------
# We remove one digit at a time using recursion.
#
# Base Case:
# If n becomes a single-digit number, return 1.
#
# Recursive Case:
# Count current digit + digits in remaining number.
#
# Time Complexity: O(log10(n))
# Space Complexity: O(log10(n)) [recursive call stack]
# =========================================================

def count_digits_recursive(n):
    if n // 10 == 0:
        return 1
    return 1 + count_digits_recursive(n // 10)


# =========================================================
# APPROACH 3: USING LOG BASE 10
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Mathematical formula:
# Number of digits = floor(log10(n)) + 1
#
# Example:
# n = 58964
# log10(58964) ≈ 4.77
# floor(4.77) + 1 = 5
#
# NOTE:
# - Works only for positive numbers
# - log10(0) is undefined
#
# Time Complexity: O(1)
# Space Complexity: O(1)
# =========================================================

import math

def count_digits_log(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n) + 1)


# =========================================================
# APPROACH 4: CONVERT NUMBER TO STRING
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Convert the number to a string and return its length.
#
# Example:
# n = 58964
# str(n) = "58964"
# length = 5
#
# Time Complexity: O(1)
# Space Complexity: O(number of digits)
# =========================================================

def count_digits_string(n):
    return len(str(n))


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":
    n = 58964

    print("Number:", n)
    print("Digits (Iterative):", count_digits_iterative(n))
    print("Digits (Recursive):", count_digits_recursive(n))
    print("Digits (Log10):", count_digits_log(n))
    print("Digits (String):", count_digits_string(n))


# =========================================================
# KEY EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ Division by 10 removes last digit
# ✔ Recursion mirrors iterative logic
# ✔ log10 gives digits - 1
# ✔ String method is simplest but uses extra memory
# ✔ Edge case: n = 0 → digit count = 1
#
# INTERVIEW TIP:
# - Prefer Iterative or Log method
# - Avoid String method if memory matters
# =========================================================
