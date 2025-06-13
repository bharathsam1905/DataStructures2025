class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"  
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"  


# Creating an object
p = Person("Bharath", 30)


# Using __str__
print(p)  # Calls __str__ -> Output: Bharath is 30 years old
print(repr(p))
