
# 🧪 **ONE Full Coding Problem (Logical Operators)**

# ## 📌 **Problem Statement**

# Write a Python program that:

# 1. Takes **three integers** from the user
# 2. Checks and prints:

#    * If **all numbers are positive**
#    * If **at least one number is zero**
#    * If **none of the numbers are negative**

# ---

# ## 🧪 Example Input

# ```
# 5
# 0
# 8
# ```

# ## ✅ Expected Output

# ```
# All numbers are positive: False
# At least one number is zero: True
# No number is negative: True
# ```

# ---

# ## ✏️ **Skeleton Code (You Solve)**

# ```python
# a = int(input())
# b = int(input())
# c = int(input())

# print("All numbers are positive:", )
# print("At least one number is zero:", )
# print("No number is negative:", )
# ```

# 🔑 Use **and, or, not** properly
# 🔑 Do NOT use loops

# ---

a = int(input())
b = int(input())
c = int(input())

print("All numbers are positive:", a>0 and b>0 and c>0)
print("At least one number is zero:", a==0 or b==0 or c==0)
print("No number is negative:", a>0 and b>0 and c>0)