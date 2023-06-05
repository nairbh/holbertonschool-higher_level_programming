#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return
    elif idx >= len(my_list):
        return
    else:
        for n in range(len(my_list)):
            if n == idx:
                newlist = my_list[n]
                my_list[n] = element
                element = newlist
                return my_list
