#!/usr/bin/python3
for n in range(0, 9):
    for k in range(n + 1, 9):

            print("{:02d}, ".format(n * 10 + k), end="")

print("{:02d}".format(89))
