#!/usr/bin/python3
def uppercase(str):
    for count, i in enumerate(str):
        if i in range(65, 91):
            chars = i
        elif i in range(97, 123):
            chars = chr(ord(i) - 32)
        if count ==l en(str)-1:
            print(chars)
        else:
            print(chars, end="")
