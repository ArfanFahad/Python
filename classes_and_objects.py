# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet (self):
#         print(f"Hello, my name is {self.name}")
#         print(f"I am {self.age} years old")

# p1 = Person("Fahad", 25)
# p1.greet()


class Station:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def traverse (head):
        current = head

        while (current != None):
            print(f"Arrived at: {current.name}")
            current = current.next

stationA = Station("Station A")
stationB = Station("Station B")

stationA.next = stationB

Station.traverse(stationA)

    
