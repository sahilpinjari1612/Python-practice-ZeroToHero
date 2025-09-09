Day 4 – Lists and Tuples in Python
Topics Covered
1. Lists

A list is an ordered, mutable collection of items.

Supports indexing, slicing, adding, and removing elements.

Example from code:

list = [1, 2, 3, 4, 5]
print(list)        # Full list
print(list[0:3])   # First 3 elements
list.append(9)     # Add element
list.remove(2)     # Remove element
print(len(list))   # Length of list

2. List Methods

append(x) → adds element at the end
insert(i, x) → inserts at given index
remove(x) → removes first occurrence of x
pop() → removes last element
sort() → sorts the list
reverse() → reverses the list

Example:

list.append(6)
list.insert(2, 7)
list.remove(1)
list.pop()
list.sort()
list.reverse()

3. Tuples

A tuple is an ordered, immutable collection of items.

Once created, you cannot change elements.

Example:

tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[0:3])   # Slice of tuple
# tuple[0] = 10  ❌ (error – immutable)

4. User Input List

Taking input and storing in a list.

Example from your code:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

list = [num1, num2, num3]
print("Sum of all numbers:", sum(list))