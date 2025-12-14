# 🧠 Master Coding Problem: Tuple Deep Dive
# 📌 Problem Statement

# You are building a configuration module for a software system.
# Some configurations are fixed and must never change during program execution.

# Create a tuple named config with the following values in order:

# 10, 20, 30, 40, 10


# Perform the following tasks step by step:

# 🔹 Tasks to Perform
# 1️⃣ Print the entire tuple
# 2️⃣ Print:

# First element

# Last element

# Element at index 2

# 3️⃣ Print:

# Length of the tuple

# Number of times 10 appears

# 4️⃣ Print:

# Index of first occurrence of 20

# 5️⃣ Print:

# A slice containing elements from index 1 to 4

# 6️⃣ Check and print:

# Maximum value

# Minimum value

# 7️⃣ Attempt to modify the tuple

# (This should raise an error — comment the line and explain why)

# 8️⃣ Create:

# An empty tuple

# A single-element tuple with value 50

# 9️⃣ Print the type of:

# config

# Empty tuple

# Single-element tuple

# 🧩 Expected Concepts Tested

# ✅ Tuple creation
# ✅ Indexing & negative indexing
# ✅ Slicing
# ✅ len(), count(), index()
# ✅ max() and min()
# ✅ Immutability
# ✅ Single-element tuple syntax
# ✅ type() function

# 💡 Rules

# ❌ Do NOT convert tuple to list

# ❌ Do NOT use any list functions

# ✅ Use only tuple-related operations

# ✍️ Your Task

# 👉 Write the complete Python code that solves all the above tasks.

config = 10, 20, 30, 40, 10

print(config)

print(config[0])
print(config[-1])
print(config[2])

print(len(config))
print(config.count(10))

print(config.index(20))

print(config[1:4])

print(max(config))
print(min(config))

# config[0] = 10

empty = ()
single = (50,)

print(type(config))
print(type(empty))
print(type(single))
