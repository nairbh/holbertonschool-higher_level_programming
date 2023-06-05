#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return
    elif idx >= len(my_list):
        return
    else:
        for i in range(len(my_list)):
            if i == idx:
                newlist = my_list[i]
                my_list[i] = element
                element = newlist

                return my_list
