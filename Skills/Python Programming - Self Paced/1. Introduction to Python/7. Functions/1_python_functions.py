"""
========================================
PYTHON FUNCTIONS
========================================

Definition:
------------
Python functions are blocks of reusable code that perform a specific task.
The main idea behind using functions is to avoid repetition of code.
Instead of writing the same logic again and again, we define it once
and reuse it by calling the function whenever required.

Benefits of Functions:
----------------------
1. Code Reusability – Write once, use multiple times.
2. Modularity – Break large programs into smaller logical parts.
3. Readability – Improves understanding of the program.
4. Easy Maintenance – Changes can be made at one place.
5. Reduced Errors – Less duplicate code means fewer bugs.
"""

# ========================================
# DEFINING A FUNCTION
# ========================================
"""
In Python, functions are defined using the 'def' keyword.
A function may or may not take parameters.
The function body contains statements that define what the function does.
"""

def fun():
    """This function prints a welcome message"""
    print("Welcome to GFG")


# ========================================
# CALLING A FUNCTION
# ========================================
"""
After defining a function, we can execute it by calling the function name
followed by parentheses.
"""

fun()   # Function call


# ========================================
# FUNCTION ARGUMENTS
# ========================================
"""
Arguments are values passed to a function when it is called.
A function can accept zero or more arguments.
"""

def evenOdd(x):
    """Checks whether a number is even or odd"""
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


# ========================================
# TYPES OF FUNCTION ARGUMENTS
# ========================================

# ----------------------------------------
# 1. DEFAULT ARGUMENTS
# ----------------------------------------
"""
Default arguments assume a value if no value is provided during function call.
"""

def myFun(x, y=50):
    print("x:", x)
    print("y:", y)

myFun(10)     # y takes default value


# ----------------------------------------
# 2. KEYWORD ARGUMENTS
# ----------------------------------------
"""
Keyword arguments allow passing values by parameter name.
Order of arguments does not matter.
"""

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# ----------------------------------------
# 3. POSITIONAL ARGUMENTS
# ----------------------------------------
"""
In positional arguments, values are assigned based on their position.
Wrong order may lead to logical errors.
"""

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")   # Logical mismatch


# ----------------------------------------
# 4. ARBITRARY ARGUMENTS (*args, **kwargs)
# ----------------------------------------
"""
Arbitrary arguments allow passing a variable number of values.

*args   -> Non-keyword variable length arguments (tuple)
**kwargs -> Keyword variable length arguments (dictionary)
"""

def myFunArgs(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFunArgs('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


# ========================================
# FUNCTION WITHIN FUNCTION (NESTED FUNCTION)
# ========================================
"""
A function defined inside another function is called a nested or inner function.
Inner functions can access variables of the outer function.
"""

def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
    
    f2()

f1()


# ========================================
# ANONYMOUS FUNCTIONS (LAMBDA)
# ========================================
"""
Anonymous functions are functions without a name.
They are defined using the 'lambda' keyword.
Used for short, simple operations.
"""

def cube(x):
    return x * x * x

cube_l = lambda x: x * x * x

print(cube(7))
print(cube_l(7))


# ========================================
# RETURN STATEMENT
# ========================================
"""
The return statement ends the function execution
and sends a value back to the caller.
"""

def square_value(num):
    """Returns square of a number"""
    return num ** 2

print(square_value(2))
print(square_value(-4))


# ========================================
# PASS BY REFERENCE vs PASS BY VALUE
# ========================================
"""
Python uses 'pass-by-object-reference'.

Mutable objects (list, dict, set):
- Changes inside function affect original object.

Immutable objects (int, float, string, tuple):
- Original value remains unchanged.
"""

# Mutable object example
def modify_list(x):
    x[0] = 20

lst = [10, 11, 12, 13]
modify_list(lst)
print(lst)   # Modified list

# Immutable object example
def modify_int(x):
    x = 20

a = 10
modify_int(a)
print(a)     # Value remains unchanged


# ========================================
# RECURSIVE FUNCTIONS
# ========================================
"""
A recursive function is a function that calls itself.
It must have:
1. Base Case – stops recursion
2. Recursive Case – function calls itself
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))


"""
End of Python Functions Module
--------------------------------
This file combines theory + programs for:
✔ Exams
✔ Viva
✔ Practical understanding
✔ Revision
"""
