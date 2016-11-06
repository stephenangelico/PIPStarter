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

class Customer(object):
	#Needs name and funds
	#Must be able to purchase and own a bike
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget
	def getbike(model):
		#Get model price and check if within budget,
		#deduct funds from budget,
		#record what model is now owned
	
