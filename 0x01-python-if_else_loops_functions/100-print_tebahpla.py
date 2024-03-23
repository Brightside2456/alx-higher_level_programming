#!/usr/bin/python3

letter = ""
for i in range(122, 96, -1):
    letter += chr(i) if (i % 2 == 0) else chr(i - 32)
print("{l}".format(l=letter), end="")
