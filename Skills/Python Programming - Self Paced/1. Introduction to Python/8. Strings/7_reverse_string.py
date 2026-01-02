"""
========================================
HOW TO REVERSE A STRING IN PYTHON
========================================

Overview:
---------
Reversing a string is a very common operation in Python.
It is frequently asked in:
✔ Exams
✔ Interviews
✔ Competitive programming
✔ Basic string manipulation tasks

Python provides multiple ways to reverse a string.
Each method has its own advantages.
"""

# ========================================
# METHOD 1: USING STRING SLICING (BEST METHOD)
# ========================================
"""
Concept:
--------
Python slicing allows extracting parts of a string.

Syntax:
-------
string[start : end : step]

Using step = -1 reverses the string.
"""

s = "GeeksforGeeks"
rev = s[::-1]
print(rev)

"""
Output:
-------
skeeGrofskeeG
"""

"""
Explanation:
------------
- ':' selects the entire string
- '-1' reads the string from right to left
- This is the MOST concise and efficient method
"""


# ========================================
# METHOD 2: USING reversed() AND join()
# ========================================
"""
Concept:
--------
reversed() returns an iterator that accesses
the string in reverse order.

join() is used to combine characters into a string.
"""

s = "GeeksforGeeks"
rev = ''.join(reversed(s))
print(rev)

"""
Output:
-------
skeeGrofskeeG
"""

"""
Explanation:
------------
- reversed(s) → reverse iterator
- ''.join(...) → builds new string
"""


# ========================================
# METHOD 3: USING A LOOP
# ========================================
"""
Concept:
--------
This method builds the reversed string manually.
It provides full control over the reversal process.
"""

s = "GeeksforGeeks"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)

"""
Output:
-------
skeeGrofskeeG
"""

"""
Explanation:
------------
- Loop iterates character by character
- Each character is prepended to the result
"""


# ========================================
# METHOD 4: USING LIST COMPREHENSION + join()
# ========================================
"""
Concept:
--------
Iterate over string indices in reverse order
and collect characters.
"""

s = "GeeksforGeeks"
rev = ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
print(rev)

"""
Output:
-------
skeeGrofskeeG
"""

"""
Explanation:
------------
- range() iterates backwards
- List comprehension collects characters
- join() forms the final string
"""


# ========================================
# METHOD 5: USING STACK (LIST AS STACK)
# ========================================
"""
Concept:
--------
Stack follows LIFO (Last In First Out) principle.
Last character added is removed first.

We simulate a stack using a list.
"""

s = "GeeksforGeeks"

# Convert string into stack
stack = list(s)

rev = ""
while stack:
    rev += stack.pop()

print(rev)

"""
Output:
-------
skeeGrofskeeG
"""

"""
Explanation:
------------
- list(s) converts string to list
- pop() removes last element
- Stack reversal happens naturally
"""

"""
Note:
-----
collections.deque can also be used as a stack
"""


# ========================================
# WHICH METHOD TO CHOOSE?
# ========================================
"""
Comparison:
-----------
Method                | Recommendation
----------------------|-------------------------
Slicing (s[::-1])     | BEST, fastest, cleanest
reversed() + join()   | Readable, pythonic
Loop                  | Good for understanding logic
List comprehension    | Control + compact code
Stack                 | Educational, DSA learning

Final Recommendation:
---------------------
✔ Use slicing in real-world code
✔ Use loop/stack for learning & interviews
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Strings are immutable in Python
2. Reversing creates a new string
3. s[::-1] is the fastest and simplest
4. reversed() returns an iterator
5. Stack approach helps understand LIFO
6. Choose method based on clarity vs performance

String reversal is a foundational problem for:
✔ Logic building
✔ Data structures
✔ Interviews
✔ Python fundamentals
"""

"""
End of Reverse String Module
----------------------------
"""
