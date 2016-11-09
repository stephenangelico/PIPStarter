#!/usr/bin/env python3
# PIP 1.3.4 Bike Shop main executable
from bicycles import Bike, Shop, Customer
sunsetcycles = Shop("Sunset Valley Cycles")
alice = Customer("Alice",200,"teen")
bob = Customer("Bob",500,"lowprice")
charlie = Customer("Charlie",1000,"weight")

charlie.getbike("Carbon-fibre high-speed racing bike",sunsetcycles)
print(charlie.owned)
print("$" + str(charlie.budget))
print("$" + str(sunsetcycles.profit))