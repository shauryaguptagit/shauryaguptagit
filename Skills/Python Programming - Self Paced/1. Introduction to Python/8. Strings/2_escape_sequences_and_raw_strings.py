"""
========================================
ESCAPE SEQUENCES AND RAW STRINGS IN PYTHON
========================================

Overview:
---------
Python strings can contain special characters such as:
✔ New lines
✔ Tabs
✔ Quotes
✔ Backslashes

To handle such characters, Python provides:
1. Escape Sequences
2. Raw Strings

Understanding these concepts is important for:
✔ Text formatting
✔ File paths
✔ Regular expressions
"""

# ========================================
# ESCAPE SEQUENCES
# ========================================
"""
Escape sequences begin with a backslash (\)
followed by a character that defines the behavior.

They allow insertion of characters that are
otherwise difficult to represent.
"""


# ---------- Single Quote (\' ) ----------
"""
Used to include a single quote inside a
single-quoted string.
"""

s = 'welcome to geek\'s course'
print(s)

"""
Output:
-------
welcome to geek's course
"""


# ---------- New Line (\n) ----------
"""
The \\n escape sequence inserts a new line.
"""

s = 'hi\nwelcome to the course'
print(s)

"""
Output:
-------
hi
welcome to the course
"""


# ---------- Tab (\t) ----------
"""
The \\t escape sequence inserts a tab space.
"""

s = 'hi\twelcome to the course'
print(s)

"""
Output:
-------
hi    welcome to the course
"""


# ---------- Double Quote (\") ----------
"""
Used to include double quotes inside a
double-quoted string.
"""

s = "He said, \"Welcome to the course!\""
print(s)

"""
Output:
-------
He said, "Welcome to the course!"
"""


# ---------- Backslash (\\) ----------
"""
To include a backslash itself, it must be escaped
using another backslash.
"""

s = 'This is a backslash: \\'
print(s)

"""
Output:
-------
This is a backslash: \
"""


# ========================================
# RAW STRINGS
# ========================================
"""
Raw strings treat backslashes as literal characters.
Escape sequences are NOT processed.

They are extremely useful for:
✔ File paths
✔ Regular expressions
✔ Strings with many backslashes
"""

# ---------- Creating a Raw String ----------
s1 = r'C:\project\name.py'
print(s1)

"""
Output:
-------
C:\project\name.py
"""

"""
Explanation:
------------
- Prefix 'r' tells Python to ignore escape sequences
- Backslashes are preserved as-is
"""


# ========================================
# ESCAPE STRINGS vs RAW STRINGS
# ========================================
"""
Comparison:
-----------
Escape Strings:
- \\n → new line
- \\t → tab
- \\\" → quote

Raw Strings:
- \\n remains \\n
- \\t remains \\t
- No escape processing
"""

# Example comparison
normal_string = "C:\\project\\name.py"
raw_string = r"C:\project\name.py"

print(normal_string)
print(raw_string)


# ========================================
# IMPORTANT NOTE ABOUT RAW STRINGS
# ========================================
"""
Raw strings CANNOT end with a single backslash.

Example (Invalid):
------------------
r"C:\path\"

This causes a syntax error because the final backslash
escapes the closing quote.
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Escape sequences start with backslash (\\)
2. They help insert special characters in strings
3. Common escapes: \\n, \\t, \\\", \\\'
4. Raw strings disable escape processing
5. Raw strings are ideal for file paths and regex
6. Choose wisely based on use-case

Understanding these concepts is essential for:
✔ File handling
✔ Text formatting
✔ Debugging string-related bugs
"""

"""
End of Escape Sequences and Raw Strings Module
----------------------------------------------
"""
