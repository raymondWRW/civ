from logic.card import Card
from data.dataGame import *
from coreFunction.dictionaryExtended import *
class Tech(Card):
	def __init__(self, name, cost, description, type, era, requiredTech, requiredAmount, futureTech):
		super().__init__(name, cost, description)
		self.type = type
		self.era = era
		self.requiredTech = requiredTech
		self.requiredAmount = requiredAmount
		self.futureTech = futureTech
		self.researched = False
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			self.finish_evaluate()
		reset()
	def avalible(self):
		count = 0
		for i in self.requiredTech:
			if player[self.index].tech[i].researched:
				count += 1
		return count >= self.requiredAmount
	def update_tech(self):
		for i in self.futureTech:
			if player[self.index].tech[i].researched == False:
				if player[self.index].tech[i].type == 'civic':
					if not i in player[self.index].civic_tech and player[self.index].tech[i].avalible():
						player[self.index].civic_tech.append(i)
				else:
					if not i in player[self.index].military_tech and player[self.index].tech[i].avalible():
						player[self.index].military_tech.append(i)
	def finish_evaluate(self):
		self.researched = True
		player[self.index].hand.pop(order[0][2])
		if self.type == 'civic':
			player[self.index].civic_tech.remove(self.name)
		else:
			player[self.index].military_tech.remove(self.name)
		remove_value(player[self.index].material, self.cost)
		
		self.update_tech()
		reset()