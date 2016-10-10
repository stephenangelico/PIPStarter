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
preferences = {}
recipe = []
# Psuedo-code follows
def order():
    for dict_key in questions:
        ingredtype = input(questions[dict_key])
        if ingredtype == 'y' or ingredtype == 'Y' or ingredtype == 'yes' or ingredtype == 'Yes':
           ingredtype = True
        else:
           ingredtype = False
        preferences[dict_key] = ingredtype

def make():
   for preference in preferences:
       if preferences[preference] == True:
           recipe.append(random.choice(ingredients[preference]))

order()
print(preferences)
make()
print(recipe)