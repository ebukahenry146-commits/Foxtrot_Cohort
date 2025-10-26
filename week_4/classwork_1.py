# ================== PYTHON HIGHER ORDER FUNCTIONS ASSIGNMENT ==================

# 1. Create a simple function called greet() that returns "Hello, how are you?".
#    Then call the function and print the result.
# Answer no 1 here.

def greet():
    return "Hello, how are you?"

def boy(name, func):
    return f"{name}: {func()}"

call = boy("Jerry", greet)
print(call)

# 2. Create a function called call_function(func) that takes another function as an argument
#    and returns the result of calling that function.
#    Use it to call greet() from question 1.
# Answer no 2 here.

def call_function(func):
    return "Hello, how are you?"

def greet(name, func): 
    return f"{name}: {func}"

call = greet("David", call_function("func"))
print(call)


# 3. Given numbers = [1, 2, 3, 4, 5]
#    Use the map() function to multiply each number by 3 and print the new list.
# Answer no 3 here.

numbers = [1, 2, 3, 4, 5]
def multiply_by_2(item):
    return item * 2

map_func = map(multiply_by_2, numbers)
print(list(map_func))

# 4. Using filter(), get only the numbers that are greater than 10
#    from this list: nums = [5, 12, 8, 20, 3, 15]
# Answer no 4 here.

nums = [5, 12, 8, 20, 3, 15] 
filter_func = filter(lambda item: item > 10 , nums)
print(list(filter_func))

# 5. Using reduce() from functools, find the total sum of this list:
#    values = [10, 20, 30, 40]
# Answer no 5 here.

from functools import reduce
values = [10, 20, 30, 40, 50]
def concatenate(param_1, param_2):
    

    return param_1 + param_2
reduce_func = reduce(concatenate,values)
print(reduce_func)

# 6. Write a lambda function that takes one number and returns the number multiplied by 5.
#    Test it with the number 6.
# Answer no 6 here.

value = [6]
def multiply_by_5(item):
    return item * 5 

map_func = map(multiply_by_5, value)
print(list(map_func))

# 7. Create a nested function:
#    - outer_function() should define an inner_function() that returns "Inner function called".
#    - The outer_function() should return the result of inner_function().
#    - Call outer_function() and print the result.
# Answer no 7 here.

def outer_function():
    def inner_function():
        return "Inner function called" 
    return inner_function()
call = (outer_function())
print (call)

# 8. Using list comprehension, create a new list that contains each number squared
#    from the list numbers = [2, 4, 6, 8].
# Answer no 8 here.



# 9. Using list comprehension, create a list that contains only even numbers
#    from numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Answer no 9 here.


# 10. Combine map() and lambda:
#     From data = [1, 2, 3, 4, 5],
#     use map() with a lambda to add 2 to every number.
#     Print the new list.
# Answer no 10 here.