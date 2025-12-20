# ======================================================
# MODULE: PYTHON CONTINUE STATEMENT
# ======================================================
# THEORY:
# ------------------------------------------------------
# The continue statement in Python is a loop control
# statement used inside for and while loops.
#
# When continue is executed:
# ✔ The current iteration is skipped
# ✔ Remaining code inside the loop for that iteration
#   is NOT executed
# ✔ Control jumps to the NEXT iteration of the loop
#
# IMPORTANT DIFFERENCE:
# - break    → exits the loop completely
# - continue → skips ONLY the current iteration
# ======================================================


# ======================================================
# BASIC EXAMPLE: SKIPPING A VALUE IN A FOR LOOP
# ------------------------------------------------------

for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")

print()

# Output:
# 1 2 3 4 5 7 8 9 10


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Loop runs from 1 to 10
# - When i == 6:
#   → continue is executed
#   → print statement is skipped
# - Loop resumes from next value (7)
# ======================================================


# ======================================================
# SYNTAX EXAMPLE (GENERAL FORM)
# ------------------------------------------------------
# while True:
#     ...
#     if condition:
#         continue
#     statement
# ======================================================


# ======================================================
# EXAMPLE 1: SKIPPING SPECIFIC CHARACTERS IN A STRING
# ------------------------------------------------------

for char in "GeeksforGeeks":
    if char == "e":
        continue
    print(char, end=" ")

print()

# Output:
# G k s f o r G k s


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Loop iterates through each character
# - When character is 'e':
#   → continue skips print()
# - All characters except 'e' are printed
# ======================================================


# ======================================================
# EXAMPLE 2: CONTINUE IN NESTED LOOPS
# ------------------------------------------------------

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in a:
    for num in row:
        if num == 3:
            continue
        print(num, end=" ")

print()

# Output:
# 1 2 4 5 6 7 8 9


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Nested loops iterate over a 2D list
# - When num == 3:
#   → continue skips printing 3
# - All other numbers are printed
# - continue affects ONLY the inner loop
# ======================================================


# ======================================================
# EXAMPLE 3: CONTINUE WITH WHILE LOOP
# ------------------------------------------------------

i = 0
while i < 10:
    if i == 5:
        i += 1   # IMPORTANT: increment before continue
        continue

    print(i)
    i += 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - while loop runs while i < 10
# - When i == 5:
#   → continue skips print
#   → i is incremented BEFORE continue
# - Prevents infinite loop
# ======================================================


# ======================================================
# WHEN TO USE CONTINUE STATEMENT?
# ------------------------------------------------------
# ✔ Skip specific values in a loop
# ✔ Filter unwanted data dynamically
# ✔ Avoid unnecessary computations
# ✔ Improve readability over nested if-else
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ continue skips current iteration only
# ✔ continue does NOT terminate the loop
# ✔ continue works in both for and while loops
# ✔ In while loops, increment must be done carefully
# ✔ continue affects only the nearest enclosing loop
#
# Python Loop Control Statements:
# 1. break    → exits loop completely
# 2. continue → skips current iteration
# 3. pass     → does nothing (placeholder)
# ======================================================
