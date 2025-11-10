from functools import reduce
# Higher Order Functions 
# Higher Order Functions are functions that take a function as an arguement, or return a function. 

def speak():
    return "Ola. My name is miracle."

def man(name, func):
    return f"{name}: {func()}"  



call = man("Jerry", speak)
# print(call) 

# Map, Filter, Reduce 

# Map is a higher order function that returns back a new list.
numbers = [1,2,3,4,5,6,7,8,9]

def multiply_by_2(item):
    return item * 2

map_func = map(multiply_by_2, numbers)
# print(list(map_func))


# Filter: Returns a new filtered list 
def no_remainder(item):
    return item % 2 == 0

filter_func = filter(lambda item: item % 2 == 0, numbers)
# print(list(filter_func))



# Reduce: Returns a reduced value of the iterable
def concatenate(param_1, param_2):
    #print(concatenate(param_1 + param_2))
    return param_1 + param_2

reduce_func = reduce(concatenate, numbers)
# print(reduce_func)


func = lambda: "This is a function"
func_with_parameters = lambda a, b, c, d : a + b + c + d  
# print(func_with_parameters (1,2,3,4))

# Function nesting
def outer_function():
    def inner_function():
        return "I'm coming from the inner function"
    return inner_function()
# print(outer_function())


# List comprehension 
new_list = [item + 2 for item in numbers if item % 2 == 0]
print(new_list)



def funcA(func):
    # Runn operation first
    func
    # Run another operation

@funcA
def funcB():
    return True









