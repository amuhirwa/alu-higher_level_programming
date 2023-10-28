#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = argv[2]
    c = int(argv[3])
    if b not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if b == "+":
        print(f'{a} + {c} = {add(a,c)}')
    elif b == "-":
        print(f'{a} - {c} = {sub(a,c)}')
    elif b == "*":
        print(f'{a} * {c} = {mul(a,c)}')
    elif b == "/":
        print(f'{a} / {c} = {div(a,c)}')
