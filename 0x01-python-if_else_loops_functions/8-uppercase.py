#!/usr/bin/python3

def uppercase(str):
    upper_string = ""
    for s in str:
       char_val = ord(s)
       if char_val > 96 and char_val < 123:
           upper_string += chr(char_val - 32)
       else:
           upper_string += s
    print(upper_string)
