#!/usr/bin/python3
for n in range(10):
    for k in range(10):
        if n < k:
            if n == 8 and k == 9:
                print("{:d}{:d}".format(n, k))
            else:
                print("{:d}{:d}, ".format(n, k), end='')
