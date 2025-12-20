# ======================================================
# MODULE: PYTHON NESTED LOOPS
# ======================================================
# THEORY:
# ------------------------------------------------------
# In Python, there are two main types of loops:
# 1. for loop
# 2. while loop
#
# A NESTED LOOP means a loop inside another loop.
#
# Examples of nested loops:
# - for loop inside for loop
# - while loop inside for loop
# - for loop inside while loop
#
# The INNER LOOP runs completely for every single
# iteration of the OUTER LOOP.
# ======================================================


# ======================================================
# SYNTAX OF PYTHON NESTED LOOPS
# ------------------------------------------------------
# for outer in sequence:
#     for inner in sequence:
#         statements (inner loop)
#     statements (outer loop)
# ======================================================


# ======================================================
# EXAMPLE 1: BASIC NESTED FOR LOOP
# ------------------------------------------------------
# Printing combinations of elements from two lists
# ======================================================

x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)

# Output:
# 1 4
# 1 5
# 2 4
# 2 5


# ======================================================
# SAME EXAMPLE USING NESTED WHILE LOOP
# ======================================================

x = [1, 2]
y = [4, 5]

i = 0
while i < len(x):
    j = 0
    while j < len(y):
        print(x[i], y[j])
        j += 1
    i += 1

# Time Complexity: O(n²)
# Auxiliary Space: O(1)


# ======================================================
# EXAMPLE 2: MULTIPLICATION TABLE USING NESTED FOR LOOPS
# ------------------------------------------------------
# Outer loop selects the table number
# Inner loop prints multiples
# ======================================================

for i in range(2, 4):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()

# Output:
# Table of 2
# Table of 3
#
# Time Complexity: O(n²)
# Auxiliary Space: O(1)


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# Outer loop runs for numbers 2 and 3
# Inner loop runs from 1 to 10
# Multiplication happens as i * j
# ======================================================


# ======================================================
# EXAMPLE 3: MIXED NESTED LOOPS (FOR + WHILE)
# ======================================================

list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

list2_size = len(list2)

for item in list1:
    print("start outer for loop")
    i = 0
    while i < list2_size:
        print(item, list2[i])
        i += 1
    print("end for loop\n")

# Time Complexity: O(n²)
# Auxiliary Space: O(1)


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# Outer for loop iterates over list1
# Inner while loop iterates over list2
# Each item of list2 is printed for every item of list1
# ======================================================


# ======================================================
# USING BREAK STATEMENT IN NESTED LOOPS
# ------------------------------------------------------
# break exits ONLY the nearest enclosing loop
# ======================================================

for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            break
        print(i, "*", j, "=", i * j)
    print()

# Output:
# 2 * 1 = 2
#
# 3 * 1 = 3
# 3 * 2 = 6

# Time Complexity: O(n²)
# Auxiliary Space: O(1)


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# When i == j, break stops the INNER loop
# Outer loop continues execution
# ======================================================


# ======================================================
# USING CONTINUE STATEMENT IN NESTED LOOPS
# ------------------------------------------------------
# continue skips current iteration but does NOT stop loop
# ======================================================

for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            continue
        print(i, "*", j, "=", i * j)
    print()

# Output:
# Skips 2*2 and 3*3

# Time Complexity: O(n²)
# Auxiliary Space: O(1)


# ======================================================
# SINGLE LINE NESTED LOOPS USING LIST COMPREHENSION
# ------------------------------------------------------
# List comprehension can replace nested loops
# ======================================================

list1 = [[j for j in range(3)] for i in range(5)]
print(list1)

# Output:
# [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Time Complexity: O(n²)
# Auxiliary Space: O(n)


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# Inner list: [j for j in range(3)] → [0, 1, 2]
# Outer loop repeats this list 5 times
# List comprehension is faster and compact
# ======================================================


# ======================================================
# IMPORTANT EXAM / VIVA POINTS 🔥
# ------------------------------------------------------
# ✔ Inner loop runs fully for each outer loop iteration
# ✔ break exits only the nearest loop
# ✔ continue skips current iteration only
# ✔ Nested loops increase time complexity
# ✔ Used in matrices, tables, patterns
# ✔ List comprehension is an optimized alternative
#
# Time Complexity:
# Outer loop → n
# Inner loop → m
# Total → O(n × m)
# ======================================================
