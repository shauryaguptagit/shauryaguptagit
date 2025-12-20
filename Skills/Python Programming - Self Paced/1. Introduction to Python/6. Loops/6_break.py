# ======================================================
# MODULE: PYTHON BREAK STATEMENT
# ======================================================
# THEORY:
# ------------------------------------------------------
# The break statement in Python is used to immediately
# terminate a loop (for or while) before it finishes
# all its iterations.
#
# When break is executed:
# ✔ The loop stops instantly
# ✔ Control moves to the statement AFTER the loop
#
# break is commonly used when:
# - Required value is found
# - No further iteration is needed
# - A stopping condition is met dynamically
# ======================================================


# ======================================================
# BASIC EXAMPLE: SEARCHING FOR AN ELEMENT IN A LIST
# ------------------------------------------------------
# Using break with for loop and else block
# ------------------------------------------------------

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print("Not found")

# Output:
# Found at 7!


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Loop iterates over list 'a'
# - When value 7 is found:
#   → Message is printed
#   → break exits the loop immediately
# - else block executes ONLY if loop finishes normally
#   (i.e., without break)
# ======================================================


# ======================================================
# BREAK STATEMENT WITH FOR LOOP
# ------------------------------------------------------
# Loop exits when condition is met
# ------------------------------------------------------

for i in range(10):
    print(i)
    if i == 6:
        break

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - for loop prints numbers from 0
# - When i becomes 6:
#   → break executes
#   → loop stops
# - Numbers after 6 are NOT printed
# ======================================================


# ======================================================
# BREAK STATEMENT WITH WHILE LOOP
# ------------------------------------------------------
# Exiting a loop based on dynamic condition
# ------------------------------------------------------

cnt = 5

while True:
    print(cnt)
    cnt -= 1

    if cnt == 0:
        print("Countdown finished!")
        break

# Output:
# 5
# 4
# 3
# 2
# 1
# Countdown finished!


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - while True creates an infinite loop
# - cnt is reduced each iteration
# - When cnt reaches 0:
#   → message is printed
#   → break stops the loop
# ======================================================


# ======================================================
# BREAK IN NESTED LOOPS
# ------------------------------------------------------
# break exits ONLY the innermost loop
# To exit outer loop also, we use a flag
# ------------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

val = 5
found = False

for row in matrix:
    for num in row:
        if num == val:
            print(f"{val} found!")
            found = True
            break   # Exits inner loop

    if found:
        break       # Exits outer loop

# Output:
# 5 found!


# ======================================================
# EXPLANATION:
# ------------------------------------------------------
# - Nested loops iterate over a 2D list
# - break inside inner loop exits ONLY inner loop
# - Flag variable 'found' is used
# - Second break exits outer loop
# ======================================================


# ======================================================
# IMPORTANT NOTES (EXAM / VIVA POINTS) 🔥
# ------------------------------------------------------
# ✔ break exits the nearest enclosing loop
# ✔ break works in both for and while loops
# ✔ break skips loop else block
# ✔ break does NOT exit multiple loops automatically
# ✔ Flags or functions are used to exit nested loops
#
# Python Jump / Loop Control Statements:
# 1. break    → exits loop
# 2. continue → skips current iteration
# 3. pass     → does nothing (placeholder)
# ======================================================
