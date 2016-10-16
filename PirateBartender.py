#!/usr/bin/env python3
# Pirate Bartender for PIP 1.3.2
import random
questions = {
	"strong": "Do ye like yer drinks strong? ",
	"salty": "Do ye like it with a salty tang? ",
	"bitter": "Are ye a lubber who likes it bitter? ",
	"sweet": "Would ye like a bit of sweetness with yer poison? ",
	"fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
customers = {}
def loyalty():
	customername = input("Avast, landlubber! Who goes there? ")
	try:
		customers[customername] == ''
	except KeyError:
		print("Ye must be new here.")
		customers[customername] = order()

	else:
		usual = input("Arr! Welcome back! Yer usual? ")
		if usual == 'y' or usual == 'Y' or usual == 'yes' or usual == 'Yes':
			print(customers[customername])
		else:
			customers[customername] = order()
	return(customers[customername])

def order():
	recipe = []
	for question in questions:
		ingredtype = input(questions[question])
		if ingredtype == 'y' or ingredtype == 'Y' or ingredtype == 'yes' or ingredtype == 'Yes':
			recipe.append(make(question))
	return(recipe)

def make(preference):
	return(random.choice(ingredients[preference]))

while __name__ == '__main__':
	print(loyalty())
	#print(customers)
	