#!/usr/bin/env python3
# Simple script to play Fizz Buzz up to a certain point.
n = 1
cap = 100
print("Fizz Buzz counting up to {}".format(cap))
while n <= cap:
    if n % 15 == 0:
        print("fizz buzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")
    else:
        print(n)
    n += 1
