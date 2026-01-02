"""
=========================================================
               PYTHON EXCEPTION HANDLING
=========================================================

Python Exception Handling allows a program to gracefully
handle unexpected runtime errors (like invalid input,
division by zero, missing files) without crashing.

Instead of terminating abruptly, Python detects the
problem, responds to it, and continues execution when
possible.
"""


# =========================================================
# BASIC EXAMPLE: HANDLING A SIMPLE EXCEPTION
# =========================================================
print("\n--- Basic Exception Handling ---")

n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")

"""
Explanation:
- Dividing by zero raises ZeroDivisionError
- try block contains risky code
- except block catches and handles the error
"""


# =========================================================
# DIFFERENCE BETWEEN ERRORS AND EXCEPTIONS
# =========================================================
"""
ERROR:
- Serious issue
- Stops execution
- Cannot be handled
- Example: SyntaxError, MemoryError

EXCEPTION:
- Runtime issue
- Can be handled using try-except
- Example: ZeroDivisionError, ValueError
"""

# Syntax Error Example (commented to avoid crash)
"""
print("Hello world"   # Missing closing parenthesis
"""

# Runtime Exception Example
print("\n--- Runtime Exception Example ---")
try:
    n = 10
    res = n / 0
except ZeroDivisionError:
    print("Runtime exception caught successfully!")


# =========================================================
# SYNTAX OF TRY-EXCEPT-ELSE-FINALLY
# =========================================================
"""
try:
    # risky code
except SomeException:
    # handle exception
else:
    # runs if no exception occurs
finally:
    # always executes
"""


# =========================================================
# try-except-else-finally EXAMPLE
# =========================================================
print("\n--- try-except-else-finally Example ---")

try:
    n = 0
    res = 100 / n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print("Result is", res)
finally:
    print("Execution complete.")

"""
Explanation:
- try: executes risky code
- except: catches specific errors
- else: runs only if no exception occurs
- finally: always runs (cleanup, logging, etc.)
"""


# =========================================================
# CATCHING SPECIFIC EXCEPTIONS
# =========================================================
print("\n--- Catching Specific Exceptions ---")

try:
    x = int("str")   # Causes ValueError
    inv = 1 / x
except ValueError:
    print("Not Valid!")
except ZeroDivisionError:
    print("Zero has no inverse!")

"""
Explanation:
- ValueError raised due to invalid integer conversion
- Specific exception handling improves debugging
"""


# =========================================================
# CATCHING MULTIPLE EXCEPTIONS
# =========================================================
print("\n--- Catching Multiple Exceptions ---")

a = ["10", "twenty", 30]

try:
    total = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error:", e)
except IndexError:
    print("Index out of range.")

"""
Explanation:
- ValueError occurs for 'twenty'
- Multiple exceptions handled in a single block
"""


# =========================================================
# CATCH-ALL EXCEPTION HANDLER (NOT RECOMMENDED)
# =========================================================
print("\n--- Catch-All Exception Example ---")

try:
    res = "100" / 20
except ArithmeticError:
    print("Arithmetic problem.")
except:
    print("Something went wrong!")

"""
WARNING:
- Bare except hides actual error type
- Makes debugging difficult
- Use only as last resort
"""


# =========================================================
# RAISING AN EXCEPTION (raise keyword)
# =========================================================
print("\n--- Raising an Exception ---")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(e)

"""
Explanation:
- raise keyword manually triggers exception
- Prevents invalid data entering program
"""


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================
print("\n--- Custom Exception Example ---")

class AgeError(Exception):
    pass

def set_age_custom(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age_custom(-5)
except AgeError as e:
    print(e)

"""
Explanation:
- Custom exceptions improve clarity
- Useful in large applications
"""


# =========================================================
# ADVANTAGES OF EXCEPTION HANDLING
# =========================================================
"""
✔ Prevents program crash
✔ Cleaner code (less if-else)
✔ Separates error handling from logic
✔ Better debugging with tracebacks
✔ Improves reliability
"""


# =========================================================
# DISADVANTAGES OF EXCEPTION HANDLING
# =========================================================
"""
✘ Performance overhead
✘ Overuse increases complexity
✘ Poor handling may leak sensitive info
"""


# =========================================================
# EXAM / VIVA QUICK NOTES
# =========================================================
"""
✔ try contains risky code
✔ except catches errors
✔ else runs only if no error
✔ finally always executes
✔ raise manually triggers exception
✔ Custom exceptions inherit from Exception
✔ Avoid bare except
"""
