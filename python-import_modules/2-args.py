#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print("0 argument.")

    elif argc == 2:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
