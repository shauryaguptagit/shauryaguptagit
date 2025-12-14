# 💻 Coding Problem — Swapping Variables in Python
# 🧩 Problem Statement

# You are given two variables x and y with some values assigned earlier in the program.
# Your task is to swap the values of these two variables so that:

# x gets the value originally held by y

# y gets the value originally held by x

# 📥 Given

# Two variables:

# x → integer value

# y → integer value

# 📌 Requirements

# Swap the values of x and y

# Do not lose any value during swapping

# Print the values of x and y **after swapping**

# 🚫 Restrictions

# ❌ Do not hardcode final values

# ❌ Do not use input()

# ✔️ Use variables only

# 🧠 Concepts Tested (from notes)

# Variables as references

# Assignment behavior

# Swapping logic

# Multiple assignment in Python

# 🧪 Example (for understanding only)

# Before swapping

# x = 100
# y = 20


# After swapping

# x = 20
# y = 100

# ✅ Your Task

# 👉 Write a Python program that:

# Initializes x and y

# Swaps them

# Prints the swapped values

# Paste only your code here when done.
# I’ll:

# Check correctness

# Point out logic issues (if any)

# Suggest Pythonic improvement (if applicable)

x = 10
y = 100
print(x,y)
old_X = x
x = y
y = old_X

print(x,y)

x,y = y,x # Tuple unboxing