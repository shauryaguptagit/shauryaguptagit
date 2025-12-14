# 🧠 ONE Coding Problem (Print + Input – Combined Practice)
# 📌 Problem Statement

# Write a Python program that:

# Takes user name as input

# Takes two numbers as input

# Prints a welcome message using the user’s name

# Prints the two numbers in the format a + b = result

# Uses:

# input() for taking input

# int() for type conversion

# print() with sep and end

# 📝 Expected Output Format
# Welcome <name>
# a + b = result

# 🧪 Example Run

# Input

# Shaurya
# 10
# 20


# Output

# Welcome Shaurya
# 10 + 20 = 30

# 🧩 Constraints

# User input must be taken using input()

# Numbers must be converted properly

# Do not print extra text

# Use sep in at least one print()

# ✏️ Skeleton Code (You Fill It)
# name = input()

# a = int(input())
# b = int(input())

# print("Welcome", name)

# print(a, b, a + b, sep=" + ", end="")


# 👉 Try completing or correcting this so the output exactly matches the expected format.

user_name = input("Enter Username!")
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("Welcome", user_name)
print(f"{a} + {b} = {a+b}")