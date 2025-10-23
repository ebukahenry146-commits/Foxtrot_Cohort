# ====================== PYTHON FUNCTIONS ASSIGNMENT ======================

# 1. Create a simple function called greet() that returns "Hello World".
# Answer no 1 here.

def greet():
    return " Hello World"
print(
    greet()
)

# 2. Create a function called add_numbers() that adds two numbers (5 and 10)
#    inside the function and returns the result.
# Answer no 2 here.

def add_numbers(num_1,num_2):
    return num_1 + num_2
output_one = add_numbers(5,10)  
print(add_numbers(5, 10))   

# 3. Create a function called introduction() that returns your name and age in a sentence.
#    Example: "My name is King and I am 25 years old."
# Answer no 3 here.

def introduction():
    name = "Ebuka"
    age = "16"
    return "My name is " + name + " and I am " + age + " years old"
print(introduction())

# 4. Create a function called area_of_square() that takes one parameter (side)
#    and returns the area of a square (side * side).
# Answer no 4 here.

def area_of_square(side):
    return side

print(
    area_of_square("side * side")
      
)

# 5. Create a function called multiply_numbers(num1, num2)
#    that returns the product of the two numbers.
#    Call the function three times with different values and print the results.
# Answer no 5 here.

def multiply_numbers(num_1, num_2):
    return num_1 * num_2

output_1 = multiply_numbers(2,3)
output_2 = multiply_numbers(4,8)
output_3 = multiply_numbers(6,3)

print(output_1 )
print(output_2 )
print(output_3 )

6.# Create a function that returns True if a number is greater than 10, otherwise returns False (You can name it check_number)
#Answer no 6 here.

numbers = [1,2,3,4,5,6,7,8,9]
def check_number():
    return check_number 
print()

# 7. Demonstrate the difference between a global variable and a local variable
#    inside a function. Use print() to show both.
# Answer no 7 here.

# Global Variable
age = "sixteen"
def func_3():
    name = "Clement"
    return "Hello my name is " + name + " and i am " + age + " years old"

print(func_3())

# Local Variable
def func_4():
    name = "Henry"
    age = "sixteen"
    return "Hello my name is " + name + " and i am " + age + " years old"

print(func_4())

# 8. Create a function called describe_pet(animal, name)
#    that returns a sentence like "My pet dog is named Rocky."
#    Call it using keyword arguments.
# Answer no 8 here.

def describe_animal(animal, name):
    return "My " + animal + " is named " + name  

describe_animal(animal= "Dog", name= "Rocky")
print(describe_animal(animal= "Dog", name= "Rocky" ))

# 9. Create a function called favorite_colors(*colors)
#    that accepts any number of colors and returns them as a tuple.
# Answer no 9 here.

def favorite_colors(*colors):
    return colors

print(
    favorite_colors("red", "black", "indigo", "white")
)

# 10. Create a function called student_profile(**data)
#     that accepts any number of keyword arguments (name, age, grade, etc.)
#     and returns them as a dictionary.
# Answer no 10 here. 

def student_profile(**data):
    return data

print(
    student_profile(
        name="Ebuka", 
        age= "16", 
        grade= "A+"
    )
)


