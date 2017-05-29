#!/usr/bin/env python3



def fizzbuzzmain(cap):
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
    
def fizzbuzz(n):
    ret = ""
    if not (n%3):
        ret += "fizz"
    if not (n%5):
        ret += "buzz"
    return ret or str(n)
    
def fizzbuzz_goodtest(f):
    output = []
    for n in range(100):
        output.append(str(f(n) + "\n"))

    expected = open("fizzbuzz-output.txt", "r")
    i = 0
    for line in expected:
        if line == output[i]:
            print("Success!")
            i += 1
        else:
            print("Nope. Try Again.")