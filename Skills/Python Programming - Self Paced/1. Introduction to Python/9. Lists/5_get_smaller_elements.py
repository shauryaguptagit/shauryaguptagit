"""
========================================
GET SMALLER ELEMENTS FROM A LIST
========================================

Problem Statement:
------------------
Given:
✔ A list of integers
✔ An integer x

Task:
-----
Return a new list containing all elements
that are strictly smaller than x.

This is a very common problem used to test:
✔ Looping
✔ Conditional checks
✔ List manipulation
✔ Understanding of filtering logic
"""

# ========================================
# EXAMPLES
# ========================================
"""
Input:
------
arr = [8, 100, 20, 40, 3, 7]
x = 10

Output:
-------
[8, 3, 7]

Explanation:
------------
Elements smaller than 10 are 8, 3, and 7.
"""

"""
Input:
------
arr = [100, 20, 40, 60, 80]
x = 60

Output:
-------
[20, 40]
"""


# ========================================
# METHOD 1: USING LOOP (BASIC & EXAM-FRIENDLY)
# ========================================
"""
This method uses:
✔ for loop
✔ if condition
✔ append()

Best suited for:
✔ Beginners
✔ Exams
✔ Viva explanations
"""

def getSmaller(l, x):
    """
    Returns a list of elements smaller than x.
    """
    res = []
    for e in l:
        if e < x:
            res.append(e)
    return res


# ========================================
# DRIVER CODE
# ========================================

l = [8, 100, 20, 40, 3, 7]
x = 10

print(getSmaller(l, x))

"""
Output:
-------
[8, 3, 7]
"""


# ========================================
# STEP-BY-STEP EXPLANATION (DRY RUN)
# ========================================
"""
Initial values:
---------------
l = [8, 100, 20, 40, 3, 7]
x = 10
res = []

Iteration:
----------
e = 8     → 8 < 10 → append → res = [8]
e = 100   → not < 10 → skip
e = 20    → not < 10 → skip
e = 40    → not < 10 → skip
e = 3     → 3 < 10 → append → res = [8, 3]
e = 7     → 7 < 10 → append → res = [8, 3, 7]

Final result returned.
"""


# ========================================
# METHOD 2: USING LIST COMPREHENSION (PYTHONIC)
# ========================================
"""
This is a shorter and more Pythonic approach.
Useful in:
✔ Clean code
✔ Competitive programming
✔ Interviews (after basic approach)
"""

def getSmaller_comp(l, x):
    return [e for e in l if e < x]

print(getSmaller_comp(l, x))

"""
Output:
-------
[8, 3, 7]
"""


# ========================================
# COMPARISON OF METHODS
# ========================================
"""
Method               | Readability | Interview | Conciseness
---------------------|-------------|-----------|-------------
For loop + append    | High        | Best      | Medium
List comprehension   | Medium      | Good      | Best
"""


# ========================================
# EDGE CASES
# ========================================
"""
1. Empty list:
   l = [], x = 5 → []

2. No smaller elements:
   l = [10, 20], x = 5 → []

3. All elements smaller:
   l = [1, 2, 3], x = 10 → [1, 2, 3]

4. Duplicate values:
   l = [5, 5, 10], x = 6 → [5, 5]
"""


# ========================================
# TIME AND SPACE COMPLEXITY
# ========================================
"""
Time Complexity:
----------------
O(n) → each element is checked once

Space Complexity:
-----------------
O(k) → where k is number of elements < x
"""


# ========================================
# KEY TAKEAWAYS
# ========================================
"""
1. Filtering lists is a very common task
2. Loop + condition is easiest to explain
3. List comprehension is concise and Pythonic
4. Order of elements is preserved
5. Original list remains unchanged

This pattern is widely used in:
✔ Data filtering
✔ Preprocessing
✔ Problem solving
✔ Interview questions
"""

"""
End of Get Smaller Elements Module
----------------------------------
"""
