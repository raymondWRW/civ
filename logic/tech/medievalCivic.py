from logic.card import *
from logic.tech.tech import Tech
from data.dataGame import *
from logic.card import PopulationBoom, Sanction, Town, BlackSmith
class MedievalCivic(Tech):
	def __init__(self):
		super().__init__(
			'medieval civic', 
			{}, 
			'Add sanction. Population boom card to your deck, increase housing on all tiles', 
			'civic', 
			'medieval',
			['pasture', 'fishing', 'irrigation', 'mathematic', 'logging', 'bronze working', 'young will serve'], 
			2, 
			['centralization', 'iron working', 'writing', 'medieval military']
		)
	def evaluate(self):	
		for i,j in player[self.index].tile:
			j['housing'] += 1
		player[self.index].append(PopulationBoom)
		player[self.index].append(Sanction)
		self.finish_evaluate()
		reset()
	def finish_evaluate(self):
		self.researched = True
		player[self.index].hand.pop(order[0][2])
		player[self.index].civic_tech.clear()
		player[self.index].military_tech.clear()
		player[self.index].civic_tech.append('centralization')
		player[self.index].civic_tech.append('iron working')
		player[self.index].civic_tech.append('writing')
		player[self.index].military_tech.append('medieval military')
		reset()
# tier 1 tech
class Centralization(Tech):
	def __init__(self):
		super().__init__(
			'centralization', 
			{'research' : 10}, 
			'Upgrade your village card, if you don’t have village card add three towns instead', 
			'civic', 
			'medieval', 
			['medieval civic'], 
			1, 
			['serfdom', 'efficient administration']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(Town())
			player[self.index].deck.append(Town())
			player[self.index].deck.append(Town())
			self.finish_evaluate()
		reset()
class IronWorking(Tech):
	def __init__(self):
		super().__init__(
			'iron working', 
			{'research' : 10}, 
			'add 3 blacksmith to your deck', 
			'civic', 
			'medieval', 
			['medieval civic'], 
			1, 
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(BlackSmith())
			player[self.index].deck.append(BlackSmith())
			player[self.index].deck.append(BlackSmith())
			self.finish_evaluate()
		reset()
class Writing(Tech):
	def __init__(self):
		super().__init__(
			'writing', 
			{'research' : 10}, 
			'add 3 blacksmith to your deck', 
			'civic', 
			'medieval', 
			['medieval civic'], 
			1, 
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(BlackSmith())
			player[self.index].deck.append(BlackSmith())
			player[self.index].deck.append(BlackSmith())
			self.finish_evaluate()
		reset()
#tier 2
  
# class Philosophy(Tech):