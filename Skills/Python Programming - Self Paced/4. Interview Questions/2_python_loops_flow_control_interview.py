"""
=========================================================
LOOPS & FLOW CONTROL IN PYTHON (INTERVIEW QUESTIONS)
=========================================================

This file covers:
✔ for & while loops
✔ break, continue, else
✔ range(), enumerate(), zip()
✔ iter() and next()
✔ Short-circuiting
✔ Nested loops & performance
✔ Common loop errors
✔ Pattern problems

Designed for:
• Interviews
• Viva preparation
• Conceptual clarity + execution
"""


# =========================================================
# Q1. INFINITE LOOP
# =========================================================
"""
An infinite loop occurs when the loop termination condition
is never met.

Common in while loops.
"""

# while True:
#     print("Infinite Loop")  # Avoid running this


# =========================================================
# Q2. FOR LOOP vs WHILE LOOP
# =========================================================
"""
for loop:
✔ Used with iterables
✔ Known number of iterations

while loop:
✔ Condition-based
✔ Unknown number of iterations
"""


# =========================================================
# Q3. range() FUNCTION
# =========================================================
"""
range(stop)
range(start, stop)
range(start, stop, step)
"""

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9


# =========================================================
# Q4. range() vs xrange()
# =========================================================
"""
Python 3:
✔ xrange removed
✔ range behaves like xrange (lazy evaluation)

Python 2:
range -> list
xrange -> generator
"""


# =========================================================
# Q5. break STATEMENT
# =========================================================
for i in range(5):
    if i == 3:
        break
    print(i)


# =========================================================
# Q6. break vs continue
# =========================================================
for i in range(5):
    if i == 2:
        continue
    print(i)


# =========================================================
# Q7. ITERATING NON-SEQUENTIAL DATA
# =========================================================
data = {'a': 1, 'b': 2}
for key in data:
    print(key)


# =========================================================
# Q8. COMMON LOOP ERRORS
# =========================================================
"""
✔ Infinite loops
✔ Modifying list while iterating
✔ Off-by-one errors
✔ Wrong indentation
"""


# =========================================================
# Q9. NESTED LOOPS
# =========================================================
for i in range(3):
    for j in range(2):
        print(i, j)


# =========================================================
# Q10. MULTIPLICATION TABLE
# =========================================================
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()


# =========================================================
# Q11. ITERATE DICTIONARY (KEY + VALUE)
# =========================================================
my_dict = {'a': 1, 'b': 2}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# =========================================================
# Q12. iter() vs next()
# =========================================================
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))


# =========================================================
# Q13. ITERATE MULTIPLE SEQUENCES
# =========================================================
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for x, y in zip(list1, list2):
    print(x, y)


# =========================================================
# Q14. TYPES OF FOR LOOPS
# =========================================================
"""
✔ Sequence iteration
✔ range-based
✔ enumerate
"""

for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)


# =========================================================
# Q15. for-else CONSTRUCT
# =========================================================
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break")


# =========================================================
# Q16. SHORT-CIRCUITING
# =========================================================
x = 0
if x != 0 and (10 / x) > 1:
    print("Condition met")
else:
    print("Short-circuited safely")


# =========================================================
# Q17. is vs ==
# =========================================================
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)


# =========================================================
# Q18. FIRST OCCURRENCE IN LIST
# =========================================================
lst = [1, 2, 3, 4, 5]
for i, val in enumerate(lst):
    if val == 3:
        print(f"Found 3 at index {i}")
        break


# =========================================================
# Q19. ERRORS WHILE ITERATING
# =========================================================
"""
IndexError – invalid index
ValueError – invalid operation
"""


# =========================================================
# Q20. PYRAMID PATTERN
# =========================================================
def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

print_pyramid(5)


# =========================================================
# Q21. for LOOP vs while LOOP (BENEFITS)
# =========================================================
"""
for loop:
✔ Cleaner
✔ Safer
✔ Preferred for known ranges

while loop:
✔ Flexible
✔ Risk of infinite loop
"""


# =========================================================
# Q22. CONDITIONAL EXPRESSIONS (TERNARY)
# =========================================================
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)


# =========================================================
# Q23. TERMINATION CONDITION
# =========================================================
"""
for → automatic termination
while → manual condition check
"""


# =========================================================
# Q24. PITFALLS OF break
# =========================================================
"""
✔ Early termination
✔ Hard-to-follow nested logic
✔ Debugging difficulty

Solutions:
✔ Clear conditions
✔ Flags
✔ Function returns
"""


# =========================================================
# Q25. NESTED LOOP PERFORMANCE
# =========================================================
"""
Nested loops → O(n²)

Optimizations:
✔ Reduce inner work
✔ Use sets/dicts
✔ Algorithm redesign
"""


# =========================================================
# QUICK INTERVIEW SUMMARY
# =========================================================
"""
✔ for loops → iterable-based
✔ while loops → condition-based
✔ break exits loop
✔ continue skips iteration
✔ for-else runs only if no break
✔ Short-circuiting prevents errors
✔ Nested loops affect performance
"""
