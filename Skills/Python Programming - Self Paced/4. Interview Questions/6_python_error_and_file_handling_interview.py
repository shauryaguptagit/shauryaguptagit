"""
=========================================================
ERROR HANDLING & FILE HANDLING IN PYTHON
INTERVIEW + VIVA NOTES
=========================================================

Covers:
✔ try-except vs try-except-finally
✔ Multiple exception handling
✔ Exception Groups (Python 3.11)
✔ File read/write modes
✔ assert keyword
✔ with statement
✔ flush() vs close()
✔ Custom exceptions
✔ File-related exceptions
✔ seek(), writelines()
✔ logging & sys.exc_info()
"""


# =========================================================
# Q1. try-except vs try-except-finally
# =========================================================
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
finally:
    print("Finally block always executes")


# =========================================================
# Q2. Catching Multiple Exceptions
# =========================================================
try:
    x = 1 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Caught error:", e)


# =========================================================
# Q3. Deleting a File
# =========================================================
import os

# os.remove("sample.txt")
# os.unlink("sample.txt")


# =========================================================
# Q4. Exception Groups (Python 3.11+)
# =========================================================
try:
    raise ExceptionGroup(
        "Grouped Errors",
        [
            TypeError("Type issue"),
            ValueError("Value issue"),
            KeyError("Key issue"),
        ],
    )
except* TypeError:
    print("Handled TypeError")
except* ValueError:
    print("Handled ValueError")
except* KeyError:
    print("Handled KeyError")


# =========================================================
# Q5. read() vs readline() vs readlines()
# =========================================================
"""
read()       -> Reads entire file as string
readline()   -> Reads one line
readlines()  -> Reads all lines into list
"""


# =========================================================
# Q6. assert Keyword
# =========================================================
assert 2 + 2 == 4
# assert 2 + 2 == 5   # Raises AssertionError


# =========================================================
# Q7. File Modes
# =========================================================
"""
'r'  -> Read
'w'  -> Write
'a'  -> Append
'b'  -> Binary
'x'  -> Exclusive creation
't'  -> Text
'r+' -> Read + Write
'w+' -> Write + Read
'a+' -> Append + Read
"""


# =========================================================
# Q8. with Statement
# =========================================================
with open("example.txt", "w") as f:
    f.write("Using with statement")


# =========================================================
# Q9. flush() vs close()
# =========================================================
f = open("flush_example.txt", "w")
f.write("Flushing content")
f.flush()   # Writes buffer to file
f.close()   # Flush + release resource


# =========================================================
# Q10. Common Built-in Exceptions
# =========================================================
"""
ZeroDivisionError
ValueError
IndexError
FileNotFoundError
TypeError
KeyError
"""


# =========================================================
# Q11. read() vs readlines() (Comparison)
# =========================================================
"""
read()      -> returns string
readlines() -> returns list of strings
"""


# =========================================================
# Q12. Binary vs Text Files
# =========================================================
with open("binary.bin", "wb") as f:
    f.write(b"\x00\x01\x02")


# =========================================================
# Q13. Syntax Errors vs Exceptions
# =========================================================
"""
Syntax Error -> Detected before execution
Exception    -> Occurs during runtime
"""


# =========================================================
# Q14. Custom Exception
# =========================================================
class AgeError(Exception):
    pass


def set_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    print("Age set to", age)


try:
    set_age(-5)
except AgeError as e:
    print(e)


# =========================================================
# Q15. File-related Exception Handling
# =========================================================
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())

except FileNotFoundError as e:
    print("File not found:", e)

except PermissionError as e:
    print("Permission denied:", e)

except IOError as e:
    print("IO error:", e)

except Exception as e:
    print("Unexpected error:", e)

else:
    print("File read successfully")

finally:
    print("File handling completed")


# =========================================================
# Q16. Bare except Block
# =========================================================
try:
    x = int("abc")
except:
    print("Something went wrong (not recommended)")


# =========================================================
# Q17. Writing to a File
# =========================================================
with open("write.txt", "w") as f:
    f.write("Hello World\n")


# =========================================================
# Q18. Ensuring File Closure
# =========================================================
with open("safe.txt", "w") as f:
    f.write("Auto closed file")


# =========================================================
# Q19. seek() Method
# =========================================================
with open("seek.txt", "w+") as f:
    f.write("Hello World")
    f.seek(0)
    print(f.read())


# =========================================================
# Q20. Writing Multiple Lines
# =========================================================
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)


# =========================================================
# Q21. else Block in Exception Handling
# =========================================================
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("No exception occurred")


# =========================================================
# Q22. Logging Exceptions
# =========================================================
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except Exception as e:
    logging.exception("Logged exception")


# =========================================================
# Q23. sys.exc_info()
# =========================================================
import sys

try:
    int("abc")
except:
    print(sys.exc_info())


# =========================================================
# Q24. Order of except Blocks
# =========================================================
try:
    x = int("abc")
except ValueError:
    print("ValueError handled")
except Exception:
    print("Generic exception handled")


# =========================================================
# Q25. Custom Error Messages
# =========================================================
raise ValueError("This is a custom error message")
