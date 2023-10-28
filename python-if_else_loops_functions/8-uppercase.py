#!/usr/bin/python3
def uppercase(str):
    for count, i in enumerate(str):
        if i in range(65, 91):
            chars = i
        else:
            print(str)
            chars = chr(ord(i) - 32)
        if count == len(str)-1:
            print("{}".format(chars))
        else:
            print("{}".format(chars), end="")
