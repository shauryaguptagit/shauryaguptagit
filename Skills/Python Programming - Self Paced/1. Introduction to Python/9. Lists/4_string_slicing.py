"""
========================================
STRING SLICING IN PYTHON
========================================

Overview:
---------
String slicing in Python allows extracting specific
parts of a string using start, end, and step values.

It is widely used for:
✔ Text manipulation
✔ Data parsing
✔ Pattern extraction
✔ Algorithmic problems

Important:
----------
Strings are IMMUTABLE.
Slicing always returns a NEW string.
"""

# ========================================
# BASIC STRING SLICING EXAMPLE
# ========================================

s = "Hello, Python!"
print(s[0:5])

"""
Output:
-------
Hello
"""

"""
Explanation:
------------
- start = 0 (inclusive)
- end = 5 (exclusive)
- Extracts characters from index 0 to 4
"""


# ========================================
# STRING SLICING SYNTAX
# ========================================
"""
Syntax:
-------
substring = s[start : end : step]

Parameters:
-----------
s     → original string
start → starting index (inclusive), default = 0
end   → ending index (exclusive), default = len(s)
step  → interval between characters, default = 1

Return Type:
------------
✔ Always returns a new string (str)
"""


# ========================================
# USING NEGATIVE INDEXING IN STRING SLICING
# ========================================
"""
Negative indices count from the end:
-1 → last character
-2 → second last character
"""

s = "abcdefghijklmno"

print(s[-4:])        # last 4 characters
print(s[:-3])        # everything except last 3 characters
print(s[-5:-2])      # slice between negative indices
print(s[-8:-1:2])    # slice with step using negatives

"""
Output:
-------
lmno
abcdefghijkl
klm
hjln
"""

"""
Explanation:
------------
s[-4:]       → from 'l' to end
s[:-3]       → start to 'k' (excluding last 3)
s[-5:-2]     → 'k', 'l', 'm'
s[-8:-1:2]   → every 2nd character in range
"""


# ========================================
# REVERSE A STRING USING SLICING
# ========================================
"""
Using step = -1 reverses the string.
"""

s = "Python"
print(s[::-1])

"""
Output:
-------
nohtyP
"""

"""
Explanation:
------------
- start & end omitted → whole string
- step = -1 → traverse backwards
- Original string remains unchanged
"""


# ========================================
# STRING SLICING EXAMPLES
# ========================================

# ----------------------------------------
# EXAMPLE 1: RETRIEVE ALL CHARACTERS
# ----------------------------------------
s = "Hello, World!"

s2 = s[:]
s3 = s[::]

print(s2)
print(s3)

"""
Output:
-------
Hello, World!
Hello, World!
"""

"""
Explanation:
------------
[:] or [::] returns the entire string
"""


# ----------------------------------------
# EXAMPLE 2: BEFORE / AFTER A POSITION
# ----------------------------------------

# From index 7 to end
print(s[7:])

# From start to index 5 (excluding 5)
print(s[:5])

"""
Output:
-------
World!
Hello
"""


# ----------------------------------------
# EXAMPLE 3: BETWEEN TWO POSITIONS
# ----------------------------------------

print(s[1:5])

"""
Output:
-------
ello
"""

"""
Explanation:
------------
- Characters from index 1 to 4
"""


# ----------------------------------------
# EXAMPLE 4: CHARACTERS AT SPECIFIC INTERVALS
# ----------------------------------------

s = "abcdefghi"

# Every second character
print(s[::2])

# Every third character from index 1 to 8
print(s[1:8:3])

"""
Output:
-------
acegi
beh
"""

"""
Explanation:
------------
s[::2]     → skips every alternate character
s[1:8:3]   → step = 3 within defined range
"""


# ========================================
# IMPORTANT NOTES ABOUT STRING SLICING
# ========================================
"""
1. Strings are immutable → slicing never modifies them
2. Slicing always returns a NEW string
3. Out-of-bound slicing is SAFE (no error)
4. start is inclusive, end is exclusive
5. Negative step reverses traversal direction
"""


# ========================================
# STRING SLICING vs INDEXING
# ========================================
"""
Indexing:
---------
✔ Returns a single character
✔ Raises error if index out of range

Slicing:
--------
✔ Returns a substring
✔ Safe for out-of-bound indices
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. String slicing uses start:end:step
2. Defaults make slicing very flexible
3. Negative indices access from end
4. step controls skipping and direction
5. s[::-1] is the easiest way to reverse a string

String slicing is essential for:
✔ Clean Python code
✔ Text processing
✔ Interview questions
✔ Data manipulation tasks
"""

"""
End of String Slicing Module
----------------------------
"""
