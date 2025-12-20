# ======================================================
# MODULE: CONDITIONAL STATEMENTS IN PYTHON
# ======================================================
# THEORY:
# Conditional statements are used to control the flow
# of a program based on certain conditions.
# These conditions evaluate to either True or False.
#
# Python provides the following conditional statements:
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. Nested if-else
# 5. Ternary (short-hand if-else)
# 6. match-case (Python 3.10+)
# ======================================================


# ------------------------------------------------------
# 1. IF STATEMENT
# ------------------------------------------------------
# The if statement executes a block of code
# only if the condition is True.

age = 20
if age >= 18:
    print("IF: Eligible to vote")


# ------------------------------------------------------
# 2. SHORT-HAND IF (Single Line IF)
# ------------------------------------------------------
# Used when there is only one statement to execute.

age = 19
if age > 18: print("SHORT-HAND IF: Eligible to vote")


# ------------------------------------------------------
# 3. IF-ELSE STATEMENT
# ------------------------------------------------------
# if-else allows us to execute one block of code
# when the condition is True and another when it is False.

age = 10
if age <= 12:
    print("IF-ELSE: Travel for free")
else:
    print("IF-ELSE: Pay for ticket")


# ------------------------------------------------------
# 4. SHORT-HAND IF-ELSE (TERNARY OPERATOR)
# ------------------------------------------------------
# This is a compact way to write if-else in a single line.
# Syntax:
# variable = value_if_true if condition else value_if_false

marks = 45
result = "Pass" if marks >= 40 else "Fail"
print("TERNARY OPERATOR:", result)


# ------------------------------------------------------
# 5. IF-ELIF-ELSE STATEMENT
# ------------------------------------------------------
# Used to check multiple conditions.
# The first True condition block gets executed.

age = 25

if age <= 12:
    print("IF-ELIF: Child")
elif age <= 19:
    print("IF-ELIF: Teenager")
elif age <= 35:
    print("IF-ELIF: Young Adult")
else:
    print("IF-ELIF: Adult")


# ------------------------------------------------------
# 6. NESTED IF-ELSE STATEMENT
# ------------------------------------------------------
# Nested if means an if-else inside another if.
# Used when decisions depend on multiple related conditions.

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("NESTED IF: 30% senior discount")
    else:
        print("NESTED IF: 20% senior discount")
else:
    print("NESTED IF: No senior discount")


# ------------------------------------------------------
# 7. TERNARY CONDITIONAL STATEMENT (AGAIN)
# ------------------------------------------------------
# Ternary statements are useful for assigning values
# based on a condition in a clean and readable way.

age = 20
status = "Adult" if age >= 18 else "Minor"
print("TERNARY STATUS:", status)


# ------------------------------------------------------
# 8. MATCH-CASE STATEMENT (Python 3.10+)
# ------------------------------------------------------
# match-case is similar to switch-case in other languages.
# It compares a value against multiple patterns.

number = 2

match number:
    case 1:
        print("MATCH-CASE: One")
    case 2 | 3:
        print("MATCH-CASE: Two or Three")
    case _:
        print("MATCH-CASE: Other number")


# ======================================================
# END OF CONDITIONAL STATEMENTS MODULE
# ======================================================