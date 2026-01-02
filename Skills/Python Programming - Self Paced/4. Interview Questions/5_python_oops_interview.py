"""
=========================================================
OBJECT ORIENTED PROGRAMMING (OOPs) IN PYTHON
INTERVIEW + VIVA NOTES
=========================================================

Covers:
✔ Method overriding
✔ Static / Class / Instance methods
✔ Multiple inheritance & MRO
✔ Polymorphism & duck typing
✔ Encapsulation
✔ __init__ vs __new__
✔ @property
✔ Composition vs inheritance
✔ Diamond problem
✔ __call__
✔ Immutability
✔ Metaclasses
✔ Private & protected members
"""


# =========================================================
# Q1. METHOD OVERRIDING
# =========================================================
class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        print("Child method (Overridden)")


obj = Child()
obj.show()


# =========================================================
# Q2. INSTANCE vs CLASS vs STATIC METHODS
# =========================================================
class Demo:
    class_var = "Class Level"

    def instance_method(self):
        return "Instance Method"

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "Static Method"


d = Demo()
print(d.instance_method())
print(d.class_method())
print(d.static_method())


# =========================================================
# Q3. MULTIPLE INHERITANCE
# =========================================================
class A:
    def show(self):
        print("Class A")


class B:
    def show_b(self):
        print("Class B")


class C(A, B):
    pass


c = C()
c.show()
c.show_b()


# =========================================================
# Q4. POLYMORPHISM
# =========================================================
class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.sound())


# =========================================================
# Q5. MONKEY PATCHING
# =========================================================
class Sample:
    def func(self):
        print("Original Function")


def monkey_func(self):
    print("Monkey Patched Function")


Sample.func = monkey_func
s = Sample()
s.func()


# =========================================================
# Q6. __init__ METHOD
# =========================================================
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Alice")
print(p.name)


# =========================================================
# Q7. ENCAPSULATION (PUBLIC / PROTECTED / PRIVATE)
# =========================================================
class Encapsulation:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print(self.__private)


e = Encapsulation()
print(e.public)
print(e._protected)
print(e._Encapsulation__private)


# =========================================================
# Q8. CALLING CLASS METHOD VIA INSTANCE
# =========================================================
class Test:
    @classmethod
    def show(cls):
        print("Class Method Called")


t = Test()
t.show()


# =========================================================
# Q9. __new__ vs __init__
# =========================================================
class DemoNew:
    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")


obj = DemoNew()


# =========================================================
# Q10. @property vs property()
# =========================================================
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks


s = Student(90)
print(s.marks)


# =========================================================
# Q11. COMPOSITION vs INHERITANCE
# =========================================================
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car driving")


car = Car()
car.drive()


# =========================================================
# Q12. DIAMOND PROBLEM & MRO
# =========================================================
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


print(D.mro())
d = D()
d.show()


# =========================================================
# Q13. del obj vs obj = None
# =========================================================
x = [1, 2, 3]
y = x

del x
print(y)

y = None
print(y)


# =========================================================
# Q14. DUCK TYPING
# =========================================================
class Pen:
    def write(self):
        print("Writing")


class Keyboard:
    def write(self):
        print("Typing")


def perform(obj):
    obj.write()


perform(Pen())
perform(Keyboard())


# =========================================================
# Q15. METHOD RESOLUTION ORDER
# =========================================================
print(D.__mro__)


# =========================================================
# Q16. __call__ METHOD
# =========================================================
class CallableClass:
    def __call__(self):
        print("Object called like function")


c = CallableClass()
c()


# =========================================================
# Q17. ENFORCING IMMUTABILITY
# =========================================================
class Immutable:
    __slots__ = ("value",)

    def __init__(self, value):
        object.__setattr__(self, "value", value)

    def __setattr__(self, key, value):
        raise AttributeError("Immutable object")


i = Immutable(10)
print(i.value)


# =========================================================
# Q18. classmethod vs staticmethod
# =========================================================
class Example:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def utility():
        print("Utility Function")


Example.increment()
Example.utility()
print(Example.count)


# =========================================================
# Q19. INHERITING FROM object
# =========================================================
class MyClass:
    pass


print(isinstance(MyClass(), object))


# =========================================================
# Q20. CLASS VARIABLE vs INSTANCE VARIABLE
# =========================================================
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


a = Counter()
b = Counter()
print(Counter.count)


# =========================================================
# Q21. METACLASSES
# =========================================================
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class", name)
        return super().__new__(cls, name, bases, dct)


class MyMetaClass(metaclass=Meta):
    pass


# =========================================================
# Q22. OOP PRINCIPLES SUMMARY
# =========================================================
"""
Encapsulation  → Data hiding
Abstraction    → Interface over implementation
Inheritance    → Code reuse
Polymorphism   → Same interface, different behavior
"""


# =========================================================
# Q23. self vs cls
# =========================================================
class Sample:
    class_var = "CLASS"

    def __init__(self, val):
        self.instance_var = val

    @classmethod
    def show_class(cls):
        print(cls.class_var)

    def show_instance(self):
        print(self.instance_var)


obj = Sample("INSTANCE")
obj.show_instance()
obj.show_class()


# =========================================================
# Q24. MULTIPLE CONSTRUCTORS (WORKAROUND)
# =========================================================
class User:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def from_name(cls, name):
        return cls(name=name)


u = User.from_name("Bob")
print(u.name)


# =========================================================
# Q25. PRIVATE & PROTECTED MEMBERS
# =========================================================
class Access:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"


a = Access()
print(a._protected)
print(a._Access__private)


print("OOPs Interview Notes Loaded Successfully ✅")
