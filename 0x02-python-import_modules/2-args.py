#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    arg_str  = "argument:" if length - 1 == 1 else "arguments:"
    print("{} {}".format(length - 1, arg_str))
    for i in range(1, length, 1):
        print("{}: {}".format(i, sys.argv[i]))

