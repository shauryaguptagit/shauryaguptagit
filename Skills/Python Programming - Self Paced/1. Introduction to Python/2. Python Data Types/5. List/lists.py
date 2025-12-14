# 🧠 MASTER CODING PROBLEM — Python Lists (Complete Coverage)
# 📌 Problem Title

# Student Score Manager

# 🧩 Problem Statement

# You are writing a small module for managing student scores using Python lists.

# You are given an initial list of scores. Using this list, perform multiple operations to demonstrate your understanding of:

# List creation

# Indexing (positive & negative)

# append, insert

# in operator

# count, index

# remove, pop, del

# max, min, sum

# reverse, sort

# Safe handling of operations

# 📥 Initial Data (Must use exactly this)
# scores = [10, 20, 30, 40, 30]

# 🛠️ Tasks (ALL mandatory)

# Print the original list

# Print:

# Element at index 3

# Last element using negative indexing

# Append the value 30 to the list

# Insert the value 15 at index 1

# Check whether 30 is present in the list and print the result

# Print how many times 30 occurs

# Print the index of the first occurrence of 30

# ⚠️ Do this safely (avoid errors)

# Remove the value 20 safely (only if present)

# Pop the last element and print the popped value

# Pop the element at index 2 and print the popped value

# Delete the element at index 1 using del

# Delete a range of elements using del

# Print:

# Maximum score

# Minimum score

# Sum of scores

# Reverse the list

# Sort the list in ascending order

# Print the final list

# 🚫 Rules

# ❌ Do NOT hardcode final outputs

# ❌ Do NOT use input()

# ❌ Do NOT use extra data structures

# ✅ Use only list operations discussed in notes

# 🎯 What This Tests

# ✔ Indexing
# ✔ Mutability
# ✔ Membership testing
# ✔ Safe list operations
# ✔ Built-in list functions
# ✔ Real-world sequence manipulation

# 📤 Your Response Format

# Paste only your Python code

# No explanation needed

# I will:

# Validate logic

# Catch unsafe operations

scores = [10, 20, 30, 40, 30]

print(scores)
print(scores[3])
print(scores[-1])
scores.append(30)
scores.insert(1,15)
print(30 in scores)
print(scores.count(30))
print(scores.index(30))
if 20 in scores:
    scores.remove(20)
print(scores.pop())
print(scores.pop(2))
del scores[1]
del scores[0:2]

print(max(scores))
print(min(scores))
print(sum(scores))

scores.reverse()
scores.sort()
print(scores)