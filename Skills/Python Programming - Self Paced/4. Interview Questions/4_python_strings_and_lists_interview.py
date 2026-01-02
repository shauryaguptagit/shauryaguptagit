"""
=========================================================
STRINGS AND LISTS IN PYTHON (INTERVIEW NOTES)
=========================================================

Covers:
✔ String functions & immutability
✔ Memory behavior of strings vs lists
✔ Indexing & slicing
✔ List operations & complexity
✔ Comprehensions
✔ Sorting, splitting, flattening
✔ Hashing & dictionary keys
✔ Performance & optimization concepts

Best suited for:
• Interviews
• Viva preparation
• Conceptual clarity
"""


# =========================================================
# Q1. swapcase() FUNCTION
# =========================================================
"""
swapcase() converts uppercase letters to lowercase and vice versa.
It returns a new string (strings are immutable).
"""

s = "GeeksforGeeks"
print(s.swapcase())  # gEEKSFORgEEKS


# =========================================================
# Q2. STRING vs LIST MEMORY STORAGE
# =========================================================
"""
Strings:
• Stored in contiguous memory
• Immutable
• Optimized using string interning

Lists:
• Dynamic arrays
• Store references (pointers) to objects
• Elements can be scattered in memory
"""


# =========================================================
# Q3. NEGATIVE INDEXING
# =========================================================
s = "hello"
lst = [1, 2, 3]

print(s[-1])        # o
print(lst[-1])      # 3
print(s[-3:])       # llo
print(lst[-2:])     # [2, 3]


# =========================================================
# Q4. LIST vs TUPLE
# =========================================================
"""
List  → Mutable, slower, not hashable
Tuple → Immutable, faster, hashable (if elements are hashable)
"""


# =========================================================
# Q5. count() vs index()
# =========================================================
s = "hello"
lst = [1, 2, 1, 3]

print(s.count('l'))       # 2
print(s.index('l'))       # 2

print(lst.count(1))       # 2
print(lst.index(1))       # 0


# =========================================================
# Q6. remove() vs pop()
# =========================================================
lst = [1, 2, 3]

lst.remove(2)             # removes value
print(lst)

x = lst.pop(1)            # removes index
print(x, lst)


# =========================================================
# Q7. INTERSECTION WITHOUT SET
# =========================================================
def list_intersection(lst1, lst2):
    count = {}
    for num in lst1:
        count[num] = count.get(num, 0) + 1

    result = []
    for num in lst2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result


lst1 = [1, 2, 2, 1]
lst2 = [2, 2]
print(list_intersection(lst1, lst2))


# =========================================================
# Q8. STRING SLICING
# =========================================================
"""
Syntax: string[start:end:step]
"""

s = "Python"
print(s[1:5])      # ytho
print(s[::-1])     # reverse string


# =========================================================
# Q9. COMMON STRING OPERATIONS
# =========================================================
s = " hello world "

print(s.upper())
print(s.strip())
print(s.replace("world", "Python"))
print("Python" in s)


# =========================================================
# Q10. LIST COMPREHENSIONS
# =========================================================
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)


# =========================================================
# Q11. sort() vs sorted()
# =========================================================
lst = [3, 1, 2]

lst.sort()
print(lst)

new_list = sorted("cba")
print(new_list)


# =========================================================
# Q12. split() vs rsplit()
# =========================================================
s = "a b c"

print(s.split(maxsplit=1))
print(s.rsplit(maxsplit=1))


# =========================================================
# Q13. COMMON LIST OPERATIONS
# =========================================================
lst = [1, 2, 3]

lst.append(4)
lst.insert(1, 10)
lst.remove(2)
lst.reverse()

print(lst)


# =========================================================
# Q14. STRING INTERNING
# =========================================================
"""
Python stores identical immutable strings in a shared pool
to reduce memory usage.
"""

a = "hello"
b = "hello"
print(a is b)  # Often True due to interning


# =========================================================
# Q15. FLATTEN A NESTED LIST
# =========================================================
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
print(flat)


# =========================================================
# Q16. STRING IMMUTABILITY
# =========================================================
"""
Strings are immutable:
✔ Thread-safe
✔ Hashable
✔ Memory efficient
"""

s = "hello"
s = s + " world"
print(s)


# =========================================================
# Q17. STRING MEMORY OPTIMIZATION
# =========================================================
"""
String interning allows reuse of identical strings
→ Better performance & lower memory usage
"""


# =========================================================
# Q18. '+' vs join()
# =========================================================
words = ["Python", "is", "fast"]

print(" ".join(words))     # Efficient
print(words[0] + " " + words[1] + " " + words[2])


# =========================================================
# Q19. STRING HASH COLLISIONS
# =========================================================
"""
Different strings CAN have same hash (collision),
but Python minimizes collisions internally.
"""


# =========================================================
# Q20. WHY STRINGS CAN BE DICT KEYS
# =========================================================
"""
Strings → Immutable + hashable
Lists   → Mutable → not hashable
"""

d = {"name": "Alice"}
# d[[1, 2]] = "test"  # ERROR


# =========================================================
# Q21. STRING COMPARISON
# =========================================================
print("apple" < "banana")  # True (lexicographical)


# =========================================================
# Q22. PICKLING & UNPICKLING
# =========================================================
import pickle

data = {"a": 1, "b": 2}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    restored = pickle.load(f)

print(restored)


# =========================================================
# Q23. LIST APPEND TIME COMPLEXITY
# =========================================================
"""
append() → Amortized O(1)
Occasional resize → O(n)
"""


# =========================================================
# Q24. WHY LISTS STORE REFERENCES
# =========================================================
"""
✔ Supports heterogeneous data
✔ Avoids copying large objects
✔ Efficient memory usage
"""


# =========================================================
# Q25. STRING vs LIST SUMMARY
# =========================================================
"""
STRING:
• Immutable
• Text data
• Hashable
• Faster comparisons

LIST:
• Mutable
• Any data type
• Not hashable
• Flexible container
"""

print("Strings & Lists interview notes loaded successfully ✅")
