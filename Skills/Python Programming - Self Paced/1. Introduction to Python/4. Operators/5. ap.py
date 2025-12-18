"""
Program: N-th Term of an Arithmetic Progression (AP)

--------------------------------------------------
PROBLEM STATEMENT:
Given:
- First term of an Arithmetic Progression (a)
- Common difference (d)
- A positive integer N

Task:
Find the N-th term of the Arithmetic Progression.

--------------------------------------------------
WHAT IS AN ARITHMETIC PROGRESSION?
An Arithmetic Progression (AP) is a sequence of numbers
in which the difference between consecutive terms is constant.

Example:
2, 3, 4, 5, 6, ...
Here:
First term (a) = 2
Common difference (d) = 1

--------------------------------------------------
FORMULA:
The N-th term of an AP is given by:

Tn = a + (N - 1) * d

--------------------------------------------------
EXAMPLE:
Input:
a = 2
d = 1
N = 5

Calculation:
T5 = 2 + (5 - 1) * 1
   = 2 + 4
   = 6

Output:
The 5th term of the series is 6
"""

# --------------------------------------------------
# NAIVE APPROACH
# --------------------------------------------------
# This approach calculates the N-th term by repeatedly
# adding the common difference using a loop.
# Time Complexity: O(n)
# Space Complexity: O(1)

def nth_term_naive(a, d, n):
    """
    Calculates N-th term using a loop (Naive Approach)
    """
    term = a
    for i in range(1, n):
        term += d
    return term


# --------------------------------------------------
# OPTIMIZED APPROACH (EXPECTED APPROACH)
# --------------------------------------------------
# This approach uses the direct formula of AP.
# Time Complexity: O(1)
# Space Complexity: O(1)

def nth_term_formula(a, d, n):
    """
    Calculates N-th term using formula:
    Tn = a + (n - 1) * d
    """
    return a + (n - 1) * d


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

# Taking input from the user
a = int(input("Enter the first term (a): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the term number (N): "))

# Using Naive Method
naive_result = nth_term_naive(a, d, n)

# Using Formula Method
formula_result = nth_term_formula(a, d, n)

# Printing results
print("\nUsing Naive Approach:")
print(f"The {n}th term of the series is: {naive_result}")

print("\nUsing Formula Approach:")
print(f"The {n}th term of the series is: {formula_result}")

"""
--------------------------------------------------
SUMMARY:
- Naive approach uses a loop and is slower for large N
- Formula approach is efficient and preferred
- Formula-based solution is recommended for exams
  and competitive programming

--------------------------------------------------
END OF PROGRAM
"""
