# =========================================================
# MODULE: LCM (LEAST COMMON MULTIPLE) OF TWO NUMBERS
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# The Least Common Multiple (LCM) of two numbers is the
# smallest positive integer that is divisible by both
# numbers without leaving a remainder.
#
# Example:
# Input:  a = 12, b = 15
# Output: 60
#
# Explanation:
# Multiples of 12 → 12, 24, 36, 48, 60, ...
# Multiples of 15 → 15, 30, 45, 60, ...
# First common multiple = 60
# =========================================================
#
# APPROACHES COVERED:
# 1. Using Iterative Loop
# 2. Using GCD (Efficient Method)
# 3. Using Prime Factorization
# =========================================================


# =========================================================
# APPROACH 1: FIND LCM USING LOOP
# =========================================================
# THEORY:
# ---------------------------------------------------------
# - Start from the greater of the two numbers
# - Check multiples of the greater number
# - The first number divisible by both is the LCM
#
# Time Complexity: O(a * b)
# Space Complexity: O(1)
#
# NOTE:
# - Simple to understand
# - Not efficient for large numbers
# =========================================================

def lcm_using_loop(a, b):
    greater = max(a, b)
    smaller = min(a, b)

    for i in range(greater, a * b + 1, greater):
        if i % smaller == 0:
            return i


# =========================================================
# APPROACH 2: FIND LCM USING GCD (BEST APPROACH)
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Mathematical relation:
#
# LCM(a, b) × GCD(a, b) = a × b
#
# So,
# LCM(a, b) = (a × b) / GCD(a, b)
#
# Python provides math.gcd() to compute GCD efficiently.
#
# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(1)
#
# MOST RECOMMENDED METHOD (Exams + Interviews)
# =========================================================

import math

def lcm_using_gcd(a, b):
    return (a * b) // math.gcd(a, b)


# =========================================================
# APPROACH 3: FIND LCM USING PRIME FACTORIZATION
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Steps:
# 1. Find prime factors of both numbers
# 2. Take maximum power of each prime
# 3. Multiply them together to get LCM
#
# Example:
# 12 = 2^2 × 3
# 15 = 3 × 5
# LCM = 2^2 × 3 × 5 = 60
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# NOTE:
# - Useful for understanding mathematics
# - Not preferred for large inputs
# =========================================================

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def lcm_using_prime_factors(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)

    lcm = 1
    for factor in set(factors_a + factors_b):
        lcm *= factor ** max(factors_a.count(factor),
                             factors_b.count(factor))
    return lcm


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":

    a = 12
    b = 15

    print("Numbers:", a, "and", b)
    print("LCM using Loop Method:", lcm_using_loop(a, b))
    print("LCM using GCD Method:", lcm_using_gcd(a, b))
    print("LCM using Prime Factorization:", lcm_using_prime_factors(a, b))


# =========================================================
# KEY EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ LCM = Least Common Multiple
# ✔ LCM(a, b) × GCD(a, b) = a × b
# ✔ GCD-based method is most efficient
# ✔ Loop method is easiest but slow
# ✔ Prime factorization improves math understanding
#
# INTERVIEW TIP:
# - Always use GCD method unless asked otherwise
# =========================================================
