"""
========================================
FIND FIRST DIGIT IN PYTHON
========================================

Overview:
---------
Finding the first digit of a positive number is a common
programming problem that helps understand:
✔ Loops
✔ Integer division
✔ Logarithms
✔ Mathematical reasoning

In this module, we explore TWO methods:
1. Iterative Division
2. Logarithmic Calculation
"""

# ========================================
# METHOD 1: ITERATIVE DIVISION
# ========================================
"""
Concept:
--------
The idea is to remove the LAST digit repeatedly
until only ONE digit remains.

We use FLOOR DIVISION (//) to remove the last digit.

Example:
--------
7549 → 754 → 75 → 7
"""

def get_first_digit(x):
    """Returns the first digit using iterative division"""
    while x >= 10:
        x = x // 10
    return x

# Example usage
number = 7549
first_digit = get_first_digit(number)
print("The first digit is:", first_digit)

"""
Output:
-------
The first digit is: 7
"""

"""
Step-by-step execution:
-----------------------
7549 // 10 = 754
754  // 10 = 75
75   // 10 = 7
Stop when number < 10
"""


# ========================================
# METHOD 2: USING LOGARITHMS
# ========================================
"""
Concept:
--------
Using logarithms, we can determine how many digits
a number has.

Steps:
------
1. Compute log10(x)
2. Take integer part → digits - 1
3. Divide the number by 10^(digits - 1)

This directly isolates the first digit.
"""

import math

def get_first_digit_log(x):
    """Returns the first digit using logarithms"""
    d = int(math.log10(x))   # Number of digits minus 1
    return x // 10 ** d

# Example usage
number = 7549
first_digit = get_first_digit_log(number)
print("The first digit is:", first_digit)

"""
Output:
-------
The first digit is: 7
"""

"""
Mathematical explanation:
-------------------------
log10(7549) ≈ 3.87
int(3.87) = 3
10^3 = 1000
7549 // 1000 = 7
"""


# ========================================
# COMPARISON OF METHODS
# ========================================
"""
Iterative Division:
-------------------
✔ Simple
✔ Easy to understand
✔ Uses loop
✖ Slower for very large numbers

Logarithmic Method:
-------------------
✔ Faster for large numbers
✔ No loop required
✖ Requires math module
✖ Slightly complex to understand
"""

"""
Example comparison:
-------------------
Iterative:
7549 → 754 → 75 → 7

Logarithmic:
log10(7549) = 3.87
7549 // 10^3 = 7
"""


# ========================================
# EDGE CASE NOTE
# ========================================
"""
Important:
----------
- These methods assume POSITIVE numbers
- log10(0) is undefined
- For negative numbers, absolute value should be used
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. First digit can be found by reducing number to single digit
2. Floor division (//) removes last digit
3. log10 gives digit count information
4. Iterative method is beginner-friendly
5. Logarithmic method is efficient for large inputs

This problem is useful for:
✔ Logic building
✔ Competitive programming
✔ Interviews
✔ Mathematical thinking in Python
"""

"""
End of Find First Digit Module
------------------------------
"""
