ChatGPT said:

Perfect, Sahil ✅ You’ve completed all Day 3 tasks correctly.

Here’s the ready-to-use documentation for your GitHub Day3.md based on your code:

Day 3 – Strings in Python
Topics Covered
1. Strings Creation & Printing

Create strings using quotes (" ").

Access full string or parts of it using slicing.

Example from your code:

name = "Sahil Pinjari"
print(name)       # Prints full string
print(name[0:6])  # Prints first 6 characters
print(name[-3:])  # Prints last 3 characters

2. String Methods

.upper() → Converts string to uppercase

.lower() → Converts string to lowercase

.strip() → Removes spaces from the start and end

.replace(old, new) → Replaces a word with another

.split() → Splits the string into a list of words

Example from your code:

msg = " python is FUN "
print(msg.upper())            # " PYTHON IS FUN "
print(msg.lower())            # " python is fun "
print(msg.strip())            # "python is FUN"
print(msg.replace("FUN","awesome"))  # " python is awesome "
print(msg.split())            # ['python', 'is', 'FUN']

3. String Formatting

Use f-strings to embed variables in strings.

Example:

age = 19
print(f"My name is {name} and I am {age} years old.")

4. User Input String

Take user input using input().

Convert to uppercase with .upper().

Find length using len().

Example:

str = input("Enter a String: ").upper()
print(len(str))
