# ======================================================
# PROGRAM: CHECK WHETHER A YEAR IS A LEAP YEAR
# ======================================================
# THEORY:
# A leap year is a year that has 366 days instead of 365.
# The extra day is added in the month of February.
#
# LEAP YEAR RULES:
# 1. The year must be divisible by 4
# 2. If the year is divisible by 100, it is NOT a leap year
# 3. If the year is divisible by 400, it IS a leap year
#
# In short:
# - Divisible by 4 → Leap year
# - Divisible by 100 → NOT leap year
# - Divisible by 400 → Leap year
#
# Example:
# 2000 → Leap year (divisible by 400)
# 1900 → Not a leap year (divisible by 100 but not 400)
# ======================================================


# ------------------------------------------------------
# INPUT YEAR
# ------------------------------------------------------
y = 2000
print("Year:", y)
print("-" * 40)


# ------------------------------------------------------
# METHOD 1: USING NESTED IF CONDITIONS
# ------------------------------------------------------
# This method checks leap year rules step-by-step
# using nested if-else blocks.

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("NESTED IF: Leap year")
        else:
            print("NESTED IF: Not a leap year")
    else:
        print("NESTED IF: Leap year")
else:
    print("NESTED IF: Not a leap year")

# Explanation:
# - First checks divisibility by 4
# - Then checks divisibility by 100
# - Finally checks divisibility by 400


# ------------------------------------------------------
# METHOD 2: USING A SINGLE COMPOUND CONDITION
# ------------------------------------------------------
# This method combines all leap year rules into
# one logical condition using AND / OR operators.

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("SINGLE CONDITION: Leap year")
else:
    print("SINGLE CONDITION: Not a leap year")

# Explanation:
# - Year divisible by 4 AND not divisible by 100
# - OR year divisible by 400


# ------------------------------------------------------
# METHOD 3: USING calendar MODULE
# ------------------------------------------------------
# Python provides a built-in function calendar.isleap()
# which returns True if the year is a leap year.

import calendar

if calendar.isleap(y):
    print("CALENDAR MODULE: Leap year")
else:
    print("CALENDAR MODULE: Not a leap year")

# Explanation:
# - isleap(y) internally applies all leap year rules
# - Simplest and most readable method


# ------------------------------------------------------
# METHOD 4: USING LAMBDA FUNCTION
# ------------------------------------------------------
# Lambda is an anonymous one-line function.
# Useful for compact logic expressions.

leap = lambda x: (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)

if leap(y):
    print("LAMBDA FUNCTION: Leap year")
else:
    print("LAMBDA FUNCTION: Not a leap year")

# Explanation:
# - Lambda stores leap year logic in a single expression
# - Returns True or False based on the year


# ======================================================
# CONCLUSION:
# ------------------------------------------------------
# Best approaches:
# ✔ For exams & beginners → Nested if or Single condition
# ✔ For clean code → Single condition
# ✔ For real projects → calendar.isleap()
#
# All methods give the same correct result.
# ======================================================