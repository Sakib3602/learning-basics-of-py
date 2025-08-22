"""
Notes:
- Arrays must be of the same type: e.g., a = [1, 2, 3]
- Lists in Python can have different types: e.g., a = [1, "hello", 3.4]
- Lists are powerful: you can append, pop, remove, sort, reverse, count, etc.
"""

# Creating a list
listOfA = [1, 4, 4, 10, 9, 2, 2, 3, 4, 5]
print("Original list:", listOfA)

# ------------------------------
# Append an element at the end
listOfA.append(1000)
print("After append:", listOfA)

# ------------------------------
# Length of the list
print("Length of list:", len(listOfA))

# Accessing the last element
print("Accessing last element:", listOfA[-1])

# ------------------------------
# Remove last element
listOfA.pop()  # removes 1000
print("After pop:", listOfA)

# ------------------------------
# Reverse the list
listOfA.reverse()
print("After reverse:", listOfA)

# Count occurrences of 4
print("Count of 4:", listOfA.count(4))

# ------------------------------
# Sort the list in ascending order
listOfA.sort()  # works only if all elements are of same type
print("After sort ascending:", listOfA)

# Sort strings
nam = ["sakib", "tamim", "mushfiq", "shakib", "tamim"]
nam.sort()  # alphabetical sort
print("After sort names:", nam)

# Sort in descending order
listOfA.sort(reverse=True)
print("After sort descending:", listOfA)

# ------------------------------
# Iterating through the list
print("Iterating through listOfA:")
for x in listOfA:
    print(x)
