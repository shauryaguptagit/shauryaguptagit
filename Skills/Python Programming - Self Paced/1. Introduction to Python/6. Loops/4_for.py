# ======================================================
# MODULE: PYTHON FOR LOOPS
# ======================================================
# THEORY:
# ------------------------------------------------------
# Python for loops are used to iterate over sequences
# such as:
# - lists
# - tuples
# - strings
# - ranges
#
# A for loop:
# ✔ Applies the same operation to every element
# ✔ Avoids manual index handling
# ✔ Works with any iterable object
# ✔ Is collection-based (not condition-based like while)
# ======================================================


# ======================================================
# BASIC FOR LOOP EXAMPLE (ITERATING OVER A LIST)
# ------------------------------------------------------

s = ["Geeks", "for", "Geeks"]

# Using for loop with list
for i in s:
    print(i)

# Output:
# Geeks
# for
# Geeks


# ======================================================
# SYNTAX OF FOR LOOP
# ------------------------------------------------------
# for variable in iterable:
#     statements
# ------------------------------------------------------
# NOTE:
# - for loop works only with iterables
# - iterable can be list, tuple, string, range, etc.
# ======================================================


# ======================================================
# FOR LOOP WITH STRING
# ------------------------------------------------------
# Iterating over each character in a string
# ------------------------------------------------------

s = "Geeks"
for ch in s:
    print(ch)

# Output:
# G
# e
# e
# k
# s


# ======================================================
# USING range() WITH FOR LOOP
# ------------------------------------------------------
# range(start, stop, step)
# ------------------------------------------------------

for i in range(0, 10, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8


# ======================================================
# CONTROL STATEMENTS WITH FOR LOOP
# ======================================================


# ------------------------------------------------------
# CONTINUE STATEMENT
# ------------------------------------------------------
# continue skips the current iteration
# and moves to the next iteration
# ------------------------------------------------------

# Prints all letters except 'e' and 's'
for i in "geeksforgeeks":
    if i == 'e' or i == 's':
        continue
    print(i)

# Output:
# g
# k
# f
# o
# r
# g
# k


# ------------------------------------------------------
# BREAK STATEMENT
# ------------------------------------------------------
# break terminates the loop immediately
# ------------------------------------------------------

for i in "geeksforgeeks":
    if i == 'e' or i == 's':
        break

print(i)

# Output:
# e


# ------------------------------------------------------
# PASS STATEMENT
# ------------------------------------------------------
# pass is used for empty loops
# ------------------------------------------------------

for i in "geeksforgeeks":
    pass

print(i)

# Output:
# s


# ======================================================
# ELSE WITH FOR LOOP
# ------------------------------------------------------
# else block executes ONLY IF
# the loop is NOT terminated by break
# ------------------------------------------------------

for i in range(1, 4):
    print(i)
else:
    print("No Break\n")

# Output:
# 1
# 2
# 3
# No Break


# ======================================================
# ENUMERATE WITH FOR LOOP
# ------------------------------------------------------
# enumerate() provides index + value together
# ------------------------------------------------------

li = ["eat", "sleep", "repeat"]

for index, value in enumerate(li):
    print(index, value)

# Output:
# 0 eat
# 1 sleep
# 2 repeat


# ======================================================
# NESTED FOR LOOPS
# ------------------------------------------------------
# One for loop inside another
# Inner loop runs completely for each
# iteration of outer loop
# ------------------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


# ======================================================
# KEY EXAM POINTS 🔥
# ------------------------------------------------------
# ✔ for loop is collection-based iteration
# ✔ No index handling required manually
# ✔ Works with list, tuple, string, range
# ✔ continue → skips iteration
# ✔ break → exits loop
# ✔ pass → empty loop
# ✔ else executes only if no break occurs
# ✔ enumerate gives index + value
# ✔ Nested loops repeat inner loop fully
# ======================================================
