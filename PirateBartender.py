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

while __name__ == '__main__':
	print(loyalty())
	#print(customers)
	