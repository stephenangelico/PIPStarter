#!/usr/bin/env python3
# Simple script to play Fizz Buzz up to a certain point.
import sys
try:
    int(sys.argv[1])
except ValueError:
    print("Can't convert {} to an integer".format(sys.argv[1]))
    sys.exit(1)
except IndexError:
    pass

if len(sys.argv) == 1:
    incap = input("To what integer do you wish to play? (default = 100) ")
else:
    incap = sys.argv[1]

cap = 0
while cap == 0:
    try:
        if incap != '':
            cap = int(incap)
        else:
            cap = 100
    except ValueError:
        print("Can't convert {} to an integer".format(incap))
        incap = input("To what integer do you wish to play? (default = 100) ")

n = 1
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
