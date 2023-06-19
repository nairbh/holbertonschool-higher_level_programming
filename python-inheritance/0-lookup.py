#!/usr/bin/python3
def lookup(obj):
    ret = dir(obj)
    if hasattr(obj,'__bases__'):
        for base in obj.__bases__:
            ret = ret + lookup(base)
    return ret
