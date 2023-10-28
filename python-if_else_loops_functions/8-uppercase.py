#!/usr/bin/python3
def uppercase(str):
    for count, i in enumerate(str):
        if ord(i) in range(97, 123):
            chars = chr(ord(i) - 32)
        else:
            chars = i
        print("{}".format(chars), end="")
    print("")
