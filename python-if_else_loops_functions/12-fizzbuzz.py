#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fizz = str(i)
        buzz = ""
        if i%3 == 0:
            fizz = "fizz"
        if i%5 == 0:
            buzz = "buzz"
        
        print(fizz+buzz,end=" ")
