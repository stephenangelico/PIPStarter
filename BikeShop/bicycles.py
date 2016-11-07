# Bike Shop class and function definitions
class Bike(object):
	#Needs model name, weight and prod cost
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost

class Shop(object):
	#Needs name and inventory
	#Must manage and track profits
	def __init__(self, name):
		self.name = name
		self.trainer = Bike("Training bike for kids",15,150) 
		self.bmx = Bike("BMX stunt bike",20,275)
		self.teen = Bike("20-inch hybrid road-mountain bike",25,220)
		self.mountain = Bike("Shock-absorbing foldable mountain bike",30,275)
		self.road = Bike("Lightweight 14-speed road bike",25,450)
		self.racing = Bike("Carbon-fibre high-speed racing bike",15,800)
		self.inventory = {
				"Training bike for kids":
					{"Count":2, "Weight":self.trainer.weight, "Cost":self.trainer.cost,},
				"BMX stunt bike":
					{"Count":2, "Weight":self.bmx.weight, "Cost":self.bmx.cost,},
				"20-inch hybrid road-mountain bike":
					{"Count":2, "Weight":self.teen.weight, "Cost":self.teen.cost,},
				"Shock-absorbing foldable mountain bike":
					{"Count":2, "Weight":self.mountain.weight, "Cost":self.mountain.cost,},
				"Lightweight 14-speed road bike":
					{"Count":2, "Weight":self.road.weight, "Cost":self.road.cost,},
				"Carbon-fibre high-speed racing bike":
					{"Count":2, "Weight":self.racing.weight, "Cost":self.racing.cost,},
				}
		self.margin = 0.2
		self.profit = 0
	def getprice(self, model):
		return self.inventory[model]["Cost"] * (1 + self.margin)
	def sellbike(self, model):
		self.profit += self.inventory[model]["Cost"] * self.margin
		self.inventory[model]["Count"] -= 1

class Customer(object):
	#Needs name and funds
	#Must be able to purchase and own a bike
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget
		self.owned = ''
	def pricecheck(self, model, shopname):
		return shopname.getprice(model)
	#def choosemodel():
	def getbike(self, model, shopname):
		#Get model price and check if within budget,
		price = self.pricecheck(model, shopname)
		if price > self.budget:
			print(self.name + " can't afford a " + model + " from " + shopname)
		else:
			#deduct funds from budget,
			self.budget -= price
			shopname.sellbike(model)
			#record what model is now owned
			self.owned = model
