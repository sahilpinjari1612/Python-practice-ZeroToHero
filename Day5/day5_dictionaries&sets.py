# Task 1: Dictionary Basics

# 1. Create a dictionary with keys: "name", "age", "city".
# 2. Print the dictionary.
# 3. Access and print only the "city".
# 4. Update the "age" value.
# 5. Add a new key "hobby" with any value.
# 6. Delete the "city" key.

dict = {"name" : "Sahil","age" : 19,"city" : "Nashik"}
print(dict)
print(dict["city"])
dict.update(age = 20)
print(dict)
dict["hobby"] = "Gym"
print(dict)
dict.pop("city")
print(dict)

# Task 2: Dictionary Methods

# Use these methods on your dictionary:
# .keys() → to get all keys.
# .values() → to get all values.
# .items() → to get key-value pairs.
# .get("name") → safely access a value.
# .update({"country": "India"}) → add a new entry.

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
dict.update({"country":"India"})
print(dict)


# Task 3: Sets

# 1. Create a set with numbers {1, 2, 3, 4, 5}.
# 2. Add a new element to the set.
# 3. Remove one element.
# 4. Create another set {4, 5, 6, 7} and perform:
#     Union
#     Intersection
#     Difference

set1 = {1, 2, 3, 4, 5}
set1.update({6})
print(set1)
set1.remove(4)
print(set1)
set2 = {4, 5, 6, 7}
unio = set1.union(set2)
print(unio)
inter = set1.intersection(set2)
print(inter)
differ = set1.difference(set2)
print(differ)


# Task 4: User Input Dictionary

# Ask the user to enter 3 student names and their marks (one by one).
# Store them in a dictionary.
# Print the dictionary.
# Print the student with the highest marks.

stud_dict = {}

name1 = input("Enter name of student 1: ")
marks1 = int(input("Enter marks of student 1: "))
name2 = input("Enter name of student 2: ")
marks2 = int(input("Enter marks of student 2: "))
name3 = input("Enter name of student 3: ")
marks3 = int(input("Enter marks of student 3: "))

stud_dict = {name1:marks1, name2:marks2, name3:marks3}
print(stud_dict)


# Find student with highest marks
topper = max(stud_dict, key=stud_dict.get)
print("Topper is:", topper, "with marks:", stud_dict[topper])