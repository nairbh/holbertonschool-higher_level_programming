#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        str1 = ' '.join("{:d}".format(n) for n in i)
        print(str1)
