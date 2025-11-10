class Person: # Blue print
    pass


miracle = Person() # Object also called an instance
clinton = Person() # Object - instance
tivsue = Person() # Object - instance

#class Person:
#  ] attributes -> characteristics
#  ] methods : action 
#               task
#               behaviours

class Footballer:


    # There are two types of attributes 
    # Class attribute
    game = "Football"
    ball = "Sphere"

    # Instance attribute
    def __init__(self, name, age, role): # Constructor
       self.name = name 
       self.age = age
       self.role = role

    # -------------- Methods here ----------
    def information(self):
       return f"{self.name} plays {Footballer.game}. The ball is {Footballer.ball}"

zinedine_zidane = Footballer(name="Zinedine Zidane", age= 34, role="Attacking Midfielder")
cristiano_ronaldo = Footballer(name= "Ronaldo", age=39, role="Stricker")

print(zinedine_zidane.information())
print(cristiano_ronaldo.information())

'''
class Person:
    def __init__(self):
        self.name = "Joe"


class Employee(Person):
    def __init__(self):
        super().__init__()


Joe = Employee()
print(Joe.name)
'''

class Person:
    def __init__(self, name, age, gender):
        self.age = age
        self.name = name
        self.gender = gender

class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)        
         

Joe = Employee(name="Joe Sandres", age=22, gender="Male")
print(Joe.age)
