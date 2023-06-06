#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    big = my_list[0]
    for n in range(1, len(my_list)):
        if my_list[n] > big:
            big = my_list[n] 
    return big
