#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if type(matrix) is list:
        return [square_matrix_simple(x) for x in matrix]
    else:
        return matrix**2
