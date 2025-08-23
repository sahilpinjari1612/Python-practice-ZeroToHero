# Day 3 - Strings in Python

# Task 1: Strings Creation & Printing
name = "Sahil Pinjari"
print(name)
print(name[0:6])
print(name[-3:])

# Task 2: String Methods
msg = " python is FUN "
print(msg.upper())
print(msg.lower())
print(msg.strip()) # Remove spaces
print(msg.replace("FUN", "awesome"))
print(msg.split())

# Task 3: String Formatting
age = 19
print(f"My name is {name} and I am {age} years old.")

# Task 4: User Input String
str = input("Enter a String: ").upper()
print(len(str))