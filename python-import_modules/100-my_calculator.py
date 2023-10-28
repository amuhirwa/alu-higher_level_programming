#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = sys.argv[2]
    c = int(sys.argv[3])
    if b not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if b == "+":
        print(f'{a} + {c} = {add(a,c)}')
    elif b == "-":
        print(f'{a} - {c} = {sub(a,c)}')
    elif b == "*":
        print(f'{a} * {c} = {mul(a,c)}')
    elif b == "/":
        print(f'{a} / {c} = {div(a,c)}')
