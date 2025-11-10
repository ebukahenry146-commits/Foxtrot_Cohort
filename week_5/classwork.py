class Employee:

    def __init__(self, name, age, gender, BVN):
        self.name = name
        self.age = age
        self.gender = gender
        self.BVN = BVN


    def information(self):
        return f"My name is {self.name}, I am a {self.gender}, I am {self.age} years old, and my Bank Verification Number is {self.BVN}"
    
egungwu_ebuka = Employee(name="Egungwu Ebuka", age=16, gender="Male", BVN=1234567890 )
print(egungwu_ebuka.information())  