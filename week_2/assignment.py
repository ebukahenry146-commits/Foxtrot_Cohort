# ====================== PYTHON DATA STRUCTURES ASSIGNMENT ======================

# ----------- DICTIONARY -----------

# 1. Create a dictionary called car with keys: "brand", "model", "year".
#    Give them values and print the dictionary.
# Answer no 1 here.

# Dictionary
Car = {
"brand": "Aliyah", 
"model": "Zendeyah", 
"year": "1998", 
}
print(Car)

# 2. From a dictionary called book = {"title": "Python 101", "author": "James", "year": 2022},
#    print only the title and author.
# Answer no 2 here.

# Dictionary
book = {
"title": "Python 101", 
"author": "James",
"year": "2022"
}
print(book["title"])
print(book["author"])

# 3. Change the value of "year" in book to 2024 and print the dictionary.
# Answer no 3 here.
book["year"] = "1134"
print(book)

# 4. Add a new key "pages" with any number value to the dictionary book.
# Answer no 4 here.

# Dictionary
book = {
"title": "Python 101", 
"author": "James",
"year": "2022", 
"pages": "9087", 
}
print(book)

# 5. Delete the "author" key from the dictionary book and print it.
# Answer no 5 here.

del book["author"]
print(book)

# ----------- LIST -----------

# 6. Create a list of 5 countries and print the first and last country.
# Answer no 6 here.

list = ["Nigeria", "Australia", "Zimbabwe", "Russia", "USA"]
print(list[0])
print(list[4])

# 7. Replace the 2nd item in your list of countries with "Canada".
# Answer no 7 here.

list.insert(1,"Canada")
print(list)

# 8. Delete the 3rd item in your list of countries.
# Answer no 8 here.

del list[2]
print(list)

# 9. Concatenate [10, 20, 30] with [40, 50, 60] and print the new list.
# Answer no 9 here.

concat = [10, 20, 30] + [40, 50, 60]
print(concat)

# 10. Check if "Kenya" exists inside your list of countries and print the result.
# Answer no 10 here.

is_in_list = "Kenya " in list
print(is_in_list)

# 11. Create a list with the word "Hello" repeated 4 times.
# Answer no 11 here.

nenye = ["Hello"] * 4
print(nenye)

# 12. Use append() to add "Japan" to your list of countries.
# Answer no 12 here.

list.append("Japan")
print(list)

# 13. Use insert() to add "Brazil" at position 2 in your list of countries.
# Answer no 13 here.

list.insert(3, "Brazil")
print(list)

# 14. Use pop() to remove the last item from a list of numbers = [100, 200, 300, 400].
# Answer no 14 here.

ebuka = [100, 200, 300, 400]
ebuka.pop(3)
print(ebuka)

# 15. Use remove() to delete the number 200 from the list numbers = [100, 200, 300, 400].
# Answer no 15 here.

ebuka.remove(200)
print(ebuka)

# ----------- NESTED LIST -----------

# 16. Given nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]
#     - Print the value "b"
#     - Add "d" into the "letters" list
# Answer no 16 here.

nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]
print(nested[1][2]["letters"][1])

# ----------- TUPLE -----------

# 17. Create a tuple of 4 animals and print the second animal.
# Answer no 17 here.
animals = ("lion", "goat", "elephant", "bear")
print(animals[1])

# 18. Try to change one value in the tuple. What happens? (Write the answer in a comment)
# Answer no 18 here.

# animals.insert(0,"dog")
# print(animals)
# tuple does not allow you to change the value of an object once inserted  

# 19. Count how many times "cat" appears in the tuple: pets = ("cat", "dog", "cat", "bird").
# Answer no 19 here.

pets = ("cat", "dog", "cat", "bird")
print (pets.count("cat"))

# ----------- SET -----------

# 20. Create two sets:
#     set1 = {"apple", "banana", "cherry"}
#     set2 = {"banana", "mango", "cherry"}
#     - Find the intersection
#     - Find the union
#     - Find the difference (set1 - set2)
# Answer no 20 here.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "mango", "cherry"}
intersect = set1.intersection(set2)
print(intersect)

union = set1.union(set2)
print(union)

difference = set1.difference(set2)
print(difference)
