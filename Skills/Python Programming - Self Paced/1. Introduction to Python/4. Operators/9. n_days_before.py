"""
Program: Day Before N Days

--------------------------------------------------
INTRODUCTION:
In this program, we determine the day that occurs
N days before a given day.

To keep the problem simple, days of the week
are represented using numbers:

Day        Number
-----------------
Sunday       0
Monday       1
Tuesday      2
Wednesday    3
Thursday     4
Friday       5
Saturday     6

--------------------------------------------------
PROBLEM STATEMENT:
Given:
- d : the current day (0 to 6)
- n : number of days before

Find:
- The day that falls n days before day d

--------------------------------------------------
KEY IDEA:
There are exactly 7 days in a week.
So, we use modulo (%) 7 to "wrap around" the week.

Formula:
day_before = (d - n) % 7

--------------------------------------------------
WHY MODULO (%) WORKS:
- Modulo keeps the result within 0 to 6
- It automatically handles large values of n
- Python handles negative modulo gracefully

Example:
d = 0 (Sunday)
n = 9

0 - 9 = -9
-9 % 7 = 5 → Friday
"""

# --------------------------------------------------
# FUNCTION TO FIND DAY BEFORE N DAYS
# --------------------------------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

def day_before_n_days(d, n):
    """
    Returns the day number (0 to 6)
    that occurs n days before day d
    """
    return (d - n) % 7


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

# Example inputs
d = int(input("Enter current day (0=Sun ... 6=Sat): "))
n = int(input("Enter number of days before: "))

# Calculate the result
result_day = day_before_n_days(d, n)

# Print the result
print("The day", n, "days before day", d, "is:", result_day)


"""
--------------------------------------------------
EXAMPLE WALKTHROUGHS:

Example 1:
Input:
d = 1 (Monday)
n = 1

Calculation:
(1 - 1) % 7 = 0

Output:
0 → Sunday

Explanation:
One day before Monday is Sunday.

--------------------------------------------------
Example 2:
Input:
d = 0 (Sunday)
n = 9

Calculation:
(0 - 9) % 7 = -9 % 7 = 5

Output:
5 → Friday

Explanation:
Nine days before Sunday is Friday.

--------------------------------------------------
Example 3:
Input:
d = 6 (Saturday)
n = 3

Calculation:
(6 - 3) % 7 = 3

Output:
3 → Wednesday

Explanation:
Three days before Saturday is Wednesday.

--------------------------------------------------
WHY PYTHON HANDLES NEGATIVE MODULO WELL:

In Python:
-9 % 7 = 5

This ensures results always stay in the valid
range of day numbers (0 to 6).

--------------------------------------------------
EDGE CASES HANDLED:
✔ Large values of n
✔ n greater than 7
✔ n equal to 0
✔ Any valid day input from 0 to 6

--------------------------------------------------
END OF PROGRAM
"""
