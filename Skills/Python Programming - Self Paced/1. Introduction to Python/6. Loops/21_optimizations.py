# =========================================================
# MODULE: OPTIMIZED DIVISORS & PRIME CHECK
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# This module covers optimized solutions for:
# 1) Finding all divisors of a number
# 2) Checking whether a number is prime
#
# Optimizations are important because basic approaches
# become very slow for large values of n.
# =========================================================


# =========================================================
# PROBLEM 1: FINDING ALL DIVISORS OF A NUMBER
# =========================================================
# A divisor of n is a number that divides n exactly
# without leaving a remainder.
#
# Example:
# n = 36 → 1, 2, 3, 4, 6, 9, 12, 18, 36
# =========================================================


# ---------------------------------------------------------
# BASIC APPROACH (NOT OPTIMIZED)
# ---------------------------------------------------------
# THEORY:
# - Loop from 1 to n
# - Check if n % x == 0
# - Time Complexity: O(n)
# - Inefficient for large n
# ---------------------------------------------------------

def divisors_basic(n):
    print("Basic Divisors Approach:")
    for x in range(1, n + 1):
        if n % x == 0:
            print(x, end=" ")
    print("\n")


# ---------------------------------------------------------
# OPTIMIZED APPROACH USING √n
# ---------------------------------------------------------
# THEORY:
# ---------------------------------------------------------
# Divisors always come in PAIRS:
# If x divides n, then (n // x) also divides n
#
# Example:
# n = 36
# 1 × 36
# 2 × 18
# 3 × 12
# 4 × 9
# 6 × 6
#
# We only need to check up to √n
#
# - If x * x < n → print both x and n//x
# - If x * x == n → print x once (perfect square)
#
# Time Complexity: O(√n)
# Space Complexity: O(1)
# ---------------------------------------------------------

def divisors_optimized(n):
    print("Optimized Divisors Approach:")
    x = 1
    while x * x < n:
        if n % x == 0:
            print(x, n // x)
        x += 1

    # Handling perfect square case
    if x * x == n:
        print(x)
    print()


# =========================================================
# PROBLEM 2: CHECKING IF A NUMBER IS PRIME
# =========================================================
# A prime number:
# - Greater than 1
# - Has exactly two divisors: 1 and itself
# =========================================================


# ---------------------------------------------------------
# BASIC PRIME CHECK (NOT OPTIMIZED)
# ---------------------------------------------------------
# THEORY:
# - Check divisibility from 2 to n-1
# - If any divisor found → NOT PRIME
# - Time Complexity: O(n)
# ---------------------------------------------------------

def prime_basic(n):
    print("Basic Prime Check:")
    if n <= 1:
        print("No")
        return

    for x in range(2, n):
        if n % x == 0:
            print("No")
            break
    else:
        print("Yes")


# ---------------------------------------------------------
# OPTIMIZED PRIME CHECK USING √n
# ---------------------------------------------------------
# THEORY:
# ---------------------------------------------------------
# If n has a divisor greater than √n,
# it must also have a divisor smaller than √n.
#
# So we only check up to √n.
#
# - Faster
# - Widely used in competitive programming
#
# Time Complexity: O(√n)
# Space Complexity: O(1)
# ---------------------------------------------------------

def prime_optimized(n):
    print("Optimized Prime Check:")
    if n <= 1:
        print("No")
        return

    x = 2
    while x * x <= n:
        if n % x == 0:
            print("No")
            break
        x += 1
    else:
        print("Yes")


# =========================================================
# DRIVER CODE (MAIN EXECUTION)
# =========================================================

if __name__ == "__main__":

    # -------- Divisors Example --------
    n1 = 36
    print("Number for Divisors:", n1)
    divisors_basic(n1)
    divisors_optimized(n1)

    # -------- Prime Check Example --------
    n2 = 25
    print("Number for Prime Check:", n2)
    prime_basic(n2)
    prime_optimized(n2)


# =========================================================
# SAMPLE OUTPUT
# ---------------------------------------------------------
# Number for Divisors: 36
# Basic Divisors Approach:
# 1 2 3 4 6 9 12 18 36
#
# Optimized Divisors Approach:
# 1 36
# 2 18
# 3 12
# 4 9
# 6
#
# Number for Prime Check: 25
# Basic Prime Check:
# No
# Optimized Prime Check:
# No
# =========================================================


# =========================================================
# IMPORTANT EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ Divisor optimization reduces time from O(n) → O(√n)
# ✔ Prime checking never needs to go beyond √n
# ✔ Perfect square must be handled separately
# ✔ These optimizations are industry standard
# =========================================================
