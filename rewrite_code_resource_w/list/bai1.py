"""
Write a Python program to sum all the items in a list.
"""
def sum_list(items):            #ham sum_list co tham so la items
    sum_numbers = 0
    for i in items:
        sum_numbers += i
    return sum_numbers
print(sum_list([1,2,-8]))