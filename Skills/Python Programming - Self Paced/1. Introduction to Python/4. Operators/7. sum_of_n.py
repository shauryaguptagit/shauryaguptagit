"""
Program: Sum of First N Natural Numbers

--------------------------------------------------
INTRODUCTION:
In this program, we calculate the sum of the first n natural numbers.
This is useful when we need cumulative totals without manually
adding each number one by one.

--------------------------------------------------
PROBLEM STATEMENT:
Imagine a person saves:
- 1 rupee on day 1
- 2 rupees on day 2
- 3 rupees on day 3
- and so on...

We need to find how much money the person saves after n days.

--------------------------------------------------
IDENTIFYING THE SERIES:
The savings follow the natural number sequence:

1, 2, 3, 4, ..., n

This is a sequence of the first n natural numbers.

--------------------------------------------------
MATHEMATICAL FORMULA:
The sum of the first n natural numbers is given by:

Sn = n(n + 1) / 2

--------------------------------------------------
EXAMPLE:
For n = 10,

S10 = 10 × (10 + 1) / 2
     = 10 × 11 / 2
     = 55

So, the total savings after 10 days is 55 rupees.
"""

# --------------------------------------------------
# FUNCTION TO CALCULATE SUM OF NATURAL NUMBERS
# --------------------------------------------------
# Uses direct mathematical formula
# Time Complexity: O(1)
# Space Complexity: O(1)

def sum_of_natural_numbers(n):
    """
    Calculates the sum of the first n natural numbers
    using the formula Sn = n(n + 1) / 2
    """
    return n * (n + 1) // 2


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

# Taking input from the user
n = int(input("Enter the value of n: "))

# Calculating the sum
total_sum = sum_of_natural_numbers(n)

# Printing the result
print(f"The sum of the first {n} natural numbers is: {total_sum}")


"""
--------------------------------------------------
UNDERSTANDING THE FORMULA (DERIVATION):

Let the sum of the first n natural numbers be:

Sn = 1 + 2 + 3 + ... + n

Reverse the series:

Sn = n + (n-1) + (n-2) + ... + 1

Add both equations term by term:

2Sn = (1+n) + (2+n-1) + (3+n-2) + ... + (n+1)

Each pair adds up to (n + 1)
Total number of such pairs = n

So:
2Sn = n(n + 1)

Dividing both sides by 2:

Sn = n(n + 1) / 2

--------------------------------------------------
DISCUSSION:
- This approach avoids loops
- Very efficient for large values of n
- Commonly used in mathematics and programming problems

--------------------------------------------------
END OF PROGRAM
"""
