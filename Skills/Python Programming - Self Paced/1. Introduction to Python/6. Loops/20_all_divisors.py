# =========================================================
# MODULE: ALL DIVISORS OF A NUMBER
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# A divisor of a number is an integer that divides the
# number exactly without leaving any remainder.
#
# In simple words:
# If n % x == 0, then x is a divisor of n.
#
# Examples:
# n = 12 → Divisors: 1, 2, 3, 4, 6, 12
# n = 13 → Divisors: 1, 13 (Prime number)
# n = 15 → Divisors: 1, 3, 5, 15
# =========================================================


# =========================================================
# PROBLEM STATEMENT:
# ---------------------------------------------------------
# Given an integer n, find and print all its divisors.
# =========================================================


# =========================================================
# APPROACH:
# ---------------------------------------------------------
# 1. Start from 1 up to n
# 2. Check for every number x:
#       if n % x == 0 → x is a divisor
# 3. Print all such values of x
#
# This approach works because every divisor of n must
# lie between 1 and n (inclusive).
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# =========================================================


# =========================================================
# METHOD 1: USING FOR LOOP
# =========================================================
# THEORY:
# ---------------------------------------------------------
# - We iterate from 1 to n using a for loop
# - For each number x, check divisibility
# - If divisible, print x
# =========================================================

def divisors_using_for(n):
    print("Divisors using for loop:")
    for x in range(1, n + 1):
        if n % x == 0:
            print(x, end=" ")
    print("\n")


# =========================================================
# METHOD 2: USING WHILE LOOP
# =========================================================
# THEORY:
# ---------------------------------------------------------
# - Similar logic as for loop
# - Use a while loop to control iteration manually
# - Useful when loop conditions need more flexibility
# =========================================================

def divisors_using_while(n):
    print("Divisors using while loop:")
    x = 1
    while x <= n:
        if n % x == 0:
            print(x, end=" ")
        x += 1
    print("\n")


# =========================================================
# DRIVER CODE (MAIN EXECUTION)
# =========================================================

if __name__ == "__main__":

    n = 12
    print("Number:", n)
    print()

    divisors_using_for(n)
    divisors_using_while(n)


# =========================================================
# SAMPLE OUTPUT
# ---------------------------------------------------------
# Number: 12
#
# Divisors using for loop:
# 1 2 3 4 6 12
#
# Divisors using while loop:
# 1 2 3 4 6 12
# =========================================================


# =========================================================
# IMPORTANT NOTES (EXAM / VIVA)
# ---------------------------------------------------------
# ✔ Divisors always include 1 and the number itself
# ✔ Prime numbers have exactly two divisors
# ✔ This method checks all numbers from 1 to n
# ✔ Time complexity is O(n)
# ✔ More optimized methods exist using √n
# =========================================================
