# Task 1: Lists

# 1. Create a list of 5 numbers.
# 2. Print the full list.
# 3. Print the first 3 elements.
# 4. Add a number to the end of the list.
# 5. Remove the second element.
# 6. Print the list length.

list = [1,2,3,4,5]
print(list)
print(list[0:3])
list.append(9)
print(list)
list.remove(2)
print(list)
print(len(list))

# Task 2: List Methods
# Use append(), insert(), remove(), pop() on your list.
# Try sorting your list using sort() and reversing it with reverse().

list.append(6)
print(list)
list.insert(2,7)
print(list)
list.remove(1)
print(list)
list.pop()
print(list)
list.sort()
list.reverse()
print(list)

# Task 3: Tuples
# Create a tuple of 5 numbers.
# Print the tuple.
# Print a slice of the tuple (first 3 elements).
# Try to change a tuple element (to see immutability).

tuple = (1,2,3,4,5)
print(tuple)
print(tuple[0:3])
# tuple.append(6) # This will show an error because tuple is immutable
print(tuple)

# Task 4: User Input List
# Ask the user to enter 3 numbers (one by one).
# Store them in a list and print the sum of all numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

list = [num1, num2, num3]

print("Sum of all numbers :", sum(list))
