"""
========================================================
FIND AVERAGE (MEAN) OF A LIST IN PYTHON
========================================================

Problem Statement:
------------------
Given a list of numbers, find the average (mean) of its elements.

Definition:
-----------
Average (Mean) = (Sum of all elements) / (Number of elements)

Example:
--------
nums = [10, 20, 30, 40]

Sum   = 10 + 20 + 30 + 40 = 100
Count = 4

Average = 100 / 4 = 25.0
"""

# ======================================================
# METHOD 1: USING BUILT-IN sum() FUNCTION (BEST & SIMPLEST)
# ======================================================
"""
This is the most common and recommended method.

Advantages:
✔ Simple
✔ Readable
✔ Efficient
✔ Exam & interview friendly
"""

a = [2, 4, 6, 8, 10]

avg = sum(a) / len(a)
print(avg)

"""
Output:
-------
6.0
"""

# Explanation:
# sum(a)  → calculates total of elements
# len(a)  → counts number of elements
# sum(a)/len(a) → average


# ======================================================
# METHOD 2: USING FOR LOOP (BASIC & EXAM-FRIENDLY)
# ======================================================
"""
This method is useful when:
✔ Explaining logic step-by-step
✔ Writing answers in theory exams
✔ Understanding how sum() works internally
"""

a = [2, 4, 6, 8, 10]

total = 0
for val in a:
    total += val

avg = total / len(a)
print(avg)

"""
Output:
-------
6.0
"""

# Dry Run:
# total = 0
# 2  → total = 2
# 4  → total = 6
# 6  → total = 12
# 8  → total = 20
# 10 → total = 30
# avg = 30 / 5 = 6.0


# ======================================================
# METHOD 3: USING statistics.mean() (CLEAN & STANDARD)
# ======================================================
"""
Python provides a built-in statistics module.

Best for:
✔ Clean code
✔ Mathematical correctness
✔ Real-world usage
"""

import statistics

a = [2, 4, 6, 8, 10]

avg = statistics.mean(a)
print(avg)

"""
Output:
-------
6
"""

# Note:
# statistics.mean() returns an int if result is whole number,
# otherwise returns float.


# ======================================================
# METHOD 4: USING numpy.average() (DATA SCIENCE FRIENDLY)
# ======================================================
"""
numpy is widely used in:
✔ Data Science
✔ Machine Learning
✔ Numerical Computing
"""

import numpy

a = [2, 4, 6, 8, 10]

avg = numpy.average(a)
print(avg)

"""
Output:
-------
6.0
"""

# Note:
# numpy.average() always returns float


# ======================================================
# EDGE CASES
# ======================================================
"""
1. Empty list:
   a = []
   → sum(a)/len(a) causes ZeroDivisionError

   Solution:
   ----------
   Always check length before calculating average.

2. Single element:
   a = [5] → average = 5

3. Float values:
   a = [1.5, 2.5, 3.5] → works correctly
"""


# ======================================================
# SAFE FUNCTION IMPLEMENTATION
# ======================================================
"""
A reusable function that safely computes average.
"""

def find_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

print(find_average([10, 20, 30]))
print(find_average([]))

"""
Output:
-------
20.0
0
"""


# ======================================================
# TIME AND SPACE COMPLEXITY
# ======================================================
"""
Time Complexity:
----------------
O(n) → each element visited once

Space Complexity:
-----------------
O(1) → no extra space used
"""


# ======================================================
# METHOD COMPARISON
# ======================================================
"""
Method                | Readability | Use Case
----------------------|-------------|----------------------------
sum() / len()         | Very High   | Best general purpose
for loop              | High        | Exams & explanation
statistics.mean()     | Very High   | Math-heavy applications
numpy.average()       | Medium      | Data science & ML
"""


# ======================================================
# KEY TAKEAWAYS
# ======================================================
"""
✔ Average = sum / count
✔ sum() + len() is the most common approach
✔ Always handle empty list case
✔ statistics.mean() is clean and standard
✔ numpy.average() is powerful for numerical data

This concept is used in:
✔ Data analysis
✔ Statistics
✔ Machine learning preprocessing
✔ Interview questions
"""

"""
End of Average of List Module
-----------------------------
"""
