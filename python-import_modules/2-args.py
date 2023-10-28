#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if (len(argv) - 1) == 0:
        print("0 arguments.")
    elif (len(argv) - 1) == 1:
        print(len(argv) - 1, "argument:")
        print("1:", argv[1])
    else:
        print(len(argv) - 1, "arguments:")
        for count, i in enumerate(argv[1:]):
            print(f'{count+1}: {i}')
