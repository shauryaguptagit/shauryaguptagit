# ======================================================
# MODULE: PYTHON WHILE LOOP
# ======================================================
# THEORY:
# ------------------------------------------------------
# A while loop in Python is used to repeatedly execute
# a block of code as long as a given condition is True.
#
# Once the condition becomes False, the loop stops
# and execution continues with the next statement
# after the loop.
#
# Syntax:
# while condition:
#     statements
#
# - condition must be a boolean expression
# - statements are executed repeatedly while condition is True
# ======================================================


# ------------------------------------------------------
# BASIC EXAMPLE: WHILE LOOP
# ------------------------------------------------------
# Print "Hello Geek" 3 times
# ------------------------------------------------------

count = 0

while count < 3:
    count = count + 1
    print("Hello Geek")

# Output:
# Hello Geek
# Hello Geek
# Hello Geek


# ======================================================
# HOW WHILE LOOP WORKS
# ------------------------------------------------------
# 1. Condition is checked
# 2. If True → loop body executes
# 3. After execution, condition is checked again
# 4. When condition becomes False → loop exits
# ======================================================


# ------------------------------------------------------
# INFINITE WHILE LOOP (DANGEROUS)
# ------------------------------------------------------
# Condition always remains True
# Loop runs infinitely until program is stopped
# ------------------------------------------------------

# age = 28
# while age > 19:
#     print("Infinite Loop")

# NOTE:
# This loop never ends because age > 19 is always True


# ======================================================
# LOOP CONTROL STATEMENTS
# ------------------------------------------------------
# Python supports the following loop control statements:
# 1. continue
# 2. break
# 3. pass
# ======================================================


# ------------------------------------------------------
# WHILE LOOP WITH CONTINUE
# ------------------------------------------------------
# continue sends control back to the beginning of the loop
# ------------------------------------------------------
# Print all characters except 'e' and 's'
# ------------------------------------------------------

a = "geeksforgeeks"
i = 0

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue   # skips current iteration
    print(a[i])
    i += 1

# Output:
# g
# k
# f
# o
# r
# g
# k


# ------------------------------------------------------
# WHILE LOOP WITH BREAK
# ------------------------------------------------------
# break immediately terminates the loop
# ------------------------------------------------------

a = "geeksforgeeks"
i = 0

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break   # exits the loop completely
    print(a[i])
    i += 1

# Output:
# g


# ------------------------------------------------------
# WHILE LOOP WITH PASS
# ------------------------------------------------------
# pass is a null statement
# It does nothing and is used as a placeholder
# ------------------------------------------------------

a = "geeksforgeeks"
i = 0

while i < len(a):
    i += 1
    pass  # no operation

print("Value of i :", i)

# Output:
# Value of i : 13


# ------------------------------------------------------
# WHILE LOOP WITH ELSE
# ------------------------------------------------------
# else block executes ONLY if loop ends normally
# (i.e., NOT terminated by break)
# ------------------------------------------------------

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break")

# Output:
# 1
# 2
# 3
# 4
# No Break


# ------------------------------------------------------
# WHILE LOOP WITH ELSE + BREAK
# ------------------------------------------------------
# else block will NOT execute if break is used
# ------------------------------------------------------

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")

# Output:
# 1


# ======================================================
# KEY POINTS TO REMEMBER (EXAM IMPORTANT)
# ------------------------------------------------------
# - while loop runs as long as condition is True
# - Infinite loop occurs if condition never becomes False
# - break exits the loop completely
# - continue skips current iteration
# - pass does nothing (used as placeholder)
# - else executes ONLY if loop ends without break
# ======================================================
