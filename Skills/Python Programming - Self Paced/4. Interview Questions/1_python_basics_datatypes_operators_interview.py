"""
=========================================================
BASICS OF PYTHON – DATA TYPES & OPERATORS (INTERVIEW Q&A)
=========================================================

This file contains:
✔ Conceptual interview answers
✔ Code examples
✔ Differences & comparisons
✔ Memory & mutability concepts
✔ Operators & precedence

Designed for:
• Interview revision
• Viva preparation
• Quick conceptual recall
"""


# =========================================================
# Q1. WHAT IS PYTHON & ITS FEATURES
# =========================================================
"""
Python is a high-level, interpreted, dynamically typed programming language.

Key Features:
✔ Simple and readable syntax
✔ Interpreted language (line-by-line execution)
✔ Dynamically typed (no explicit type declaration)
✔ Large standard library (NumPy, Pandas, Django, etc.)
✔ Cross-platform support
✔ Object-oriented & functional programming support
"""


# =========================================================
# Q2. PYTHON 2 vs PYTHON 3
# =========================================================
"""
Differences:
1. print
Python 2: print "Hello"
Python 3: print("Hello")

2. Division
Python 2: 5 / 2 = 2
Python 3: 5 / 2 = 2.5

3. Unicode
Python 3 treats strings as Unicode by default

4. Python 2 EOL: 2020
"""

print(5 / 2)   # Python 3 behavior


# =========================================================
# Q3. MEMORY MANAGEMENT
# =========================================================
"""
Python uses:
✔ Private heap
✔ Reference counting
✔ Garbage collection
"""

a = [1, 2, 3]
b = a        # Reference count increases
del a        # Object not deleted as b still references it
print(b)


# =========================================================
# Q4. PEP 8
# =========================================================
"""
PEP 8: Style guide for Python code

✔ 4 spaces indentation
✔ 79 character line limit
✔ Meaningful variable names
✔ Blank lines between functions
"""

def add_numbers(a, b):
    return a + b


# =========================================================
# Q5. PYTHON DATA TYPES
# =========================================================
"""
Numeric: int, float, complex
Sequence: str, list, tuple
Mapping: dict
Set: set, frozenset
Boolean: bool
Binary: bytes, bytearray, memoryview
NoneType: None
"""


# =========================================================
# Q6. LIST vs TUPLE
# =========================================================
my_list = [1, 2, 3]
my_list[0] = 10     # Allowed

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error (Immutable)


# =========================================================
# Q7. STRING vs LIST
# =========================================================
"""
Strings are immutable
Lists are mutable
"""

s = "hello"
# s[0] = "H"  # Error

l = [1, "a", True]
l[0] = 2
print(l)


# =========================================================
# Q8. WALRUS OPERATOR (:=)
# =========================================================
"""
Introduced in Python 3.8
Assigns value inside expression
"""

names = ["Jacob", "Joe", "Jim"]
if (name := "Joe") in names:
    print(f"Hello, {name}!")


# =========================================================
# Q9. INTERPRETER vs COMPILER
# =========================================================
"""
Interpreter:
✔ Executes line by line
✔ Easy debugging

Compiler:
✔ Converts whole program first
✔ Faster execution
"""


# =========================================================
# Q10. SHALLOW COPY vs DEEP COPY
# =========================================================
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
shallow[0][0] = 99
print("Shallow:", original)

deep = copy.deepcopy(original)
deep[0][0] = 100
print("Deep:", original)


# =========================================================
# Q11. MUTABLE vs IMMUTABLE
# =========================================================
"""
Mutable: list, dict, set
Immutable: int, float, str, tuple
"""

mutable_list = [1, 2, 3]
mutable_list[0] = 10

immutable_tuple = (1, 2, 3)
new_tuple = (10,) + immutable_tuple[1:]
print(new_tuple)


# =========================================================
# Q12. BUILT-IN DATA STRUCTURES
# =========================================================
"""
List: Ordered, mutable
Tuple: Ordered, immutable
Set: Unique values
Dict: Key-value pairs
"""


# =========================================================
# Q14. is vs ==
# =========================================================
a = [1, 2]
b = [1, 2]
print(a == b)   # Value equality
print(a is b)   # Memory identity


# =========================================================
# Q15. TYPE CONVERSION
# =========================================================
a = 5 + 2.5     # Implicit
b = int("10")   # Explicit
print(a, b)


# =========================================================
# Q16. NUMERIC DATA TYPES
# =========================================================
x = 10
y = 3.14
z = 3 + 4j
print(x, y, z)


# =========================================================
# Q17. DICTIONARY vs LIST
# =========================================================
d = {"a": 1, "b": 2}
l = [1, 2, 3]
print(d["a"], l[0])


# =========================================================
# Q18. / vs //
# =========================================================
print(7 / 2)   # True division
print(7 // 2)  # Floor division


# =========================================================
# Q19. OPERATOR PRECEDENCE
# =========================================================
result = 2 + 3 * 4
print(result)


# =========================================================
# Q20. LOGICAL vs BITWISE
# =========================================================
print(True and False)
print(5 & 3)


# =========================================================
# Q21. + vs +=
# =========================================================
lst = [1, 2]
lst += [3]

s = "hello"
s += " world"
print(lst, s)


# =========================================================
# Q22. INDENTATION
# =========================================================
"""
Indentation is mandatory in Python.
It defines code blocks.
"""


# =========================================================
# Q23. ESCAPE SEQUENCES
# =========================================================
print("Hello\nWorld")
print("Tab\tSpace")


# =========================================================
# Q24. None vs False vs 0
# =========================================================
print(None == 0)
print(False == 0)


# =========================================================
# Q25. bytes vs bytearray
# =========================================================
b = b"hello"
# b[0] = 72  # Error

ba = bytearray(b"hello")
ba[0] = 72
print(ba)


# =========================================================
# QUICK INTERVIEW REVISION
# =========================================================
"""
✔ Python is interpreted & dynamically typed
✔ Lists are mutable, tuples are immutable
✔ is checks memory, == checks value
✔ // is floor division
✔ Walrus operator assigns inside expressions
✔ bytes immutable, bytearray mutable
"""
