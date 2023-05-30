#!/usr/bin/python3

for n in range(97, 123):
    
    if n == ord('e') or n == ord('q'):
        
        continue
    print("{:c}".format(n), end='')

