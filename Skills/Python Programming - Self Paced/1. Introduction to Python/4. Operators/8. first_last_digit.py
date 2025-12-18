"""
Program: Find the Last Digit of a Number in Python

--------------------------------------------------
INTRODUCTION:
In this program, we learn how to find the last digit of a given number
using Python. The solution works for:
- Positive numbers
- Negative numbers
- Single-digit numbers
- Zero

--------------------------------------------------
PROBLEM STATEMENT:
Write a Python program that takes an integer as input
and prints its last digit.

--------------------------------------------------
EXAMPLE SCENARIOS:
Input: 234  -> Output: 4
Input: 7    -> Output: 7
Input: 0    -> Output: 0
Input: -234 -> Output: 4

--------------------------------------------------
BASIC IDEA:
The modulo (%) operator returns the remainder when a number
is divided by 10. The remainder corresponds to the last digit.

For non-negative numbers:
234 % 10 = 4
78  % 10 = 8
7   % 10 = 7
0   % 10 = 0

--------------------------------------------------
PROBLEM WITH NEGATIVE NUMBERS:
In Python, modulo (%) behaves differently for negative numbers.

Example:
-234 % 10 = 6

This happens because Python ensures the remainder has the same
sign as the divisor (10).

--------------------------------------------------
SOLUTION:
To handle negative numbers correctly, we use abs().
abs(x) converts a number to its positive value.

Then:
last_digit = abs(x) % 10

This always gives the correct last digit.
"""

# --------------------------------------------------
# FUNCTION TO FIND LAST DIGIT
# --------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

def find_last_digit(number):
    """
    Returns the last digit of any integer
    (positive, negative, or zero)
    """
    return abs(number) % 10


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

# Taking input from the user
x = int(input("Enter an integer: "))

# Finding the last digit
last_digit = find_last_digit(x)

# Printing the result
print("The last digit is:", last_digit)


"""
--------------------------------------------------
UNDERSTANDING MODULO WITH NEGATIVE NUMBERS:

In Python:
-234 % 10 = 6
Reason:
-234 = (-24 × 10) + 6

234 % -10 = -6
Reason:
234 = (-23 × -10) + (-6)

--------------------------------------------------
WHY abs() WORKS:
abs(x) removes the sign of the number and converts it to positive.
This ensures that modulo always gives the correct last digit.

--------------------------------------------------
EDGE CASES HANDLED:
✔ Positive numbers
✔ Negative numbers
✔ Single-digit numbers
✔ Zero

--------------------------------------------------
END OF PROGRAM
"""
