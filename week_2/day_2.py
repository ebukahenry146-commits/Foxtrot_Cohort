# Data Structure in Python 
# Data Structures are used to store multiple values in a single variable.
# There are four built-in data structures in Python: List, Tuple, Set, Dictionary.

'''
dictionary  
list
tuple
set
'''
# Dictionary
person = {
"first_name": "Justice",
"last_name": "Rivers",
"age": "28",
"gender":"Male",  
"profession": "Petroleum Engineer",
"nationality": {
"nation": "Nigeria",
"nin": "34456627987", 
"tax": "all paid in full"
},
"tags":[1,2,3,4,2,5]
}
print(person)







introducion = f"Hello {person["first_name"]} {person["last_name"]} from {person["nationality"]["nation"]}.It's nice to meet You"
print(introducion)

# Update or Reassign values in keys 
person["profession"] = "Software Engineering"
print(person["profession"])

# Assign new key with a value in a dictionary
person["club"] = "Liverpool"
print(person["club"])

# Delete a key
del person["gender"]








# person.clear() # removes the entire key with it's dictionary

# List
datas = ["Paul", 22, False, 14.5, person, [1,2,3,4,5]]
#print (type(datas))

print(
datas[4]["tags"][0],
datas[5][2]
)

print(datas[4]["nationality"]["nin"])
 
datas[0] = "John" # Assigning value into an existing list

del datas[5] # deleting data inside a list0

concat = [1,2,3,4,5] + [6,7,8,9,0] # Concatenation
print(concat)

is_in_datas = 48 in datas # Membership
print(is_in_datas)

daniel_bryan = ["Yes"] * 4 # Repititon
print(daniel_bryan)

numbers = [1,2,3,4,5,6,7,8,9,0, "end"]
numbers.append(11)
numbers.insert(0, 100) #Add a data at a paticular time index
numbers.pop(10) # Remove items from the list through index
numbers.remove(7) # Remove items from the list through the value

print(numbers)

# Simple classwork
nested_numbers = [2,46,33,1,6,3,["twenty", "yes",5,6, {"another": [3,55,6,"middle",17]},7], 55,2, 4]

# Locate yes
print(nested_numbers[6][1])
# add "end" to the list of another

nested_numbers[6][4]["another"].append("end")


print(nested_numbers)
# delete the number 7
del nested_numbers[6][5]
print(nested_numbers)


# Tuple

colors = ("red", "blue", "yellow", "red") # immutable

repeat = colors * 2
membership = "blue" in colors
concat = colors + ("orange", "green", "purple")
c = colors.count("red")

# del colors[0] #This does not work because it is immutable

print(c)
print(colors[3])

# Set
top_4 = {"Arsenal", "Liverpool", "Tottenham", "Bournemouth"}

top_4.clear() # Clear values out of set

top_4.difference

regulars = {"Fullham", "Bournemouth", "Burnley", "Wolves"}

# top_4.clear() # Clear values out of set 
# check for other methods to use as well

intersect = top_4.intersection(regulars) # Common Value between two sets
union = top_4.union(regulars) # Joins sets # short form for union ->top_4 | regulars 
difference = top_4.difference(regulars) # Not common values between sets # short form for diffrerence -> top_4 - regulars


print(top_4)




