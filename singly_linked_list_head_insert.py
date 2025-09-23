class Tickets:
    def __init__(self, name):
        self.name = name
        self.next = None
    
dhaka = Tickets("Dhaka Stadium")
rajshahi = Tickets("Rajshahi Stadium")
khulna = Tickets("Khulna Stadium")
chattogram = Tickets("Chattogram Stadium")
chapai = Tickets("Chapainawabganj Stadium")

dhaka.next = rajshahi
rajshahi.next = khulna
khulna.next = chattogram
chattogram.next = chapai

# now our head is dhaka so I need to catch it
head = dhaka
dukka = Tickets("Dukka Stadium") # new object
dukka.next = head # now dhaka is next head 
head = dukka # new head is dukka 


def Stadium(stadium_name):
    current = head
    while (current != None):
        print(current.name)
        current = current.next
Stadium(dhaka)


