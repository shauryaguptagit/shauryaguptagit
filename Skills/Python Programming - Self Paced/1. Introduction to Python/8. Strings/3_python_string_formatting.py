"""
========================================
PYTHON STRING FORMATTING
========================================

Overview:
---------
String formatting allows us to create dynamic strings by
inserting variables, values, or expressions into strings.

Python provides FIVE main ways to format strings:
1. % Operator (Old-style formatting)
2. format() Method
3. f-Strings (Literal String Interpolation)
4. String Template Class
5. center() Method

This module explains all methods with examples and
compares which approach is best in real-world usage.
"""

# ========================================
# 1. STRING FORMATTING USING % OPERATOR
# ========================================
"""
This is the OLDEST method of string formatting in Python.
It uses the modulo (%) operator.

Common format specifiers:
%s → string
%d → integer
%f → floating-point number
"""

# ---------- Single value insertion ----------
print(
    "The mangy, scrawny stray dog %s gobbled down" % 'hurriedly' +
    " the grain-free, organic dog food."
)

"""
Output:
-------
The mangy, scrawny stray dog hurriedly gobbled down the grain-free, organic dog food.
"""

# ---------- Multiple values insertion ----------
x = 'looked'
print("Misha %s and %s around" % ('walked', x))

"""
Output:
-------
Misha walked and looked around
"""

# ---------- Float precision handling ----------
print('The value of pi is: %5.4f' % (3.141592))

"""
Output:
-------
The value of pi is: 3.1416
"""

# ---------- Multiple format conversion types ----------
variable = 12
string = "Variable as integer = %d \nVariable as float = %f" % (variable, variable)
print(string)

"""
Output:
-------
Variable as integer = 12
Variable as float = 12.000000
"""


# ========================================
# 2. STRING FORMATTING USING format() METHOD
# ========================================
"""
Introduced in Python 3 to handle complex formatting.

Uses curly braces {} as placeholders.
"""

# ---------- Basic formatting ----------
print('We all are {}.'.format('equal'))

"""
Output:
-------
We all are equal.
"""

# ---------- Index-based insertion ----------
print('{2} {1} {0}'.format('directions', 'the', 'Read'))

"""
Output:
-------
Read the directions
"""

# ---------- Keyword-based insertion ----------
print('a: {a}, b: {b}, c: {c}'.format(a=1, b='Two', c=12.3))

"""
Output:
-------
a: 1, b: Two, c: 12.3
"""

# ---------- Reusing inserted objects ----------
print(
    'The first {p} was alright, but the {p} {p} was tough.'.format(p='second')
)

"""
Output:
-------
The first second was alright, but the second second was tough.
"""

# ---------- Float precision with format() ----------
print('The valueof pi is: %1.5f' % 3.141592)
print('The valueof pi is: {0:1.5f}'.format(3.141592))

"""
Output:
-------
The valueof pi is: 3.14159
The valueof pi is: 3.14159
"""


# ========================================
# 3. STRING FORMATTING USING f-STRINGS
# ========================================
"""
Introduced in Python 3.6 (PEP 498).

f-Strings are:
✔ Fast
✔ Readable
✔ Powerful
✔ Most preferred method
"""

# ---------- Basic f-string ----------
name = 'Ele'
print(f"My name is {name}.")

"""
Output:
-------
My name is Ele.
"""

# ---------- Arithmetic expressions ----------
a = 5
b = 10
print(f"He said his age is {2 * (a + b)}.")

"""
Output:
-------
He said his age is 30.
"""

# ---------- Lambda expressions ----------
print(f"He said his age is {(lambda x: x * 2)(3)}")

"""
Output:
-------
He said his age is 6
"""

# ---------- Float precision in f-strings ----------
num = 3.14159
print(f"The valueof pi is: {num:{1}.{5}}")

"""
Output:
-------
The valueof pi is: 3.1416
"""


# ========================================
# 4. STRING TEMPLATE CLASS
# ========================================
"""
Template strings provide simpler and safer substitution.
They are especially useful when:
✔ Strings are user-supplied
✔ Security is a concern

Uses $ placeholders.
"""

from string import Template

n1 = 'Hello'
n2 = 'GeeksforGeeks'

template = Template('$n3 ! This is $n4.')
print(template.substitute(n3=n1, n4=n2))

"""
Output:
-------
Hello ! This is GeeksforGeeks.
"""

"""
Note:
-----
$$ → Escaped dollar sign
"""


# ========================================
# 5. STRING FORMATTING USING center() METHOD
# ========================================
"""
center() returns a new string centered within
a specified width, padded with spaces by default.
"""

string = "GeeksForGeeks!"
width = 30

centered_string = string.center(width)
print(centered_string)

"""
Output:
-------
        GeeksForGeeks!
"""


# ========================================
# COMPARISON OF STRING FORMATTING METHODS
# ========================================
"""
Method        | Use Case
--------------|---------------------------------------
% Operator    | Legacy code, simple formatting
format()     | Complex formatting, Python 3 support
f-Strings    | Best choice (fast, readable, powerful)
Template     | User input, security-sensitive cases
center()     | Alignment and layout formatting
"""


# ========================================
# BEST PRACTICES
# ========================================
"""
Recommendations:
----------------
✔ Use f-strings (Python 3.6+) for most cases
✔ Use Template when handling user-supplied strings
✔ Avoid % operator in new code
✔ Use format() for backward compatibility

f-strings are:
✔ Faster
✔ Cleaner
✔ Easier to read
✔ Support expressions
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Python supports 5 string formatting techniques
2. % formatting is outdated but still used
3. format() improves flexibility
4. f-strings are the modern standard
5. Template strings improve safety
6. center() helps in layout formatting

String formatting is essential for:
✔ Clean output
✔ Logging
✔ User messages
✔ Professional Python code
"""

"""
End of Python String Formatting Module
--------------------------------------
"""
