class Tempu:
    def __init__(self, stand):
        self.stand = stand
        self.next = None
    
tempu_one = Tempu("Jigatala")
tempu_two = Tempu("Dhanmondi 15")
tempu_three = Tempu("Dhanmondi 27")
tempu_four = Tempu("Khamar Bari")

tempu_one.next = tempu_two
tempu_two.next = tempu_three
tempu_three.next = tempu_four

head = tempu_one
head = head.next

def tempu_stand(stand):     
    while(stand != None):
        print(stand.stand)
        stand = stand.next 

tempu_stand(head)