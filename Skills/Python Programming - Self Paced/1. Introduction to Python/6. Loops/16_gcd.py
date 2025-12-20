# =========================================================
# MODULE: GCD (GREATEST COMMON DIVISOR) IN PYTHON
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# The gcd() function in Python is used to compute the
# Greatest Common Divisor (GCD) of two or more integers.
#
# GCD is the largest positive integer that divides both
# numbers without leaving a remainder.
#
# Example:
# a = 60, b = 48
# GCD = 12
#
# Common divisors of 60 and 48:
# [1, 2, 3, 4, 6, 12]
# Greatest among them = 12
# =========================================================
#
# Python provides a built-in function gcd() in the math module.
# =========================================================


# =========================================================
# IMPORT REQUIRED MODULES
# =========================================================

import math
from functools import reduce


# =========================================================
# SYNTAX OF math.gcd()
# ---------------------------------------------------------
# math.gcd(x, y)
#
# Parameters:
# - x, y: non-negative integers
# - At least one number must be non-zero
#
# Returns:
# - GCD of x and y
# - If one number is 0, returns absolute value of the other
# =========================================================


# =========================================================
# EXAMPLE 1: GCD OF TWO NUMBERS
# =========================================================
# THEORY:
# ---------------------------------------------------------
# gcd(a, b) returns the largest integer that divides both
# a and b exactly.
# =========================================================

def gcd_two_numbers(a, b):
    return math.gcd(a, b)


# =========================================================
# EXAMPLE 2: GCD OF A NUMBER AND ZERO
# =========================================================
# THEORY:
# ---------------------------------------------------------
# If one number is 0, gcd() returns the absolute value
# of the other number.
#
# gcd(0, x) = |x|
# =========================================================

def gcd_with_zero(a, b):
    return math.gcd(a, b)


# =========================================================
# EXAMPLE 3: GCD OF TWO CO-PRIME NUMBERS
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Two numbers are called co-prime if their GCD is 1.
# Example: 17 and 29
# =========================================================

def gcd_coprime(a, b):
    return math.gcd(a, b)


# =========================================================
# EXAMPLE 4: GCD OF A LIST OF NUMBERS
# =========================================================
# THEORY:
# ---------------------------------------------------------
# To compute GCD of multiple numbers:
# - Use functools.reduce()
# - Apply math.gcd cumulatively
#
# Example:
# nums = [48, 64, 80]
# gcd = gcd(gcd(48, 64), 80) = 16
# =========================================================

def gcd_of_list(nums):
    return reduce(math.gcd, nums)


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":

    # Example 1: GCD of two numbers
    a = 60
    b = 48
    print("GCD of", a, "and", b, "is:", gcd_two_numbers(a, b))

    # Example 2: GCD when one number is zero
    x = 0
    y = 25
    print("GCD of", x, "and", y, "is:", gcd_with_zero(x, y))

    # Example 3: GCD of co-prime numbers
    p = 17
    q = 29
    print("GCD of", p, "and", q, "is:", gcd_coprime(p, q))

    # Example 4: GCD of a list of numbers
    numbers = [48, 64, 80]
    print("GCD of list", numbers, "is:", gcd_of_list(numbers))


# =========================================================
# KEY EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ gcd() is present in math module
# ✔ gcd(x, 0) = |x|
# ✔ gcd of co-prime numbers is 1
# ✔ reduce() is used for multiple values
# ✔ gcd() always returns a non-negative integer
#
# INTERVIEW TIP:
# - Prefer math.gcd() over manual Euclidean algorithm
# =========================================================
