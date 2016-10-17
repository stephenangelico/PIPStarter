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
# Known bug: Stock not decreased for return orders
ingredstock = {
	"glug of rum": 5,
	"slug of whisky": 5,
	"splash of gin": 5,
	"olive on a stick": 5,
	"salt-dusted rim": 5,
	"rasher of bacon": 5,
	"shake of bitters": 5,
	"splash of tonic": 5,
	"twist of lemon peel": 5,
	"sugar cube": 5,
	"spoonful of honey": 5,
	"spash of cola": 5,
	"slice of orange": 5,
	"dash of cassis": 5,
	"cherry on top": 5,
}
ingredmapping = {
	"glug of rum": 1,
	"slug of whisky": 2,
	"splash of gin": 4,
	"olive on a stick": 8,
	"salt-dusted rim": 16,
	"rasher of bacon": 32,
	"shake of bitters": 64,
	"splash of tonic": 128,
	"twist of lemon peel": 256,
	"sugar cube": 512,
	"spoonful of honey": 1024,
	"spash of cola": 2048,
	"slice of orange": 4096,
	"dash of cassis": 8192,
	"cherry on top": 16384,
}
# Known bug: not enough naming possibilities for all ingredients
# Known bug: no way to handle random choosing collisions
nameadjectives = ["Acidic","Barnyard","Bright","Charcoal","Chocolaty","Creamy","Elegant","Expressive","Grassy","Juicy","Lean","Musty","Oxidized","Round","Smokey","Spicy","Supple","Tart","Vanillin","Velvety"]
namenouns = ["Apple","Blackcurrant","Blood Orange","Dried Lime","Ginger","Lychee","Mace","Mango","Mulberry","Nectarine","Nutmeg","Quince","Papaya","Passionfruit","Pineapple","Raspberry","Rose","Sarsaparilla","Watermelon","Zest"]
drinknames = {}
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
			pass
		else:
			customers[customername] = order()
	return(customers[customername])

def order():
	recipe = []
	for question in questions:
		ingredtype = input(questions[question])
		if ingredtype == 'y' or ingredtype == 'Y' or ingredtype == 'yes' or ingredtype == 'Yes':
			recipe.append(make(question))
	for ingredient in recipe:
		ingredstock[ingredient] -= 1
	return(recipe,drinkname(recipe))

def make(preference):
	return(random.choice(ingredients[preference]))

def drinkname(recipe):
	drinkid = 0
	for ingredient in recipe:
		drinkid += ingredmapping[ingredient]
	try:
		drinknames[drinkid] == ''
	except KeyError:
		drinknames[drinkid] = random.choice(nameadjectives) + ' ' + random.choice(namenouns)
	return(drinknames[drinkid])

def restock():
	for ingredient in ingredstock:
		if ingredstock == 0:
			print("Arr! Be back soon! Need fresh stock of {}.".format(ingredient))
			ingredstock[ingredient] += 5

while __name__ == '__main__':
	print(loyalty())
	restock()
	#print(customers)
	