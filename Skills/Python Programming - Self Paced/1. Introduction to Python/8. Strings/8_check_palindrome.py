"""
========================================
CHECK IF A STRING IS PALINDROME IN PYTHON
========================================

Overview:
---------
A palindrome is a string that reads the same
forward and backward.

Examples:
---------
✔ "madam"     → Palindrome
✔ "malayalam"→ Palindrome
✖ "hello"    → Not a palindrome

This problem is commonly asked in:
✔ Exams
✔ Interviews
✔ Competitive programming
✔ String manipulation practice
"""

# ========================================
# METHOD 1: TWO POINTER TECHNIQUE (BEST LOGIC)
# ========================================
"""
Concept:
--------
Compare characters from both ends of the string
and move towards the center.

Advantages:
-----------
✔ No extra space
✔ Efficient (checks only half the string)
"""

s = "malayalam"

i, j = 0, len(s) - 1
is_palindrome = True

while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes")
else:
    print("No")

"""
Output:
-------
Yes
"""

"""
Explanation:
------------
- Compare s[i] with s[j]
- Move i forward and j backward
- Stop early if mismatch is found
"""


# ========================================
# METHOD 2: USING all() WITH GENERATOR EXPRESSION
# ========================================
"""
Concept:
--------
Check whether all mirrored characters are equal.

Uses:
-----
✔ Generator expression
✔ all() function
"""

s = "malayalam"

if all(s[i] == s[-i - 1] for i in range(len(s) // 2)):
    print("Yes")
else:
    print("No")

"""
Output:
-------
Yes
"""

"""
Explanation:
------------
- range(len(s)//2) → first half indices
- s[-i-1] → mirrored character from end
- all() returns True only if all comparisons pass
"""


# ========================================
# METHOD 3: USING STRING SLICING
# ========================================
"""
Concept:
--------
Reverse the string and compare with original.

This is the simplest and most Pythonic approach.
"""

s = "malayalam"

if s == s[::-1]:
    print("Yes")
else:
    print("No")

"""
Output:
-------
Yes
"""

"""
Explanation:
------------
- s[::-1] reverses the string
- If original == reversed → palindrome
"""


# ========================================
# METHOD 4: USING reversed() + join()
# ========================================
"""
Concept:
--------
Create a reversed copy of the string
using reversed() and join().
"""

s = "geeks"

rev = ''.join(reversed(s))

if s == rev:
    print("Yes")
else:
    print("No")

"""
Output:
-------
No
"""

"""
Explanation:
------------
- reversed(s) → reverse iterator
- join() → constructs reversed string
- Compare with original string
"""


# ========================================
# COMPARISON OF METHODS
# ========================================
"""
Method                      | Space | Speed | Readability
----------------------------|-------|-------|-------------
Two Pointer Technique       | O(1)  | Fast  | Logical
all() + generator           | O(1)  | Fast  | Pythonic
Slicing (s[::-1])           | O(n)  | Fast  | BEST & clean
reversed() + join()         | O(n)  | Medium| Clear
"""


# ========================================
# WHICH METHOD TO USE?
# ========================================
"""
Recommendations:
----------------
✔ Use slicing (s[::-1]) for simplicity
✔ Use two-pointer method for interviews
✔ Use all() for elegant Pythonic code

Interview Tip:
--------------
Explain TWO POINTER method for efficiency,
then mention slicing as a shortcut.
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Palindrome reads same forward and backward
2. Strings are immutable → comparisons only
3. Two-pointer avoids extra space
4. Slicing is shortest and cleanest
5. all() provides functional-style solution

Palindrome checking is important for:
✔ Logic building
✔ Interviews
✔ String algorithms
✔ Competitive programming
"""

"""
End of Palindrome Check Module
------------------------------
"""
