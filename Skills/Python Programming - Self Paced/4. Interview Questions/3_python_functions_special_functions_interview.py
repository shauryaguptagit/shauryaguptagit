"""
=========================================================
FUNCTIONS & SPECIAL FUNCTIONS IN PYTHON (INTERVIEW)
=========================================================

This file covers:
✔ Role of functions & modular programming
✔ Arguments (default, keyword, *args, **kwargs)
✔ Return values & multiple returns
✔ Pass by object reference
✔ Lambda functions
✔ map(), filter(), zip()
✔ Recursion & memoization
✔ Scope (LEGB)
✔ Docstrings & annotations
✔ Decorators (intro)
✔ Debugging basics

Designed for:
• Interviews
• Viva preparation
• Strong conceptual clarity
"""


# =========================================================
# Q1. ROLE OF FUNCTIONS (MODULAR PROGRAMMING)
# =========================================================
"""
Functions divide a program into reusable, independent blocks.
Benefits:
✔ Code reusability
✔ Better readability
✔ Easy debugging & testing
✔ Maintainability
"""


def add(a, b):
    return a + b


# =========================================================
# Q2. RETURNING MULTIPLE VALUES
# =========================================================
def calculate(a, b):
    return a + b, a - b, a * b


s, d, m = calculate(10, 5)
print(s, d, m)


# =========================================================
# Q3. DEFAULT ARGUMENTS
# =========================================================
def greet(name, message="Hello"):
    print(f"{message}, {name}!")


greet("Alice")
greet("Bob", "Hi")


# =========================================================
# Q4. KEYWORD ARGUMENTS
# =========================================================
def greet2(name, message):
    print(f"{message}, {name}!")


greet2(message="Welcome", name="Charlie")


# =========================================================
# Q5. VARIABLE LENGTH ARGUMENTS
# =========================================================
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))


def show_details(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)


show_details(name="Alice", age=21)


# =========================================================
# Q6. PARAMETER PASSING (OBJECT REFERENCE)
# =========================================================
def modify_list(lst):
    lst.append(100)


nums = [1, 2, 3]
modify_list(nums)
print(nums)  # Modified (mutable)


def modify_number(x):
    x += 10


a = 5
modify_number(a)
print(a)  # Not modified (immutable)


# =========================================================
# Q7. map() vs filter()
# =========================================================
nums = [1, 2, 3, 4, 5, 6]

mapped = map(lambda x: x * 2, nums)
filtered = filter(lambda x: x % 2 == 0, nums)

print(list(mapped))
print(list(filtered))


# =========================================================
# Q8. ASCII MANIPULATION
# =========================================================
print(ord('A'))   # ASCII value
print(chr(65))    # Character from ASCII


# =========================================================
# Q9. LAMBDA FUNCTIONS
# =========================================================
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))


# =========================================================
# Q10. FUNCTION WITHOUT RETURN
# =========================================================
def demo():
    pass


print(demo())  # None


# =========================================================
# Q11. FUNCTION RETURNING FUNCTION
# =========================================================
def outer():
    def inner():
        return "Hello from inner"
    return inner


f = outer()
print(f())


# =========================================================
# Q12. RECURSION
# =========================================================
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# =========================================================
# Q13. SCOPE IN PYTHON (LEGB)
# =========================================================
x = 10  # Global


def scope_test():
    x = 5  # Local
    print("Local x:", x)


scope_test()
print("Global x:", x)


# =========================================================
# Q14. DOCSTRINGS
# =========================================================
def square(n):
    """
    Returns square of a number.
    """
    return n * n


print(square.__doc__)


# =========================================================
# Q15. SHALLOW vs DEEP COPY
# =========================================================
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 99
print(original)  # Affected
print(deep)      # Not affected


# =========================================================
# Q16. FUNCTION ANNOTATIONS
# =========================================================
def add_nums(a: int, b: int) -> int:
    return a + b


print(add_nums(3, 4))


# =========================================================
# Q17. HIGHER ORDER FUNCTIONS
# =========================================================
def apply(func, value):
    return func(value)


print(apply(lambda x: x * x, 5))


# =========================================================
# Q18. RECURSION LIMITATIONS
# =========================================================
"""
✔ Python recursion limit ~1000
✔ High memory usage
✔ Slower than loops
"""


# =========================================================
# Q19. MEMOIZATION
# =========================================================
from functools import lru_cache


@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))


# =========================================================
# Q20. DECORATORS (INTRO)
# =========================================================
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorator
def say_hi():
    print("Hi!")


say_hi()


# =========================================================
# Q21. DEBUGGING
# =========================================================
"""
Run in terminal:
python -m pdb script.py
"""


# =========================================================
# Q22. zip() FUNCTION
# =========================================================
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80]

z = zip(names, scores)
print(list(z))


# =========================================================
# Q23. zip() WITH DIFFERENT LENGTHS
# =========================================================
"""
Stops at shortest iterable
"""


# =========================================================
# Q24. filter() vs map()
# =========================================================
nums = [1, 2, 3, 4, 5]

even = filter(lambda x: x % 2 == 0, nums)
square = map(lambda x: x * x, nums)

print(list(even))
print(list(square))


# =========================================================
# Q25. zip vs filter vs map
# =========================================================
"""
zip   → combine iterables
filter→ select elements
map   → transform elements
"""


# =========================================================
# QUICK INTERVIEW SUMMARY
# =========================================================
"""
✔ Functions enable modular programming
✔ Python uses object reference passing
✔ Lambda = short anonymous functions
✔ map/filter/zip return iterators
✔ Recursion uses call stack
✔ Memoization boosts recursion speed
✔ Decorators modify behavior
"""
