"""
========================================
PATTERN SEARCHING IN PYTHON
========================================

Overview:
---------
Pattern searching is a common problem in computer science
where we try to find all occurrences of a smaller string
(pattern) inside a larger string (text).

This is similar to:
✔ Ctrl + F in text editors
✔ Searching keywords in documents
✔ Finding substrings in data processing
"""

# ========================================
# PROBLEM STATEMENT
# ========================================
"""
Given:
------
- A text string (txt)
- A pattern string (pat)

Task:
-----
Find ALL indices where the pattern occurs in the text.

Example:
--------
Text    = "geeks for geeks"
Pattern = "geeks"

Output:
-------
[0, 10]
"""


# ========================================
# BASIC APPROACH USING find()
# ========================================
"""
Python provides the built-in find() method.

Syntax:
-------
string.find(substring, start_index)

Returns:
--------
- Index of first occurrence
- -1 if not found
"""


# ========================================
# IMPLEMENTATION
# ========================================

def pattern_search(txt, pat):
    """
    Finds and prints all occurrences of pat in txt
    using Python's find() method.
    """
    pos = txt.find(pat)

    while pos >= 0:
        print(pos)
        pos = txt.find(pat, pos + 1)


# ========================================
# DRIVER CODE
# ========================================

txt = "geeks for geeks"
pat = "geeks"

print("Pattern found at indices:")
pattern_search(txt, pat)

"""
Output:
-------
0
10
"""


# ========================================
# STEP-BY-STEP EXECUTION EXPLANATION
# ========================================
"""
1. Initialize text and pattern:
   txt = "geeks for geeks"
   pat = "geeks"

2. First find():
   txt.find("geeks") → 0
   pos = 0 → print 0

3. Next find():
   txt.find("geeks", 1) → 10
   pos = 10 → print 10

4. Next find():
   txt.find("geeks", 11) → -1

5. Loop stops when pos becomes -1
"""


# ========================================
# WHY pos + 1 ?
# ========================================
"""
Using pos + 1 ensures:
✔ We continue searching AFTER the current match
✔ Prevents infinite loops
✔ Allows overlapping checks if required
"""


# ========================================
# EDGE CASES
# ========================================
"""
1. Pattern not found:
   find() returns -1 immediately

2. Pattern equals text:
   Output index = 0

3. Empty pattern:
   find("") returns 0 (by definition)

4. Case sensitivity:
   find() is case-sensitive
"""


# ========================================
# IMPROVEMENT: STORE INDICES IN A LIST
# ========================================
"""
Sometimes, instead of printing, we may want
to return all positions.
"""

def pattern_search_list(txt, pat):
    positions = []
    pos = txt.find(pat)

    while pos >= 0:
        positions.append(pos)
        pos = txt.find(pat, pos + 1)

    return positions

print("Positions list:", pattern_search_list(txt, pat))

"""
Output:
-------
Positions list: [0, 10]
"""


# ========================================
# TIME COMPLEXITY
# ========================================
"""
Time Complexity:
----------------
Worst case: O(n * m)
where:
- n = length of text
- m = length of pattern

For basic applications, this method is sufficient.

Advanced algorithms:
--------------------
✔ Naive pattern matching
✔ KMP algorithm
✔ Rabin-Karp
✔ Boyer-Moore
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Pattern searching finds substring occurrences
2. find() returns index or -1
3. Loop until find() returns -1
4. pos + 1 ensures forward progress
5. Useful for searching, filtering, text analysis

Pattern searching is fundamental for:
✔ String processing
✔ Search engines
✔ Text editors
✔ Competitive programming
"""

"""
End of Pattern Searching Module
-------------------------------
"""
