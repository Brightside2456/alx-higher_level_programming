#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    length = len(sys.argv)
    arg_str  = "argument" if length < 1 else "arguments"
    print("{} {}".format(length, arg_str))
    for i in range(length):
        print("{} : {}".format(i+1, sys.argv[i]))

