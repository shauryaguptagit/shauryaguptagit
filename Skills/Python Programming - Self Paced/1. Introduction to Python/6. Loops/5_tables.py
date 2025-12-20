# ======================================================
# MODULE: TABLE OF A NUMBER (MULTIPLICATION TABLE)
# ======================================================
# THEORY:
# ------------------------------------------------------
# Creating a multiplication table is a basic yet
# important programming exercise.
#
# It helps us understand:
# ✔ Loops (while and for)
# ✔ Repetitive execution
# ✔ Controlling iteration count
#
# A multiplication table prints multiples of a number:
# n × 1, n × 2, n × 3, ...
# ======================================================


# ======================================================
# BASIC MULTIPLICATION TABLE USING WHILE LOOP
# ------------------------------------------------------
# This program prints the first 10 multiples of a number
# ------------------------------------------------------

n = 5      # Number whose table is to be printed
i = 1      # Loop counter

while i <= 10:
    print(n * i, end=" ")
    i += 1

print("\n")  # New line after table

# Output:
# 5 10 15 20 25 30 35 40 45 50


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - n is fixed as 5
# - i starts from 1
# - while loop runs till i <= 10
# - n * i is printed in each iteration
# - i is incremented after each loop
# ======================================================


# ======================================================
# EXTENDED TABLE USING WHILE LOOP (USER-SPECIFIED LENGTH)
# ------------------------------------------------------
# This program prints first 'm' multiples of number 'n'
# ------------------------------------------------------

n = 5      # Number whose table is required
m = 7      # Number of multiples to print
i = 1

while i <= m:
    print(n * i, end=" ")
    i += 1

print("\n")

# Output:
# 5 10 15 20 25 30 35


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - n = number for table
# - m = how many multiples user wants
# - Loop runs m times instead of fixed 10
# - Makes program flexible
# ======================================================


# ======================================================
# BASIC MULTIPLICATION TABLE USING FOR LOOP
# ------------------------------------------------------
# Printing first 10 multiples using for loop
# ------------------------------------------------------

n = 5

for i in range(1, 11):
    print(n * i, end=" ")

print("\n")

# Output:
# 5 10 15 20 25 30 35 40 45 50


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - for loop automatically handles iteration
# - range(1, 11) generates numbers from 1 to 10
# - n * i is printed for each value
# ======================================================


# ======================================================
# EXTENDED TABLE USING FOR LOOP (USER-SPECIFIED LENGTH)
# ------------------------------------------------------
# Printing first 'm' multiples using for loop
# ------------------------------------------------------

n = 5
m = 7

for i in range(1, m + 1):
    print(n * i, end=" ")

print("\n")

# Output:
# 5 10 15 20 25 30 35


# ======================================================
# FINAL NOTES (EXAM IMPORTANT) 🔥
# ------------------------------------------------------
# ✔ while loop is condition-based
# ✔ for loop is sequence-based
# ✔ for loop is cleaner for fixed iterations
# ✔ while loop gives more control
# ✔ Both loops can solve same problems
# ✔ Using 'm' makes program flexible
# ======================================================
