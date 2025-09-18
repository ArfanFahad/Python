class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet (self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age} years old")

p1 = Person("Fahad", 25)
p1.greet()