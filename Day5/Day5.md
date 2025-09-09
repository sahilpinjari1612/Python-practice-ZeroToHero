📘 Day 5 – Dictionaries and Sets
🔹 Task 1: Dictionary Basics
    Created a dictionary with keys: "name", "age", "city".
    Accessed values using keys (dict["city"]).
    Updated values using .update().
    Added a new key "hobby".
    Removed "city" using .pop().

🔹 Task 2: Dictionary Methods
    .keys() → retrieved all keys.
    .values() → retrieved all values.
    .items() → retrieved key-value pairs.
    .get("name") → safely accessed a value.
    .update({"country": "India"}) → added a new entry.

🔹 Task 3: Sets
    Created sets {1, 2, 3, 4, 5} and {4, 5, 6, 7}.
    Performed:
        Union (set1.union(set2))
        Intersection (set1.intersection(set2))
        Difference (set1.difference(set2))

🔹 Task 4: User Input Dictionary
    Took input for 3 students and their marks.
    Stored them in a dictionary.
    Found the student with the highest marks using:
        topper = max(stud_dict, key=stud_dict.get)
        print("Topper is:", topper, "with marks:", stud_dict[topper])


✅ Concepts Covered:
    Dictionaries: Creation, Access, Update, Delete
    Dictionary Methods
    Sets: Union, Intersection, Difference   
    Finding maximum value in a dictionary