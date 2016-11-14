#!/usr/bin/env python3
# PIP 1.3.4 Bike Shop main executable
from bicycles import Bike, Shop, Customer
sunsetcycles = Shop("Sunset Valley Cycles")
alice = Customer("Alice",200,"teen")
bob = Customer("Bob",500,"lowprice")
charlie = Customer("Charlie",1000,"weight")

alice.choosemodel(sunsetcycles)
print(alice.name + " now owns a " + alice.owned + " and has $" + str(alice.budget) + " remaining.\n")
bob.choosemodel(sunsetcycles)
print(bob.name + " now owns a " + bob.owned + " and has $" + str(bob.budget) + " remaining.\n")
charlie.choosemodel(sunsetcycles)
print(charlie.name + " now owns a " + charlie.owned + " and has $" + str(charlie.budget) + " remaining.\n")
print("Remaining inventory for {}:".format(sunsetcycles.name))
for model in sunsetcycles.inventory:
	print(model + ": " + str(sunsetcycles.inventory[model]["Count"]))
print("\n" + sunsetcycles.name + " has made a profit of $" + str(sunsetcycles.profit))