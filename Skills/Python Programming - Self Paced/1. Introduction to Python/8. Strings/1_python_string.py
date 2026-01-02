"""
========================================
PYTHON STRING
========================================

Overview:
---------
A string in Python is a sequence of characters enclosed
within quotes. It can contain:
✔ Letters
✔ Numbers
✔ Symbols
✔ Spaces

Python does NOT have a separate character data type.
Even a single character is treated as a string of length 1.

Strings are widely used for:
✔ Text processing
✔ User input/output
✔ Data manipulation
"""

# ========================================
# CREATING A STRING
# ========================================
"""
Strings can be created using:
1. Single quotes (' ')
2. Double quotes (" ")

Both behave exactly the same.
"""

s1 = 'GfG'   # single quote
s2 = "GfG"   # double quote

print(s1)
print(s2)

"""
Output:
-------
GfG
GfG
"""


# ========================================
# MULTI-LINE STRINGS
# ========================================
"""
Multi-line strings use triple quotes:
- ''' ... '''
- \"\"\" ... \"\"\"

Newlines are preserved.
"""

s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

"""
Output:
-------
I am Learning
Python String on GeeksforGeeks
I'm a 
Geek
"""


# ========================================
# ACCESSING CHARACTERS IN STRING
# ========================================
"""
Strings are INDEXED sequences.

Positive Indexing:
- Starts from 0 (left to right)

Negative Indexing:
- Starts from -1 (right to left)
"""

s = "GeeksforGeeks"

print(s[0])   # first character
print(s[4])   # 5th character

"""
Output:
-------
G
s
"""

"""
Note:
-----
- Accessing out-of-range index → IndexError
- Only integers are allowed as indices
"""


# ---------- Negative Indexing ----------

print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end

"""
Output:
-------
k
G
"""


# ========================================
# STRING SLICING
# ========================================
"""
Slicing extracts a part of the string.

Syntax:
-------
string[start : end]

- start → included
- end → excluded
"""

s = "GeeksforGeeks"

print(s[1:4])    # index 1 to 3
print(s[:3])     # start to index 2
print(s[3:])     # index 3 to end
print(s[::-1])   # reverse string

"""
Output:
-------
eek
Gee
ksforGeeks
skeeGrofskeeG
"""


# ========================================
# STRING ITERATION
# ========================================
"""
Strings are iterable.
Each character can be accessed using a loop.
"""

s = "Python"

for char in s:
    print(char)

"""
Output:
-------
P
y
t
h
o
n
"""


# ========================================
# STRING IMMUTABILITY
# ========================================
"""
Strings are IMMUTABLE.
Once created, they cannot be modified.

Any "change" creates a NEW string.
"""

s = "geeksforGeeks"
s = "G" + s[1:]   # new string created
print(s)

"""
Output:
-------
GeeksforGeeks
"""


# ========================================
# DELETING A STRING
# ========================================
"""
Individual characters cannot be deleted,
but the entire string variable can be deleted
using 'del'.
"""

s = "GfG"
del s

"""
Note:
-----
Accessing 's' after deletion will raise NameError
"""


# ========================================
# UPDATING A STRING
# ========================================
"""
Updates are done by creating new strings
using slicing or string methods.
"""

s = "hello geeks"

s1 = "H" + s[1:]                          # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word

print(s1)
print(s2)

"""
Output:
-------
Hello geeks
hello GeeksforGeeks
"""


# ========================================
# COMMON STRING METHODS
# ========================================

# ---------- len() ----------
s = "GeeksforGeeks"
print(len(s))

"""
Output:
-------
13
"""

# ---------- upper() and lower() ----------
s = "Hello World"
print(s.upper())
print(s.lower())

"""
Output:
-------
HELLO WORLD
hello world
"""

# ---------- strip() and replace() ----------
s = "   Gfg   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))

"""
Output:
-------
Gfg
Python is awesome
"""


# ========================================
# CONCATENATING STRINGS
# ========================================
"""
Strings can be concatenated using '+' operator.
"""

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

"""
Output:
-------
Hello World
"""


# ========================================
# REPEATING STRINGS
# ========================================
"""
Strings can be repeated using '*' operator.
"""

s = "Hello "
print(s * 3)

"""
Output:
-------
Hello Hello Hello
"""


# ========================================
# FORMATTING STRINGS
# ========================================

# ---------- Using f-strings ----------
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

"""
Output:
-------
Name: Alice, Age: 22
"""

# ---------- Using format() ----------
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

"""
Output:
-------
My name is Alice and I am 22 years old.
"""


# ========================================
# STRING MEMBERSHIP TESTING
# ========================================
"""
'in' keyword checks whether a substring
exists inside a string.
"""

s = "GeeksforGeeks"

print("Geeks" in s)
print("GfG" in s)

"""
Output:
-------
True
False
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Strings are sequences of characters
2. Strings are immutable
3. Indexing starts from 0
4. Negative indexing accesses from end
5. Slicing extracts substrings
6. Strings support iteration
7. Many built-in methods simplify text handling
8. f-strings are the most preferred formatting method

Strings are fundamental for:
✔ Text processing
✔ User interaction
✔ File handling
✔ Real-world Python applications
"""

"""
End of Python String Module
---------------------------
"""
