#!/usr/bin/python3

letter = 122
for i in range(1, 26):
    print(chr(letter), end="")
    if letter > 97:
        letter = letter - 32 - i
    else:
        letter = letter + 32 - i
