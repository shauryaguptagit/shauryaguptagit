"""
========================================
BASIC STRING OPERATIONS IN PYTHON
========================================

Overview:
---------
Strings are one of the most commonly used data types in Python.
This module covers basic string operations with clear
implementations and explanations.

Operations covered:
1. Accessing characters by index
2. Inserting character/string into a string
3. Modifying character in a string
4. Deleting characters from a string
5. Concatenating strings
6. Finding length of a string
7. Comparing strings for equality
"""

# ========================================
# 1. ACCESSING CHARACTERS BY INDEX
# ========================================
"""
To access a character in a string, we need:
✔ A non-empty string
✔ A valid index (0-based)

Syntax:
--------
character = s[index]
"""

def access_char_by_index(s, k):
    """Returns character at index k"""
    return s[k]

s = "GeeksforGeeks"
k = 4
print("Character at index", k, ":", access_char_by_index(s, k))

"""
Output:
-------
Character at index 4 : s
"""


# ========================================
# 2. INSERTING CHARACTER / STRING INTO A STRING
# ========================================
"""
Strings are immutable in Python.
So insertion creates a NEW string using slicing.

Steps:
------
1. Slice string before index
2. Insert new character/string
3. Append remaining part
"""

def insert_string(s, insert_str, k):
    """Inserts insert_str at index k"""
    return s[:k] + insert_str + s[k:]

s = "GeeksGeeks"
insert_str = "for"
k = 5

print("Original String :", s)
s = insert_string(s, insert_str, k)
print("Modified String :", s)

"""
Output:
-------
Original String : GeeksGeeks
Modified String : GeeksforGeeks
"""


# ========================================
# 3. MODIFYING CHARACTER IN STRING
# ========================================
"""
Since strings are immutable, modification also
creates a NEW string.

Replace character at a given index.
"""

def modify_char(s, index, ch):
    """Replaces character at index with ch"""
    return s[:index] + ch + s[index + 1:]

s = "Geeks Gor Geeks"
index = 6
ch = 'F'

print("Original String =", s)
s = modify_char(s, index, ch)
print("Modified String =", s)

"""
Output:
-------
Original String = Geeks Gor Geeks
Modified String = Geeks For Geeks
"""


# ========================================
# 4. DELETION OF CHARACTER FROM STRING
# ========================================
"""
To delete characters from a string:
- We filter out unwanted characters
- Build a new string

Here we remove ALL occurrences of a character.
"""

def remove_char(s, ch):
    """Removes all occurrences of ch from s"""
    result = ""
    for c in s:
        if c != ch:
            result += c
    return result

s = "geeksforgeeks"
s = remove_char(s, 'g')
print(s)

"""
Output:
-------
eeksforeeks
"""


# ========================================
# 5. CONCATENATING STRINGS
# ========================================
"""
String concatenation means joining strings together.
The '+' operator is used.
"""

init = "this is init"
add = " added now"

init = init + add
print(init)

"""
Output:
-------
this is init added now
"""


# ========================================
# 6. FINDING LENGTH / SIZE OF STRING
# ========================================
"""
Use len() function to find number of characters
in a string (including spaces).
"""

s = "GeeksforGeeks"
print(len(s))

"""
Output:
-------
13
"""


# ========================================
# 7. COMPARING STRINGS FOR EQUALITY
# ========================================
"""
Python provides multiple ways to compare strings:
✔ == operator (most common)
✔ <, > for lexicographical comparison
"""

def compare_strings(s1, s2):
    if s1 == s2:
        print(s1, "is equal to", s2)
    else:
        print(s1, "is not equal to", s2)
        if s1 > s2:
            print(s1, "is greater than", s2)
        else:
            print(s2, "is greater than", s1)

s1 = "geeks"
s2 = "forGeeks"
compare_strings(s1, s2)

s3 = "geeks"
s4 = "geeks"
compare_strings(s3, s4)

"""
Output:
-------
geeks is not equal to forGeeks
geeks is greater than forGeeks
geeks is equal to geeks
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Strings are immutable in Python
2. Indexing starts from 0
3. Insert, modify, delete operations create new strings
4. '+' is used for concatenation
5. len() gives string length
6. '==' compares content of strings
7. Lexicographical comparison follows ASCII order

These operations are fundamental for:
✔ Problem solving
✔ Competitive programming
✔ Interviews
✔ Real-world Python development
"""

"""
End of Basic String Operations Module
-------------------------------------
"""
