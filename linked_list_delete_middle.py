class Tempu:
    def __init__(self, stand):
        self.stand = stand
        self.next = None
    
tempu_one = Tempu("Jigatala")
tempu_two = Tempu("Dhanmondi 15")
tempu_three = Tempu("Dhanmondi 27")
tempu_four = Tempu("Khamar Bari")
tempu_five = Tempu("Farmgate")

tempu_one.next = tempu_two
tempu_two.next = tempu_three
tempu_three.next = tempu_four
tempu_four.next = tempu_five

head = tempu_one
prev = tempu_two
prev.next = prev.next.next 

def tempu_stand(stand):     
    while(stand != None):
        print(stand.stand)
        stand = stand.next 

tempu_stand(head)