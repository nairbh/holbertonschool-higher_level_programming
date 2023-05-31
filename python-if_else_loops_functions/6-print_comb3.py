#!/usr/bin/python3
for n in range(10): 
    for k in range(n + 1, 10): 
        if n == 8 and k == 9:
            print(f"{n}{k}")

        else:
            print(f"{n}{k}, ", end="")
