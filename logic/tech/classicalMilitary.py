from logic.card import *
from logic.tech.tech import Tech
from data.dataGame import *
from data.dataGame import *
import random
#tier1
class Spear(Tech):
	def __init__(self):
		super().__init__(
			'spear', 
			{'research' : 5}, 
			'infantry gain 5 attack',
			'military', 
			'classical',
			[], 
			0, 
			['military tradition']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['infantry']['damage'] += 5
			self.finish_evaluate()
		reset()
class CelestialNavigation(Tech):
	def __init__(self):
		super().__init__(
			'celestial navigation', 	
			{'research' : 5}, 
			'add 3 ship card to your deck',
			'military', 
			'classical',
			['classical military'], 
			1, 
			['greek fire']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(Ship())
			player[self.index].deck.append(Ship())
			player[self.index].deck.append(Ship())
			random.shuffle(player[self.index].deck)
			self.finish_evaluate()
		reset()
class StandardUniform(Tech):
	def __init__(self):
		super().__init__(
			'standard uniform',
			{'research' : 5}, 
			'infantry gain 10 max hp',
			'military', 
			'classical',
			[], 
			0, 
			['early defense']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['infantry']['max health'] += 10
			self.finish_evaluate()
		reset()
class Chariot(Tech):
	def __init__(self):
		super().__init__(
			'chariot', 
			{'research' : 5}, 
			'add 3 cavalry to your deck',
			'military', 
			'classical',
			['classical military'], 
			1,
			['horseback riding']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(Cavalry())
			player[self.index].deck.append(Cavalry())
			player[self.index].deck.append(Cavalry())
			self.finish_evaluate()
		reset()

#tier 2
class MilitaryTradition(Tech):
	def __init__(self):
		super().__init__(
			'military tradition', 
			{'research' : 5}, 
			'Gain one extra science for every unit killed',
			'military', 
			'classical',
			['spear'], 
			1, 
			['young will serve']
		)
	def evaluate(self):
		if greater(current_player().material, self.cost):
			current_player().modifier['military tradition'] = True
			self.finish_evaluate()
		reset()
class EarlyDefense(Tech):
	def __init__(self):
		super().__init__(
			'early defense', 
			{'research' : 5}, 
			'infantry gain 5 attack',
			'military', 
			'classical',
			[], 
			0, 
			['military tradition']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['infantry']['damage'] += 5
			self.finish_evaluate()
		reset()
class HorsebackRiding(Tech):
	def __init__(self):
		super().__init__(
			'horseback riding', 	
			{'research' : 7}, 
			'cavalry gain one movement',
			'military', 
			'classical',
			['chariot'], 
			1, 
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['cavalry']['max movement'] += 1
			self.finish_evaluate()
		reset()
class greekFire(Tech):
	def __init__(self):
		super().__init__(
			'greek fire', 	
			{'research' : 7}, 
			'ship deal +5 damage',
			'military', 
			'classical',
			['celestial navigation'], 
			1, 
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['ship']['damage'] += 5
			self.finish_evaluate()
		reset()
class youngWillServe(Tech):
	def __init__(self):
		super().__init__(
			'young will serve', 	
			{'research' : 10}, 
			'add one mobolisation card',
			'military', 
			'classical',
			['military tradition', 'greek fire', 'early defense', 'horseback riding'], 
			1, 
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(Mobolization())
			random.shuffle(player[self.index].deck)
			self.finish_evaluate()
		reset()