#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modu = number%10
if number<0:
    modu= -(abs(number)%10)
if modu>5:
    print(f'Last digit of {number} is {modu} and is greater than 5')
elif modu==0:
    print(f'Last digit of {number} is 0 and is 0')
else:
    print(f'Last digit of {number} is {modu} and is less than 6 and not 0')
