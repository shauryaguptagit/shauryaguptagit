# =========================================================
# MODULE: CHECK PRIME NUMBER IN PYTHON
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# A Prime Number is a natural number greater than 1
# that has exactly two distinct positive divisors:
# 1 and itself.
#
# Examples:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 → Prime
# 1, 4, 6, 8, 9, 10, 12 → Not Prime
#
# NOTE:
# - Numbers less than or equal to 1 are NOT prime
# - Negative numbers are NOT prime
# =========================================================


# =========================================================
# METHOD 1: USING FLAG VARIABLE (MOST COMMON & RECOMMENDED)
# =========================================================
# THEORY:
# ---------------------------------------------------------
# A number 'n' is prime if it has no divisors between
# 2 and √n.
#
# Why up to √n?
# If n = a × b and both a and b are greater than √n,
# then their product would be greater than n.
# Hence, at least one factor must be ≤ √n.
#
# Time Complexity: O(√n)
# Space Complexity: O(1)
# =========================================================

def is_prime_flag(n):
    if n <= 1:
        return False

    is_prime = True  # Flag variable

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


# =========================================================
# METHOD 2: USING sympy.isprime()
# =========================================================
# THEORY:
# ---------------------------------------------------------
# The SymPy library provides a built-in function isprime()
# that checks if a number is prime.
#
# NOTE:
# - Requires external library installation:
#   pip install sympy
# - For very large numbers, there is a small probability
#   of pseudo-primes.
# =========================================================

def is_prime_sympy(n):
    from sympy import isprime
    return isprime(n)


# =========================================================
# METHOD 3: USING SIEVE OF ERATOSTHENES
# =========================================================
# THEORY:
# ---------------------------------------------------------
# The Sieve of Eratosthenes is an algorithm used to find
# all prime numbers up to n.
#
# Steps:
# 1. Create a boolean list initialized as True
# 2. Mark multiples of each prime as False
# 3. Finally check sieve[n]
#
# Time Complexity: O(n log log n)
# Space Complexity: O(n)
# =========================================================

def is_prime_sieve(n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]


# =========================================================
# METHOD 4: USING RECURSION
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Recursive approach checks divisibility from √n down to 2.
#
# Base Cases:
# - If i <= 2 → Prime
# - If n % i == 0 → Not Prime
#
# Time Complexity: O(√n)
# Space Complexity: O(√n) (recursive stack)
# =========================================================

from math import sqrt

def is_prime_recursive(n, i):
    if n <= 1:
        return False
    if i <= 2:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i - 1)


# =========================================================
# DRIVER CODE (TESTING ALL METHODS)
# =========================================================

if __name__ == "__main__":

    num = 29
    print("Number:", num)

    print("\nUsing Flag Variable Method:")
    print(is_prime_flag(num))

    print("\nUsing SymPy Method:")
    print(is_prime_sympy(num))

    print("\nUsing Sieve of Eratosthenes:")
    print(is_prime_sieve(num))

    print("\nUsing Recursive Method:")
    print(is_prime_recursive(num, int(sqrt(num)) + 1))


# =========================================================
# SAMPLE OUTPUT
# ---------------------------------------------------------
# Number: 29
# True
# True
# True
# True
# =========================================================


# =========================================================
# EXAM / VIVA IMPORTANT POINTS
# ---------------------------------------------------------
# ✔ Prime numbers have exactly two divisors
# ✔ Best method for single number → √n method
# ✔ Sieve is best for finding multiple primes
# ✔ sympy.isprime() is simplest but external
# ✔ Negative numbers are NOT prime
# =========================================================
