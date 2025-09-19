#for positional arguments 
def add_numbers(*args): 
    total = 0
    for num in args:
        total = total + num
    return total

def single_number():
    number = 5
    return number

def another_number():
    an_number = 5
    return an_number

a_list = [single_number(), another_number()]
x, y = a_list

print(add_numbers())