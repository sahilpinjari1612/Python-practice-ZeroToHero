# Task 1: Basic if-else

# 1. Take a number from the user.
# 2. Check if it is positive, negative, or zero.
# 3. Print the result.

num = int(input("Enter a number: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive")
    
# Task 2: Nested Conditions

# 1. Ask the user to enter their age.
# 2. If age < 18 → print "You are a minor."
# 3. If 18 ≤ age < 60 → print "You are an adult."
# 4. If age ≥ 60 → print "You are a senior citizen."

age = int(input("Enter your age: "))
if (age < 18):
    print("You are a minor.")
elif (age < 60):
    print("You are an adult.")
else :
    print("You are a senior citizen.")
    
# Task 3: Multiple Conditions with elif

# 1. Ask the user to enter marks (0–100).
# 2. Print grade based on marks:
#     90+ → A
#     75–89 → B
#     50–74 → C
#     <50 → Fail

marks = int(input("Enter marks (0-100): "))
if (marks == 90 and marks > 90):
    print("Grade A")
elif (marks >= 75 and marks <= 89):
    print("Grade B")
elif (marks >= 50 and marks <= 74):
    print("Grade C")
else:
    print("Fail")
    
# Task 4: Mini Project – Simple Calculator

# 1. Ask the user to input two numbers.
# 2. Ask for an operation (+, -, *, /).
# 3. Use if-elif-else to perform the operation.
# 4. Print the result.

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
opration = input("Enter which opration you want (+, -, *, /)")

if (opration == "+"):
    print("Addition: ",num1 + num2)
elif (opration == "-"):
    print("Substraction: ",num1 - num2)
elif (opration == "*"):
    print("Multipliction: ",num1*num2)
elif (opration == "/"):
    print("Division: ",num1/num2)