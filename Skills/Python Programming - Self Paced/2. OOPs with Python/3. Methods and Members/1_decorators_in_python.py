"""
===========================================================
DECORATORS IN PYTHON
===========================================================

A Decorator in Python:
✔ Modifies or extends behavior of functions or methods
✔ Without changing the original function code
✔ Uses functions as first-class objects
✔ Common in logging, authentication, caching, validation

Definition:
A decorator is a function that takes another function
as an argument and returns a new function with enhanced behavior.
"""


# =========================================================
# BASIC DECORATOR EXAMPLE
# =========================================================
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper


@decorator
def greet():
    print("Hello, World!")


greet()

"""
Output:
-------
Before calling the function.
Hello, World!
After calling the function.

Explanation:
✔ decorator() receives greet()
✔ wrapper() adds behavior before & after greet()
✔ @decorator == greet = decorator(greet)
"""


# =========================================================
# DECORATOR WITH PARAMETERS (*args, **kwargs)
# =========================================================
def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper


@decorator_name
def add(a, b):
    return a + b


print(add(5, 3))

"""
Output:
-------
Before execution
After execution
8

Explanation:
✔ *args → positional arguments
✔ **kwargs → keyword arguments
✔ Makes decorator reusable for any function
"""


# =========================================================
# FUNCTIONS AS FIRST-CLASS OBJECTS
# =========================================================
"""
Functions in Python can be:
✔ Assigned to variables
✔ Passed as arguments
✔ Returned from other functions
"""

# Assigning function to variable
def greet(name):
    return f"Hello, {name}!"


say_hi = greet
print(say_hi("Alice"))


# Passing function as argument
def apply(func, value):
    return func(value)


print(apply(say_hi, "Bob"))


# Returning function from function
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply


double = make_multiplier(2)
print(double(5))

"""
Output:
-------
Hello, Alice!
Hello, Bob!
10
"""


# =========================================================
# HIGHER-ORDER FUNCTIONS
# =========================================================
"""
Higher-Order Functions:
✔ Take functions as arguments
✔ OR return functions
✔ OR do both
"""


def fun(f, x):
    return f(x)


def square(x):
    return x * x


print(fun(square, 5))

"""
Output:
-------
25

Decorators ARE higher-order functions
"""


# =========================================================
# FUNCTION DECORATORS
# =========================================================
def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")
        func()
        print(">>> Function finished")
    return wrapper


@simple_decorator
def greet():
    print("Hello, World!")


greet()

"""
Output:
-------
>>> Starting function
Hello, World!
>>> Function finished
"""


# =========================================================
# METHOD DECORATORS
# =========================================================
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper


class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")


obj = MyClass()
obj.say_hello()

"""
Output:
-------
Before method execution
Hello!
After method execution

Explanation:
✔ self must be passed explicitly
✔ Used for logging, validation in classes
"""


# =========================================================
# CLASS DECORATORS
# =========================================================
def add_class_name(cls):
    cls.class_name = cls.__name__
    return cls


@add_class_name
class Person:
    pass


print(Person.class_name)

"""
Output:
-------
Person

Explanation:
✔ Decorator modifies class itself
✔ Adds attributes or methods dynamically
"""


# =========================================================
# BUILT-IN DECORATORS
# =========================================================

# -----------------------------
# @staticmethod
# -----------------------------
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y


print(MathOperations.add(5, 3))

"""
✔ No self
✔ No cls
✔ Utility method
"""


# -----------------------------
# @classmethod
# -----------------------------
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

"""
✔ Uses cls
✔ Modifies class-level data
"""


# -----------------------------
# @property
# -----------------------------
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)


c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
print(c.area)

"""
✔ Access like attributes
✔ Encapsulation with validation
"""


# =========================================================
# CHAINING MULTIPLE DECORATORS
# =========================================================
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())

"""
Output:
-------
400
200

Explanation:
✔ Decorators execute bottom-up
✔ Order matters
"""


# =========================================================
# REAL-WORLD USE CASES (EXAM NOTE)
# =========================================================
"""
Decorators are used in:
✔ Logging
✔ Authentication (Flask / Django)
✔ Authorization
✔ Caching (functools.lru_cache)
✔ Rate limiting
✔ Retry mechanisms
"""


# =========================================================
# FINAL SUMMARY
# =========================================================
"""
DECORATORS SUMMARY
------------------------------------------------------------
✔ Functions that wrap other functions
✔ Based on first-class functions
✔ Cleaner alternative to repetitive code
✔ Support function, method & class modification
✔ Widely used in real-world frameworks

Key Rule:
@decorator
def f()
⇨ f = decorator(f)
"""

"""
END OF DECORATORS NOTES
===========================================================
"""
