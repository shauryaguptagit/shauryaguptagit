"""
========================================
STRING COMPARISON IN PYTHON
========================================

Overview:
---------
Python supports several operators and methods to compare strings.
These comparisons can be used to:
✔ Check equality or inequality
✔ Compare alphabetical (lexicographical) order
✔ Perform case-insensitive checks
✔ Verify prefixes and suffixes

Comparison operators supported:
==, !=, <, <=, >, >=
"""

# ========================================
# BASIC STRING COMPARISON EXAMPLE
# ========================================

s1 = "apple"
s2 = "banana"

print(s1 == s2)   # Equality check
print(s1 != s2)   # Inequality check
print(s1 < s2)    # Lexicographical comparison

"""
Output:
-------
False
True
True
"""

"""
Explanation:
------------
- == checks if strings are identical
- != checks if strings are different
- < compares strings alphabetically
"""


# ========================================
# 1. == OPERATOR FOR EQUALITY CHECK
# ========================================
"""
The == operator checks if:
✔ Both strings have the same characters
✔ In the same order
✔ With the same case
"""

s1 = "Python"
s2 = "Python"

print(s1 == s2)

"""
Output:
-------
True
"""

"""
Explanation:
------------
Both strings are exactly the same.
"""


# ========================================
# 2. != OPERATOR FOR INEQUALITY CHECK
# ========================================
"""
The != operator checks whether two strings differ.
"""

s1 = "Python"
s2 = "Java"

print(s1 != s2)

"""
Output:
-------
True
"""

"""
Explanation:
------------
Strings are different, so inequality check returns True.
"""


# ========================================
# 3. LEXICOGRAPHICAL COMPARISON
# ========================================
"""
Lexicographical comparison compares strings
based on alphabetical order (dictionary order).

It uses ASCII/Unicode values internally.
"""

s1 = "apple"
s2 = "banana"

print(s1 < s2)
print(s2 > s1)

"""
Output:
-------
True
True
"""

"""
Explanation:
------------
- "apple" comes before "banana"
- Useful for sorting and ordering strings
"""


# ========================================
# 4. CASE-INSENSITIVE STRING COMPARISON
# ========================================
"""
String comparisons are case-sensitive by default.
To compare strings ignoring case, convert both
strings to lowercase or uppercase.
"""

s1 = "Apple"
s2 = "apple"

print(s1.lower() == s2.lower())

"""
Output:
-------
True
"""

"""
Explanation:
------------
- lower() converts both strings to lowercase
- Comparison becomes case-insensitive
"""


# ========================================
# 5. USING startswith() METHOD
# ========================================
"""
startswith() checks whether a string begins
with a given substring.
"""

s = "hello world"
print(s.startswith("hello"))

"""
Output:
-------
True
"""


# ========================================
# 6. USING endswith() METHOD
# ========================================
"""
endswith() checks whether a string ends
with a given substring.
"""

print(s.endswith("world"))

"""
Output:
-------
True
"""


# ========================================
# COMBINED EXAMPLE
# ========================================
"""
Using comparison methods together is common
in real-world applications.
"""

filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF file detected")

"""
Output:
-------
PDF file detected
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. == checks equality of strings
2. != checks inequality
3. <, >, <=, >= compare lexicographically
4. String comparisons are case-sensitive
5. lower() / upper() enable case-insensitive checks
6. startswith() and endswith() are useful for pattern checks

String comparison is widely used in:
✔ Sorting
✔ Searching
✔ Validation
✔ File handling
✔ Conditional logic
"""

"""
End of String Comparison Module
-------------------------------
"""
