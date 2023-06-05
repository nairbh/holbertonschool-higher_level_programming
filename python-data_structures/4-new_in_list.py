#!/bin/usr/python3
def new_in_list(my_list, idx, element):
    for n, i in enumerate(my_list):
        if i == idx:
            my_list[n]=element
    return my_list
