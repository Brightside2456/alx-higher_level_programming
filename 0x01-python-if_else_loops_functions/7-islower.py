#!/usr/bin/python3

def islower(c):
    uni_point = ord(c)
    if uni_point > 96 and uni_point < 123:
        return True
    return False
