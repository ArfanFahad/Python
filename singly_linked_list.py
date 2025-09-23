class Station:
    def __init__(self, name):
        self.name = name
        self.next = None

uttara = Station("Uttara")
mirpur10 = Station("Mirpur 10")
kazipara = Station("Kazipara")
shewrapara = Station("Shewrapara")


uttara.next = mirpur10
mirpur10.next = kazipara
kazipara.next = shewrapara

def myStation (head):
    current = head

    while(current != None):
        print(current.name)
        current = current.next

myStation(uttara)

    
