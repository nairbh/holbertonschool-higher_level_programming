#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ define triangle """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = pascal_triangle(n - 1)
    wor = triangle[-1]
    row = [1]

    for i in range(1, len(wor)):

        row.append(wor[i - 1] + wor[i])
    row.append(1)
    triangle.append(row)

    return triangle
