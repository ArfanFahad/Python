

def linear_equations (num):
    
    formula = ((2 * num) - 4) and (5 - num)

    if formula % 2 == 0:
        print("Satisfied Number: ", num)
    else: 
        return num
    

my_lists = [10, 20, 30, 40, 3]
print("Given Numbers: ", my_lists)
satifyable_numbers = []

for item in my_lists:
    linear_equations(item)
    satifyable_numbers.append(item)


