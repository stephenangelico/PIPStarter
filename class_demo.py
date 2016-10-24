import random
class Musician(object):
	def __init__(self, sounds, name):
		self.name = name
		self.sounds = sounds
	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()

class Bassist(Musician):
	def __init__(self, name):
		super().__init__(["Twang", "Thrumb", "Bling"], name)

class Guitarist(Musician):
	def __init__(self, name):
		super().__init__(["Boink", "Bow", "Boom"], name)
	def tune(self):
		print("Be with you in a moment")
		print("Twoning, sproing, splang")

class Drummer(Musician):
	def __init__(self, name):
		super().__init__(["Boom", "Crash", "Ting"], name)
	def count_time(self):
		print("One, Two, Three, Four!")
	def combust(self):
		print("FOOOM!")

class Band(object):
	def __init__(self, guitarist, drummer):
		self.members = []
		self.guitarist = guitarist
		self.drummer = drummer
		self.members.append(guitarist)
		self.members.append(drummer)
		self.guitarist.tune()
	def jam(self):
		self.drummer.count_time()
		for member in self.members:
			member.solo(4)
		if random.randint(1,10) == 10:
			self.drummer.combust()
	def hire(self, musician):
		self.members.append(musician)
		print("Please welcome {} to the stage!".format(musician.name))
		print(self.members)
	#def fire(self, musician):
	#	self.members.remove(musician)
		
PIP_Rollers = Band(Guitarist("Matthew"), Drummer("Ben"))
PIP_Rollers.jam()
PIP_Rollers.hire(Bassist("Henry"))
PIP_Rollers.jam()
#PIP_Rollers.fire(Bassist("Henry"))
