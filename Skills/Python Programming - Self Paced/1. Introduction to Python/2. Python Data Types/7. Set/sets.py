# 🧠 Master Coding Problem: Python Sets (Complete Coverage)
# 📌 Problem Statement

# You are building a data-processing module for an analytics system.

# Two datasets are provided:

# One dataset contains even numbers below 10

# Another dataset contains multiples of 3 below 10

# You must use sets to process these datasets efficiently.

# 🔹 Step-by-Step Tasks
# 1️⃣ Create Sets

# Create a set even_set containing:

# 2, 4, 6, 8


# Create a set multiple_3_set containing:

# 3, 6, 9

# 2️⃣ Print Both Sets

# (Observe that order is not guaranteed)

# 3️⃣ Add & Update

# Add 10 to even_set

# Try adding 6 again to even_set

# Update even_set using a list containing [12, 14]

# 4️⃣ Membership Check

# Check whether 6 is present in even_set

# Check whether 15 is present in even_set

# 5️⃣ Removal Operations

# Use discard() to remove 4

# Use remove() to remove 8

# Safely try removing 100 (avoid crash)

# 6️⃣ Set Operations

# Print results of:

# Union

# Intersection

# Difference (even_set - multiple_3_set)

# Symmetric Difference

# 7️⃣ Relationship Checks

# Print results of:

# isdisjoint

# issubset

# issuperset

# 8️⃣ Clear vs Delete

# Clear multiple_3_set

# Add one element after clearing

# Delete even_set completely

# 9️⃣ Empty Set Creation

# Create an empty set correctly

# Print its type

# 🧩 Concepts Covered (All from Your Notes)

# ✅ Set creation
# ✅ Distinct elements
# ✅ Unordered nature
# ✅ add(), update()
# ✅ in operator
# ✅ discard() vs remove()
# ✅ union, intersection
# ✅ difference, symmetric_difference
# ✅ isdisjoint, issubset, issuperset
# ✅ clear() vs del
# ✅ Empty set creation
# ✅ type()

# 🚫 Rules

# ❌ No lists for operations (except update)

# ❌ No indexing

# ❌ No sorting

# ✅ Use only set operations

# ✍️ Your Task

# 👉 Write the full Python code solving all steps above.

even_set = {2, 4, 6, 8}
multiple_3_set = {3, 6, 9}

print(even_set)
print(multiple_3_set)

even_set.add(10)
even_set.add(6)
even_set.update([12,14])

print(6 in even_set)
print(15 in even_set)

even_set.discard(4)
even_set.remove(8)

print(even_set | multiple_3_set)
print(even_set & multiple_3_set)
print(even_set - multiple_3_set)
print(even_set ^ multiple_3_set)

print(even_set.isdisjoint(multiple_3_set))
print(even_set.issubset(multiple_3_set))
print(even_set.issuperset(multiple_3_set))

multiple_3_set.clear()
multiple_3_set.add(10)
del even_set

empty_set = set()
print(type(empty_set))