# =========================================================
# MODULE: FIBONACCI NUMBERS USING STAIRCASE PROBLEM
# =========================================================
# INTRODUCTION:
# ---------------------------------------------------------
# The Fibonacci sequence is a series of numbers where
# each number is the sum of the two preceding ones.
#
# Fibonacci Sequence (starting from 1, 1):
# 1, 1, 2, 3, 5, 8, 13, ...
#
# In this program, we understand Fibonacci numbers
# using a real-life problem called the "Staircase Puzzle".
# =========================================================


# =========================================================
# THE STAIRCASE PUZZLE (PROBLEM STATEMENT)
# ---------------------------------------------------------
# Imagine a staircase with 'n' stairs.
# You can climb:
# - 1 stair at a time OR
# - 2 stairs at a time
#
# TASK:
# Find the number of distinct ways to reach the top.
#
# EXAMPLES:
# ---------------------------------------------------------
# n = 3
# Ways:
# 1 + 1 + 1
# 1 + 2
# 2 + 1
# Total = 3 ways
#
# n = 4
# Ways:
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
# Total = 5 ways
# =========================================================


# =========================================================
# OBSERVATION & RELATION
# ---------------------------------------------------------
# Ways(n) = Ways(n - 1) + Ways(n - 2)
#
# This is EXACTLY the Fibonacci relation.
#
# Hence:
# Number of ways to climb 'n' stairs
# = Fibonacci number at position 'n'
# =========================================================


# =========================================================
# ITERATIVE APPROACH TO FIBONACCI (MOST EFFICIENT)
# =========================================================
# THEORY:
# ---------------------------------------------------------
# - Start with base cases:
#   F(0) = 1
#   F(1) = 1
#
# - Every next term:
#   F(n) = F(n-1) + F(n-2)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# This approach is preferred for:
# - Exams
# - Interviews
# - Large inputs
# =========================================================


def fibonacci_staircase(n):
    """
    This function prints Fibonacci numbers up to n
    representing the number of ways to reach each stair.
    """

    # Base case: no stairs
    if n == 0:
        print(1)
        return

    # Base case: one stair
    if n == 1:
        print(1, 1)
        return

    # First two Fibonacci values
    a = 1
    b = 1

    print(a, b, end=" ")

    # Generate remaining Fibonacci numbers
    for i in range(2, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":

    # Number of stairs
    n = 5

    print("Number of stairs:", n)
    print("Ways to reach each stair (Fibonacci Sequence):")

    fibonacci_staircase(n)


# =========================================================
# STEP-BY-STEP EXPLANATION (FOR n = 5)
# ---------------------------------------------------------
# F(0) = 1
# F(1) = 1
# F(2) = 1 + 1 = 2
# F(3) = 1 + 2 = 3
# F(4) = 2 + 3 = 5
# F(5) = 3 + 5 = 8
#
# OUTPUT:
# 1 1 2 3 5 8
# =========================================================


# =========================================================
# KEY EXAM / VIVA POINTS
# ---------------------------------------------------------
# ✔ Fibonacci follows: F(n) = F(n-1) + F(n-2)
# ✔ Staircase problem maps directly to Fibonacci
# ✔ Iterative approach is most efficient
# ✔ Used in:
#   - Dynamic Programming
#   - Problem Solving
#   - Mathematics & Algorithms
#
# INTERVIEW TIP:
# - Always explain Fibonacci using real-life problems
# =========================================================
