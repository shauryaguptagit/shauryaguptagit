"""
========================================================
SPLIT EVEN AND ODD ELEMENTS INTO TWO DIFFERENT LISTS
========================================================

Problem Statement:
------------------
Given a list of integers, split its elements into:
✔ One list containing even numbers
✔ Another list containing odd numbers

This is a very common problem used to test:
✔ Conditional logic
✔ Loops
✔ List comprehension
✔ Functional programming concepts
"""

# ======================================================
# SAMPLE INPUT
# ======================================================
"""
Input:
------
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected Output:
----------------
Even Numbers: [2, 4, 6, 8, 10]
Odd Numbers : [1, 3, 5, 7, 9]
"""


# ======================================================
# METHOD 1: USING LIST COMPREHENSION (BEST & PYTHONIC)
# ======================================================
"""
This is the most efficient and recommended method.

Advantages:
✔ Short
✔ Fast
✔ Readable
✔ Interview-friendly
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in a if n % 2 == 0]
odds  = [n for n in a if n % 2 != 0]

print("Even Numbers:", evens)
print("Odd Numbers :", odds)

"""
Output:
-------
Even Numbers: [2, 4, 6, 8, 10]
Odd Numbers : [1, 3, 5, 7, 9]
"""


# ======================================================
# METHOD 2: USING filter() FUNCTION
# ======================================================
"""
filter() applies a condition to each element
and keeps only those that satisfy it.

Note:
✔ filter() returns an iterator
✔ Convert it to list explicitly
"""

evens = list(filter(lambda n: n % 2 == 0, a))
odds  = list(filter(lambda n: n % 2 != 0, a))

print("Even Numbers:", evens)
print("Odd Numbers :", odds)


# ======================================================
# METHOD 3: USING FOR LOOP (EXAM & VIVA FRIENDLY)
# ======================================================
"""
This method is best for:
✔ Beginners
✔ Written exams
✔ Step-by-step explanation in viva
"""

evens, odds = [], []

for n in a:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Even Numbers:", evens)
print("Odd Numbers :", odds)


# ======================================================
# METHOD 4: USING WHILE LOOP
# ======================================================
"""
Less commonly used, but useful for understanding
index-based iteration.
"""

evens, odds = [], []
i = 0

while i < len(a):
    if a[i] % 2 == 0:
        evens.append(a[i])
    else:
        odds.append(a[i])
    i += 1

print("Even Numbers:", evens)
print("Odd Numbers :", odds)


# ======================================================
# DRY RUN (FOR LOOP METHOD)
# ======================================================
"""
Initial:
--------
a = [1,2,3,4,5,6,7,8,9,10]
evens = []
odds  = []

Iteration:
----------
1  → odd  → odds  = [1]
2  → even → evens = [2]
3  → odd  → odds  = [1,3]
4  → even → evens = [2,4]
...
10 → even → evens = [2,4,6,8,10]

Final Result:
-------------
Even Numbers: [2, 4, 6, 8, 10]
Odd Numbers : [1, 3, 5, 7, 9]
"""


# ======================================================
# EDGE CASES
# ======================================================
"""
1. Empty list:
   a = [] → evens = [], odds = []

2. All even:
   a = [2,4,6] → odds empty

3. All odd:
   a = [1,3,5] → evens empty

4. Mixed + duplicates:
   a = [2,2,3,3,4] → handled correctly
"""


# ======================================================
# TIME AND SPACE COMPLEXITY
# ======================================================
"""
Time Complexity:
----------------
O(n) → each element checked once

Space Complexity:
-----------------
O(n) → two new lists created
"""


# ======================================================
# METHOD COMPARISON
# ======================================================
"""
Method             | Readability | Speed | Exam Friendly
-------------------|-------------|-------|--------------
List Comprehension | High        | High  | Medium
filter()           | Medium      | High  | Low
For Loop           | Very High   | High  | Best
While Loop         | Medium      | Low   | Medium
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ Modulus operator (%) is key for even/odd checks
✔ List comprehension is the cleanest solution
✔ For-loop is best for theory & viva
✔ Original list remains unchanged
✔ Order of elements is preserved

This problem is widely used in:
✔ Placements
✔ Coding rounds
✔ Data preprocessing
✔ Python fundamentals
"""

"""
End of Even-Odd Split Module
----------------------------
"""
