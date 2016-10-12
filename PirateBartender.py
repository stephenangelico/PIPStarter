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
preferences = {}
recipe = []
def loyalty():
	customername = input("Avast, landlubber! Who goes there? ")
	try:
		customers[customername] == ''
	except KeyError:
		print("Ye must be new here.")
		order()
		make()
		customers[customername] = recipe

	else:
		usual = input("Arr! Welcome back! Yer usual? ")
		if usual == 'y' or usual == 'Y' or usual == 'yes' or usual == 'Yes':
			print(customers[customername])
		else:
			order()
			make()
			customers[customername] = recipe

def order():
	del recipe[:]
	for question in questions:
		ingredtype = input(questions[question])
		if ingredtype == 'y' or ingredtype == 'Y' or ingredtype == 'yes' or ingredtype == 'Yes':
			ingredtype = True
		else:
			ingredtype = False
		preferences[question] = ingredtype

def make():
	for preference in preferences:
		if preferences[preference] == True:
			recipe.append(random.choice(ingredients[preference]))

while __name__ == '__main__':
	loyalty()
	print(preferences)
	print(recipe)
	print(customers)
	preferences.clear()
