#!/usr/bin/python3
def uppercase(str):
    for count, i in enumerate(str):
        if i in range(97, 123):
            chars = chr(ord(i) - 32)
        else:
            chars = i
        if count == len(str)-1:
            print("{}".format(chars))
        else:
            print("{}".format(chars), end="")
