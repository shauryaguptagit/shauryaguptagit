"""
Program: N-th Term of a Geometric Progression (GP)

--------------------------------------------------
PROBLEM STATEMENT:
Given:
- First term of a Geometric Progression (a)
- Common ratio (r)
- Position (n)

Task:
Find the n-th term of the Geometric Progression.

NOTE:
Since the result can be very large, return the answer modulo (10^9 + 7).

--------------------------------------------------
WHAT IS A GEOMETRIC PROGRESSION?
A Geometric Progression (GP) is a sequence of numbers
where each term is obtained by multiplying the previous
term by a constant called the common ratio.

Example:
2, 4, 8, 16, ...
Here:
First term (a) = 2
Common ratio (r) = 2

--------------------------------------------------
FORMULA:
The n-th term of a GP is given by:

Tn = a × r^(n - 1)

--------------------------------------------------
EXAMPLES:

Input:
a = 2, r = 2, n = 4
Output:
16

Explanation:
GP series: 2, 4, 8, 16, ...
The 4th term is 16.

Input:
a = 4, r = 3, n = 3
Output:
36

Explanation:
GP series: 4, 12, 36, 108, ...
The 3rd term is 36.
"""

# --------------------------------------------------
# CONSTANT FOR MODULO OPERATION
# --------------------------------------------------
# Used to prevent integer overflow
MOD = int(1e9 + 7)


# --------------------------------------------------
# NAIVE APPROACH
# --------------------------------------------------
# Idea:
# Multiply the first term by the common ratio (n - 1) times.
# This directly simulates the GP.

# Time Complexity: O(n)
# Space Complexity: O(1)

def nth_term_naive(a, r, n):
    """
    Finds n-th term of GP using a loop
    """
    result = a
    for _ in range(1, n):
        result = (result * r) % MOD
    return result


# --------------------------------------------------
# OPTIMIZED APPROACH (EXPECTED APPROACH)
# --------------------------------------------------
# Idea:
# Instead of multiplying r repeatedly, use Binary Exponentiation
# to compute r^(n - 1) efficiently.

# Time Complexity: O(log n)
# Space Complexity: O(1)

def power_mod(x, n):
    """
    Computes (x^n) % MOD using Binary Exponentiation
    """
    result = 1
    x = x % MOD

    while n > 0:
        # If n is odd, multiply current base
        if n % 2 == 1:
            result = (result * x) % MOD

        # Square the base
        x = (x * x) % MOD
        n //= 2

    return result


def nth_term_optimized(a, r, n):
    """
    Finds n-th term of GP using formula and binary exponentiation
    """
    return (a * power_mod(r, n - 1)) % MOD


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

# Taking input from user
a = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter term number (n): "))

# Calculating using both approaches
naive_ans = nth_term_naive(a, r, n)
optimized_ans = nth_term_optimized(a, r, n)

# Printing results
print("\nUsing Naive Approach:")
print(f"The {n}th term of the GP is: {naive_ans}")

print("\nUsing Optimized (Binary Exponentiation) Approach:")
print(f"The {n}th term of the GP is: {optimized_ans}")

"""
--------------------------------------------------
SUMMARY:
- Naive approach uses repeated multiplication (slow for large n)
- Optimized approach uses Binary Exponentiation (fast & efficient)
- Optimized method is preferred for large inputs and exams

--------------------------------------------------
END OF PROGRAM
"""
