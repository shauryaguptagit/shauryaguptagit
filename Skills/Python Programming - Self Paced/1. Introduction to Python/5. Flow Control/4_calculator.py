# ======================================================
# PROGRAM: SIMPLE CALCULATOR USING CONDITIONAL STATEMENTS
# ======================================================
# THEORY:
# A calculator program performs arithmetic operations
# based on the user's choice.
#
# In this program, we support:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
#
# The program follows these steps:
# 1. Display a menu of operations
# 2. Take user choice
# 3. Validate the choice
# 4. Take two numbers as input
# 5. Perform the selected operation
# 6. Display the result
#
# If the user enters an invalid choice,
# the program exits with an error message.
# ======================================================

import sys   # Used to exit the program when input is invalid


# ------------------------------------------------------
# DISPLAY MENU
# ------------------------------------------------------
print("""
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
""")


# ------------------------------------------------------
# READ USER'S CHOICE
# ------------------------------------------------------
choice = int(input("Select operation from 1, 2, or 3: "))

# Validate the choice
if choice not in (1, 2, 3):
    print("Invalid choice")
    sys.exit()   # Terminates the program


# ------------------------------------------------------
# TAKE INPUT NUMBERS
# ------------------------------------------------------
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# ------------------------------------------------------
# PERFORM CALCULATION USING IF-ELIF-ELSE
# ------------------------------------------------------
if choice == 1:
    # Addition
    result = num1 + num2

elif choice == 2:
    # Subtraction
    result = num1 - num2

else:
    # Multiplication
    result = num1 * num2


# ------------------------------------------------------
# DISPLAY RESULT
# ------------------------------------------------------
print("The result is:", result)


# ======================================================
# EXAMPLE EXECUTION (FOR UNDERSTANDING)
# ------------------------------------------------------
# Choice = 3 (Multiplication)
# num1 = 3
# num2 = 7
#
# Output:
# The result is: 21
#
# ======================================================
# CONCLUSION:
# ------------------------------------------------------
# - if-elif-else controls program flow
# - sys.exit() safely stops execution on invalid input
# - Menu-driven programs are common real-world use cases
# - This program demonstrates conditional statements clearly
# ======================================================