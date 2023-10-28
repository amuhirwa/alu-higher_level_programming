#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fizz = ""
        buzz = str(i)
        if i % 3 == 0:
            fizz = "Fizz"
            buzz = ""
        if i % 5 == 0:
            buzz = "Buzz"
        print(fizz+buzz, end=" ")
