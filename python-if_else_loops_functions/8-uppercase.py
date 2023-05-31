#!/usr/bin/python3
def uppercase(str):
    for n in range(0, len(str)):
            ch = ord(str[n])
            if ch >= 96 and ch <= 122:
                ch = ch - 32
            print("{:c}".format(ch), end="")
    print("")
