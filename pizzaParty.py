'''Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

Divide each person's hours worked by 3 to get their slice count.
You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
Each person gets a minimum of two slices.
Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.'''


import math

def get_pizzas_to_order(hours_worked):
    slicecountperperson = []
    for hours in hours_worked:
        if math.ceil(hours/3) <= 1:
            slicecountperperson.append(2)
        else:
            slicecountperperson.append(math.ceil(hours/3))
    totalpizza = math.ceil(sum(slicecountperperson)/8)
    print (totalpizza)

get_pizzas_to_order([8, 8, 8])
get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10])
get_pizzas_to_order([1, 2, 3, 4, 5])
get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8])
get_pizzas_to_order([9, 9, 6])
get_pizzas_to_order([10, 12, 16, 9, 8, 11, 15, 8, 0])