"""
=========================================================
                PYTHON LAMBDA FUNCTIONS
=========================================================

Lambda functions are anonymous functions in Python.
They are defined using the `lambda` keyword instead of `def`.

✔ No function name (anonymous)
✔ Single expression only
✔ Automatically returns the result
✔ Used for short, temporary operations
"""

# =========================================================
# BASIC EXAMPLE
# =========================================================
s1 = "GeeksforGeeks"

# Lambda function to convert string to uppercase
s2 = lambda func: func.upper()

print("\n--- Basic Lambda Example ---")
print(s2(s1))

"""
Explanation:
s2 is a lambda function.
It takes a string as input and returns its uppercase version.
"""


# =========================================================
# SYNTAX OF LAMBDA FUNCTION
# =========================================================
"""
lambda arguments : expression

lambda      -> keyword
arguments   -> input parameters (comma-separated)
expression  -> single expression whose value is returned
"""


# =========================================================
# 1. USING LAMBDA WITH CONDITIONAL CHECKING
# =========================================================
# Positive, Negative or Zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print("\n--- Conditional Lambda ---")
print(n(5))
print(n(-3))
print(n(0))

"""
Explanation:
Nested if-else is used inside lambda.
Returns classification based on value of x.
"""

# Even or Odd check
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print("\n--- Even / Odd Check ---")
print(check(4))
print(check(7))


# =========================================================
# 2. USING LAMBDA WITH LIST COMPREHENSION
# =========================================================
li = [lambda arg=x: arg * 10 for x in range(1, 5)]

print("\n--- Lambda with List Comprehension ---")
for i in li:
    print(i())

"""
Explanation:
Each lambda captures the current value of x.
Multiplies x by 10.
Outputs: 10, 20, 30, 40
"""


# =========================================================
# 3. RETURNING MULTIPLE RESULTS USING LAMBDA
# =========================================================
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)

print("\n--- Lambda Returning Multiple Values ---")
print(res)

"""
Explanation:
Lambda returns a tuple.
First value -> sum
Second value -> product
"""


# =========================================================
# 4. USING LAMBDA WITH filter()
# =========================================================
nums = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, nums)

print("\n--- Lambda with filter() ---")
print(list(even))

"""
Explanation:
Lambda checks if number is even.
filter() keeps elements where condition is True.
"""


# =========================================================
# 5. USING LAMBDA WITH map()
# =========================================================
a = [1, 2, 3, 4]

b = map(lambda x: x * 2, a)

print("\n--- Lambda with map() ---")
print(list(b))

"""
Explanation:
Lambda doubles each element.
map() applies transformation to all items.
"""


# =========================================================
# 6. USING LAMBDA WITH reduce()
# =========================================================
from functools import reduce

a = [1, 2, 3, 4]

b = reduce(lambda x, y: x * y, a)

print("\n--- Lambda with reduce() ---")
print(b)

"""
Explanation:
reduce() applies lambda cumulatively.
Calculates product of all elements.
Result: 24
"""


# =========================================================
# DIFFERENCE BETWEEN lambda AND def
# =========================================================
# Using lambda
sq = lambda x: x ** 2
print("\n--- Lambda vs def ---")
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2

print(sqdef(3))

"""
Explanation:
Both functions return square of a number.
lambda is shorter and anonymous.
def is better for reusable and complex logic.
"""


# =========================================================
# COMPARISON TABLE (EXAM READY)
# =========================================================
"""
Feature            | lambda Function              | def Function
---------------------------------------------------------------
Definition         | Single expression             | Multiple statements
Name               | Anonymous (or assigned)       | Must have a name
Statements         | Only one expression           | Multiple allowed
Return             | Implicit                      | Explicit using return
Docstring          | Not allowed                   | Allowed
Reusability        | Short, temporary use           | Long-term reusable
"""


# =========================================================
# IMPORTANT EXAM / VIVA POINTS
# =========================================================
"""
✔ Lambda functions are anonymous
✔ Can have multiple arguments but one expression
✔ Cannot contain loops or multiple statements
✔ Best used with map(), filter(), reduce()
✔ Faster to write, not meant for complex logic
"""


# =========================================================
# ONE-LINE VIVA ANSWERS
# =========================================================
"""
Q: What is a lambda function?
A: An anonymous function defined using the lambda keyword.

Q: How many expressions can lambda have?
A: Only one expression.

Q: Does lambda need return keyword?
A: No, it returns value automatically.

Q: Where are lambda functions commonly used?
A: With map(), filter() and reduce().
"""
