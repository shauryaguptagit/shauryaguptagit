# ======================================================
# PROGRAM: CHECK WHETHER A NUMBER IS ODD OR EVEN
# ======================================================
# THEORY:
# Even numbers are those numbers that are exactly divisible
# by 2, meaning the remainder when divided by 2 is 0.
#
# Odd numbers are those numbers that are NOT exactly divisible
# by 2, meaning the remainder when divided by 2 is 1.
#
# Python provides multiple ways to check whether a number
# is odd or even:
# 1. Using Modulo (%) operator
# 2. Using lambda + map (memory efficient)
# 3. Using Bitwise AND (&) operator
# ======================================================


# ------------------------------------------------------
# METHOD 1: USING MODULO (%) OPERATOR
# ------------------------------------------------------
# The modulo operator (%) returns the remainder of division.
# If number % 2 == 0 → Even
# If number % 2 == 1 → Odd

x = 24

if x % 2 == 0:
    print("MODULO METHOD:", x, "is Even")
else:
    print("MODULO METHOD:", x, "is Odd")

# Checking another number
x = 7

if x % 2 == 0:
    print("MODULO METHOD:", x, "is Even")
else:
    print("MODULO METHOD:", x, "is Odd")


# ------------------------------------------------------
# METHOD 2: USING LAMBDA WITH MAP (MEMORY EFFICIENT)
# ------------------------------------------------------
# lambda is an anonymous function (one-line function)
# map() applies this function to every element of a list
#
# map() is memory efficient because it creates an iterator
# instead of creating a full list in memory.

numbers = [1, 2, 3, 4, 5]

result = map(
    lambda num: str(num) + " Even" if num % 2 == 0 else str(num) + " Odd",
    numbers
)

print("\nLAMBDA + MAP METHOD:")
print("\n".join(result))


# ------------------------------------------------------
# METHOD 3: USING BITWISE AND (&) OPERATOR
# ------------------------------------------------------
# In binary:
# - Even numbers always end with 0
# - Odd numbers always end with 1
#
# Bitwise AND (&) with 1 checks the last bit:
# number & 1 == 0 → Even
# number & 1 == 1 → Odd

x = 24

if x & 1 == 0:
    print("\nBITWISE METHOD:", x, "is Even")
else:
    print("\nBITWISE METHOD:", x, "is Odd")

# Checking another number
x = 7

if x & 1 == 0:
    print("BITWISE METHOD:", x, "is Even")
else:
    print("BITWISE METHOD:", x, "is Odd")


# ======================================================
# END OF PROGRAM
# ======================================================