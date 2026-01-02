"""
=========================================================
                FILE HANDLING IN PYTHON
=========================================================

File Handling (File I/O) allows Python programs to:
✔ Read data from files
✔ Write data to files
✔ Append data
✔ Handle large datasets
✔ Store persistent information

Files are stored on disk and accessed using file objects.
"""


# =========================================================
# OPENING FILES
# =========================================================
"""
To work with a file, we must open it using open().

Syntax:
file = open('filename', 'mode')

Example:
file = open('example.txt', 'r')
"""

# NOTE:
# Always close files after use or use 'with' statement


# =========================================================
# FILE MODES
# =========================================================
"""
'r'  -> Read mode (file must exist)
'w'  -> Write mode (creates or truncates file)
'a'  -> Append mode (adds data at end)
'b'  -> Binary mode (images, audio, etc.)

Combined Modes:
'r+' -> Read + Write (no truncation)
'w+' -> Read + Write (truncates file)
'a+' -> Append + Read
"""


# =========================================================
# READING FROM FILES
# =========================================================
print("\n--- Reading from a File ---")

"""
Methods:
read()      -> Reads entire file
readline()  -> Reads one line
readlines() -> Reads all lines into a list
"""

# Example: read()
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found (read example skipped)")


# =========================================================
# WRITING TO FILES
# =========================================================
print("\n--- Writing to a File ---")

"""
Writing Modes:
'w' -> Overwrites file
'a' -> Appends data
"""

file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is written using write().\n")
file.close()


# =========================================================
# APPENDING TO FILES
# =========================================================
print("\n--- Appending to a File ---")

file = open("example.txt", "a")
file.write("This line is appended.\n")
file.close()


# =========================================================
# CLOSING FILES
# =========================================================
"""
file.close() releases system resources.
Failing to close files may cause data loss or corruption.
"""


# =========================================================
# USING WITH STATEMENT (BEST PRACTICE)
# =========================================================
print("\n--- Using with Statement ---")

"""
with automatically:
✔ Opens the file
✔ Closes the file (even if error occurs)
"""

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found (with example skipped)")


# =========================================================
# HANDLING FILE EXCEPTIONS
# =========================================================
print("\n--- File Exception Handling ---")

try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Unexpected error:", e)


# =========================================================
# FILE METHODS
# =========================================================
"""
Common File Methods:
read(size)
readline()
readlines()
write(string)
writelines(list)
seek(offset, whence)
tell()
"""


# =========================================================
# read(size)
# =========================================================
print("\n--- read(size) Example ---")

with open("example.txt", "r") as file:
    content = file.read(5)
    print(content)

"""
Reads first 5 characters from file.
"""


# =========================================================
# readline()
# =========================================================
print("\n--- readline() Example ---")

with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

"""
Reads file line-by-line.
"""


# =========================================================
# readlines()
# =========================================================
print("\n--- readlines() Example ---")

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

"""
Reads entire file into a list of lines.
"""


# =========================================================
# write(string)
# =========================================================
print("\n--- write() Example ---")

with open("example.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")


# =========================================================
# writelines(list)
# =========================================================
print("\n--- writelines() Example ---")

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)

"""
Writes multiple strings to file.
"""


# =========================================================
# seek(offset, whence)
# =========================================================
print("\n--- seek() Example ---")

"""
whence values:
0 -> Beginning of file
1 -> Current position
2 -> End of file
"""

with open("example.txt", "r") as file:
    file.seek(10, 0)   # Move to 10th byte
    print(file.read())


# =========================================================
# tell()
# =========================================================
print("\n--- tell() Example ---")

with open("example.txt", "r") as file:
    print("Initial position:", file.tell())
    file.read(5)
    print("After reading 5 chars:", file.tell())


# =========================================================
# BINARY FILE HANDLING (OVERVIEW)
# =========================================================
"""
Binary files use 'b' mode:
'rb' -> read binary
'wb' -> write binary

Used for:
✔ Images
✔ Audio
✔ Video
✔ PDFs
"""


# =========================================================
# ADVANTAGES OF FILE HANDLING
# =========================================================
"""
✔ Data persistence
✔ Handles large datasets
✔ Easy data sharing
✔ Useful for logs & configs
"""


# =========================================================
# DISADVANTAGES
# =========================================================
"""
✘ Risk of data loss if misused
✘ Requires exception handling
✘ File permission issues
"""


# =========================================================
# EXAM / VIVA QUICK NOTES
# =========================================================
"""
✔ open() opens a file
✔ Always close files
✔ with statement is safest
✔ read(), readline(), readlines()
✔ write(), writelines()
✔ seek() moves cursor
✔ tell() shows cursor position
✔ Handle FileNotFoundError
"""
