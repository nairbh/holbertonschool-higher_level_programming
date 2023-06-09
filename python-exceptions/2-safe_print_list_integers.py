#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    try:
        while index < x:
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end="")
                index += 1
            count += 1
    except (IndexError, ValueError, TypeError):
        pass

    print()
    return index
