"""
=========================================================
           ERRORS AND EXCEPTIONS IN PYTHON
=========================================================

Errors are problems in a program that cause it to stop execution.
Exceptions are raised when some internal event disrupts the normal
flow of the program.

✔ Errors usually stop the program
✔ Exceptions can be handled using try-except
✔ Proper exception handling improves program stability
"""

# =========================================================
# TYPES OF ERRORS IN PYTHON
# =========================================================
"""
1. Syntax Errors
2. Logical Errors (Runtime Errors / Exceptions)
"""


# =========================================================
# SYNTAX ERRORS
# =========================================================
"""
Syntax errors occur when Python code does not follow
the grammatical rules of the language.

✔ Detected at compile time
✔ Program does NOT execute
✔ Python points to exact location
"""

# Example 1: Missing colon after if statement
# ❌ This code will produce a SyntaxError

"""
a = 10000
if a > 2999
    print("Eligible")
"""

# Explanation:
# Missing ':' after the if condition causes SyntaxError


# Example 2: Incorrect indentation
# ❌ This code will also produce a SyntaxError

"""
if a < 3:
print("gfg")
"""

# Explanation:
# Python requires proper indentation for code blocks


# =========================================================
# LOGICAL ERRORS (EXCEPTIONS)
# =========================================================
"""
Logical errors allow the program to run but produce
incorrect or unexpected results.

✔ No syntax error
✔ Program executes normally
✔ Output is wrong
✔ Harder to detect
"""

# Example of Logical Error
a = [10, 20, 30, 40, 50]
b = 0

for i in a:
    b += i

res = b / len(a) - 1
print("\nLogical Error Output:", res)

"""
Expected Output: 30
Actual Output: 29.0

Reason:
The formula incorrectly subtracts 1.
Correct formula should be:
b / len(a)
"""


# =========================================================
# COMMON BUILT-IN EXCEPTIONS
# =========================================================
"""
Exception Type        Description
---------------------------------------------
IndexError            Wrong list index accessed
KeyError              Dictionary key not found
NameError             Variable not defined
TypeError             Wrong data type used
ValueError            Correct type but invalid value
ZeroDivisionError     Division by zero
AttributeError        Attribute does not exist
ImportError           Module not found
MemoryError           Program runs out of memory
AssertionError        assert condition fails
"""


# =========================================================
# ERROR HANDLING IN PYTHON
# =========================================================
"""
Python uses:
✔ try
✔ except
✔ finally

to handle runtime exceptions gracefully.
"""


# =========================================================
# try-except-finally EXAMPLE
# =========================================================
print("\n--- try-except-finally Example ---")

try:
    print("code start")
    print(1 / 0)  # Raises ZeroDivisionError

except:
    print("an error occurs")

finally:
    print("GeeksForGeeks")

"""
Explanation:
✔ try block executes risky code
✔ except block handles the error
✔ finally block ALWAYS executes
"""


# =========================================================
# HANDLING SPECIFIC EXCEPTIONS
# =========================================================
print("\n--- Handling Specific Exception ---")

try:
    x = int("abc")   # Raises ValueError
except ValueError:
    print("ValueError occurred")

"""
Explanation:
✔ Catching specific exceptions is better practice
✔ Prevents hiding unexpected errors
"""


# =========================================================
# RAISING CUSTOM EXCEPTIONS
# =========================================================
print("\n--- Raising Custom Exception ---")

try:
    a = 1999
    if a < 2999:
        raise ValueError("please add money")
    else:
        print("Eligible")

except ValueError as e:
    print(e)

"""
Explanation:
✔ raise keyword is used to manually throw exceptions
✔ Custom messages improve clarity
"""


# =========================================================
# WHY USE EXCEPTION HANDLING?
# =========================================================
"""
✔ Prevent program crash
✔ Improve user experience
✔ Handle unexpected inputs
✔ Make debugging easier
✔ Write robust applications
"""


# =========================================================
# IMPORTANT POINTS (EXAM READY)
# =========================================================
"""
✔ Syntax errors occur before execution
✔ Logical errors occur during execution
✔ Exceptions are runtime errors
✔ try-except prevents program termination
✔ finally always executes
✔ raise is used for custom exceptions
"""


# =========================================================
# VIVA / INTERVIEW QUESTIONS
# =========================================================
"""
Q: Difference between error and exception?
A: Errors stop execution, exceptions can be handled.

Q: When is finally block executed?
A: Always, whether exception occurs or not.

Q: Can one try have multiple except blocks?
A: Yes.

Q: What happens if exception is not handled?
A: Program crashes.

Q: Why catch specific exceptions?
A: To avoid masking other errors.
"""
