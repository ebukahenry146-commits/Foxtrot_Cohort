



















#output = subtraction():
# print(output)


'''
What can a function return 
string
boolean 
integer 
float
list 
tuple
dictionary
set
function 
variable
'''

def introduction():
    return "Hi my name is Miracle"

# print (
# introduction ()
# )

age = 12 # Global variable 

def func():
   name = "King" # Local variable
   return "His is name is " + name + " and he is " + str(age)

# print (
#        func()
# )



# Parameters and Arguments 
def func_1(words): # parameter
    return words


#print(
#    func_1("This is an argument") # argument  
# )


def reuseable_addition(num_one,num_two):
    return num_one + num_two

output_one = reuseable_addition(14, 2)
output_two = reuseable_addition(4, 4)
output_three = reuseable_addition(16, 18) 

print()


# Types of argument

# Positional argument
def func_2(pos1, pos2, pos3):
    return pos1, pos2, pos3

func_2("first value", "second value", "third value")  # Positional argument

func_2(pos1= "First", pos2="Second", pos3="third" )   #Keyword argument

# Default Argument 
def game(mode="easy"):
   if mode:
       return f"Game on!!! mode {mode}"

#print(
#    game(),
#    game("hard")
#)



# ARGS Variable Length Argument
def func_4(*param):
    return param # The structure is a tuple

print(
    func_4("red", "blue", "yellow", "green")
)

# KWARGS - Keyword as an argument 
def func_5(**param):
    return param # A dictionary is returned  

print(
     func_5(
        name="Miracle", 
        email="miracle@gmail.com",     
        availability= True,
        ratings=8.0
    )
)




