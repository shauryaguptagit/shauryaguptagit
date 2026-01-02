"""
=========================================================
                PYTHON ascii() FUNCTION
=========================================================

The ascii() function in Python returns a string containing
a printable representation of an object.

✔ Non-ASCII characters are escaped
✔ Uses \\x, \\u or \\U Unicode escape sequences
✔ Ensures output contains only ASCII characters
✔ Useful for debugging, logging and ASCII-safe output
"""

# =========================================================
# BASIC EXAMPLE
# =========================================================
print("\n--- Basic ascii() Example ---")
print(ascii("¥"))

"""
Explanation:
The yen symbol (¥) is a non-ASCII character.
ascii() converts it into its Unicode escape sequence '\\xa5'.
"""


# =========================================================
# SYNTAX OF ascii()
# =========================================================
"""
ascii(object)

object -> Any Python object (string, int, list, tuple, set, etc.)
Return -> String with non-ASCII characters escaped
"""


# =========================================================
# ascii() WITH STRING CONTAINING NON-ASCII CHARACTERS
# =========================================================
s = "G ë ê k s f ? r G ? e k s"
print("\n--- ascii() on string with non-ASCII characters ---")
print(ascii(s))

"""
Explanation:
Characters like ë and ê are non-ASCII.
ascii() replaces them with Unicode escape sequences.
"""


# =========================================================
# ascii() WITH MULTI-LINE STRING
# =========================================================
s = '''Geeks
for
geeks'''

print("\n--- ascii() on multi-line string ---")
print(ascii(s))

"""
Explanation:
New line characters are represented as '\\n'.
ascii() keeps ASCII characters unchanged.
"""


# =========================================================
# ascii() WITH SET
# =========================================================
s = {"Š", "E", "T"}
print("\n--- ascii() on set ---")
print(ascii(s))

"""
Explanation:
The non-ASCII character 'Š' is converted to '\\u0160'.
ASCII characters remain unchanged.
"""


# =========================================================
# ascii() WITH LIST
# =========================================================
a = ["Ň", "ĕ", "Ŵ"]
print("\n--- ascii() on list ---")
print(ascii(a))

"""
Explanation:
Each non-ASCII element in the list is escaped individually.
The structure of the list is preserved.
"""


# =========================================================
# ascii() WITH TUPLE
# =========================================================
t = ("Ģ", "Õ", "Õ", "D")
print("\n--- ascii() on tuple ---")
print(ascii(t))

"""
Explanation:
Tuple structure is preserved.
Only non-ASCII characters are escaped.
"""


# =========================================================
# ascii() WORKS WITH ANY PYTHON OBJECT
# =========================================================
data = {
    "currency": "€",
    "value": 100,
    "valid": True
}

print("\n--- ascii() on dictionary ---")
print(ascii(data))

"""
Explanation:
ascii() recursively converts non-ASCII characters
inside complex objects.
"""


# =========================================================
# DIFFERENCE BETWEEN ascii() AND repr()
# =========================================================
s = "café"

print("\n--- repr() vs ascii() ---")
print("repr(): ", repr(s))
print("ascii():", ascii(s))

"""
repr():
✔ Keeps Unicode characters as-is
✔ Useful for debugging and logs

ascii():
✔ Converts non-ASCII to Unicode escapes
✔ Useful for ASCII-only environments
"""


# =========================================================
# WHEN TO USE ascii()
# =========================================================
"""
✔ When output must be ASCII-only
✔ Logging in systems that don't support Unicode
✔ Debugging Unicode-related issues
✔ Safe serialization or transmission
"""


# =========================================================
# IMPORTANT CHARACTERISTICS (EXAM READY)
# =========================================================
"""
✔ Built-in function
✔ Accepts only one argument
✔ Always returns a string
✔ Escapes non-ASCII characters
✔ Preserves object structure
"""


# =========================================================
# VIVA / INTERVIEW QUESTIONS
# =========================================================
"""
Q: What does ascii() return?
A: A string containing ASCII-only representation of an object.

Q: Does ascii() modify the original object?
A: No, it only returns a string representation.

Q: Difference between ascii() and repr()?
A: ascii() escapes non-ASCII characters, repr() does not.

Q: Can ascii() be used on lists and tuples?
A: Yes, it works on all Python objects.
"""
