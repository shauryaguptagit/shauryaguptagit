# 🧠 Dictionary Mastery – One Complete Coding Problem
# 📌 Problem Statement

# You are building a mini product price manager for an online store.

# Step-by-step Tasks (ALL in one program):

# Create an empty dictionary named products

# Add the following products and prices:

# "laptop" → 50000

# "mobile" → 20000

# "earphones" → 1500

# Print the entire dictionary

# Access and print the price of "mobile" using:

# square brackets

# get() method

# Try to access "tablet" using:

# get() with default value "Not Available"

# Check if "laptop" exists:

# If yes, update its price to 48000

# Print total number of products

# Remove "earphones" using pop() and print the removed price

# Add a new product "keyboard" → 2500

# Remove the last inserted item using popitem() and print it

# Finally, print the updated dictionary

# 🧪 Expected Concepts Tested

# ✔ Dictionary creation
# ✔ Insert & update
# ✔ Key access ([] and get())
# ✔ Membership check (in)
# ✔ pop() vs popitem()
# ✔ len()
# ✔ Printing final state

products = {}

products["laptop"] = 50000
products["mobile"] = 20000
products["earphones"] = 1500

print(products)

print(products["mobile"])
print(products.get("mobile"))

print(products.get("tablet", "Not Available"))

if "laptop" in products:
    products["laptop"] = 48000

print(len(products))

print(products.pop("earphones"))

products["keyboard"] = 2500

print(products.popitem())

print(products)