# =========================================================
# MODULE: PYRAMID PATTERNS IN PYTHON
# =========================================================
# THEORY:
# ---------------------------------------------------------
# Pyramid patterns are arrangements of characters (*, numbers,
# alphabets) in a symmetrical shape resembling a pyramid.
#
# Learning pyramid patterns helps understand:
# 1. Nested loops
# 2. Space and alignment logic
# 3. Loop boundaries
# 4. Pattern visualization
#
# Broad Classification:
# 1. Full Pyramid
# 2. Inverted Full Pyramid
# 3. Hollow Pyramid
# 4. Half Pyramid
# 5. Inverted Half Pyramid
# 6. Number Pyramid
# 7. Alphabet Pyramid
# =========================================================


# =========================================================
# 1. FULL PYRAMID USING LOOPS
# =========================================================
# Example (n = 5):
#     *
#    ***
#   *****
#  *******
# *********

def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars (odd count)
        for k in range(2 * i - 1):
            print("*", end="")
        print()

print("FULL PYRAMID")
full_pyramid(5)


# =========================================================
# 2. FULL PYRAMID USING RECURSION
# =========================================================

def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def recursive_pyramid(n, row=1):
    if row > n:
        return
    print_space(n - row)
    print_star(2 * row - 1)
    print()
    recursive_pyramid(n, row + 1)

print("\nFULL PYRAMID (RECURSION)")
recursive_pyramid(5)


# =========================================================
# 3. PYRAMID WITH ALPHABETS
# =========================================================
# Output:
#      A
#     A B
#    A B C
#   A B C D
#  A B C D E

print("\nALPHABET PYRAMID")
n = 5
for i in range(n):
    print(" " * (n - i), end="")
    ch = 65
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()


# =========================================================
# 4. PYRAMID WITH NUMBERS
# =========================================================
# Output:
#     1
#    123
#   12345
#  1234567
# 123456789

print("\nNUMBER PYRAMID")
def number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print(j + 1, end="")
        print()

number_pyramid(5)


# =========================================================
# 5. INVERTED FULL PYRAMID
# =========================================================
# *********
#  *******
#   *****
#    ***
#     *

print("\nINVERTED FULL PYRAMID")
def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

inverted_full_pyramid(5)


# =========================================================
# 6. HOLLOW FULL PYRAMID
# =========================================================
#     *
#    * *
#   *   *
#  *     *
# *********

print("\nHOLLOW FULL PYRAMID")
def hollow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_pyramid(5)


# =========================================================
# 7. HALF PYRAMID (STARS)
# =========================================================
# *
# * *
# * * *
# * * * *
# * * * * *

print("\nHALF PYRAMID")
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print()

half_pyramid(5)


# =========================================================
# 8. HALF PYRAMID USING RECURSION
# =========================================================

print("\nHALF PYRAMID (RECURSION)")
def recursive_half_pyramid(n):
    if n == 0:
        return
    recursive_half_pyramid(n - 1)
    print("*" * n)

recursive_half_pyramid(5)


# =========================================================
# 9. HALF PYRAMID WITH NUMBERS
# =========================================================
# 1
# 1 2
# 1 2 3
# ...

print("\nHALF NUMBER PYRAMID")
def number_half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

number_half_pyramid(5)


# =========================================================
# 10. HALF PYRAMID WITH ALPHABETS
# =========================================================
# A
# B B
# C C C
# ...

print("\nHALF ALPHABET PYRAMID")
def alphabet_half_pyramid(n):
    ch = 65
    for i in range(n):
        for j in range(i + 1):
            print(chr(ch), end=" ")
        ch += 1
        print()

alphabet_half_pyramid(5)


# =========================================================
# 11. INVERTED HALF PYRAMID
# =========================================================
# * * * * *
# * * * *
# * * *
# * *
# *

print("\nINVERTED HALF PYRAMID")
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

inverted_half_pyramid(5)


# =========================================================
# 12. HOLLOW INVERTED HALF PYRAMID
# =========================================================
# *****
#  *  *
#   * *
#    **
#     *

print("\nHOLLOW INVERTED HALF PYRAMID")
def hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_inverted_half_pyramid(5)


# =========================================================
# END OF PYRAMID PATTERN MODULE
# =========================================================
# KEY EXAM / VIVA POINTS:
# ---------------------------------------------------------
# ✔ Patterns rely on nested loops
# ✔ Spaces control alignment
# ✔ Stars/numbers control structure
# ✔ Time Complexity (most): O(n²)
# ✔ Space Complexity: O(1) except recursion
# ✔ Frequently asked in exams & interviews
# =========================================================
