class Number:
    def __init__(self, data):
        self.data = data
        self.next = None
    
first_number = Number("First Number")
third_number = Number("Third Number")
fourth_number = Number("Fourth Number")

first_number.next = third_number
third_number.next = fourth_number

head = first_number
second_number = Number("Second Number")
head.next = second_number
second_number.next = third_number

def all_number(value):
    current = value
    while(current != None):
        print(current.data)
        current = current.next

all_number(head)
