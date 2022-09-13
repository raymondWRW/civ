from logic.card import *
from logic.tech.tech import Tech
from logic.modifier import modAnimalHusbandry, modFishingVillage, modPasture
from data.dataGame import *
from logic.discover import Administration, Exploration, Insight
import random
class ClassicalCivic(Tech):
	def __init__(self):
		super().__init__(
			'classical civic', 
			{}, 
			'choose one of the three bonus to begin your civilization', 
			'civic', 
			'classical',
			[], 
			0, 
			['animal husbandry', 'organization', 'flint']
		)
		self.discover = []
		self.discover.append(Administration())
		self.discover.append(Exploration())
		self.discover.append(Insight())
	def evaluate(self):
		if not greater(player[self.index].material, self.cost):
			reset()
		if len(order) == 2:
			visible_screen['discover'] = self.discover	
		if len(order) == 3:
			if order[2][0] == 'leftclick' and order[2][1] == 'discover card':
				self.discover[order[2][2]].evaluate()
				self.finish_evaluate()
			reset()
# tier 1 tech
class AnimalHusbandry(Tech):
	def __init__(self):
		super().__init__(
			'animal husbandry', 
			{'research' : 5}, 
			'unimproved grassland tile produce one extra food', 
			'civic', 
			'classical', 
			['classical civic'], 
			1, 
			['pasture']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].tile['plain']['modifier']['resource'].append(modAnimalHusbandry)
			self.finish_evaluate()
		reset()
class Organization(Tech):
	def __init__(self):
		super().__init__(
			'organization', 
			{'research' : 5}, 
			'add 3 village card to your deck', 
			'civic', 
			'classical', 
			['classical civic'], 
			1, 
			['fishing', 'irrigation', 'mathematic']
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].deck.append(Village())
			player[self.index].deck.append(Village())
			player[self.index].deck.append(Village())
			random.shuffle(player[self.index].deck)
			self.finish_evaluate()
		reset()
class Flint(Tech):
	def __init__(self):
		super().__init__(
			'flint', 
			{'research' : 5}, 
			'Mine, lumber camp gain one hammer', 
			'civic', 
			'classical',
			['classical civic'], 
			2, 
			['mathematic', 'logging', 'bronze working']
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			add_value(player[self.index].building['mine']['resource'], {'hammer' : 1})
			add_value(player[self.index].building['lumber camp']['resource'], {'hammer' : 1})
			self.finish_evaluate()
		reset()
# tier 2 tech
class Pasture(Tech):
	def __init__(self):
		super().__init__(
			'pasture',
			{'research' : 7},
			'unimproved grassland tile produce one extra horse and gold',
			'civic',
			'classical',
			['animal husbandry'],
			1,
			[]
		)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].tile['plain']['modifier']['resource'].append(modPasture)
			self.finish_evaluate()
		reset()
class Fishing(Tech):
	def __init__(self):
		super().__init__(
			'fishing', 
			{'research' : 7}, 
			'Coastal tile produce 1  extra food and 1 gold, village produce 3 gold if adjacent coastal tile', 
			'civic', 
			'classical',
			['organization'], 
			1, 
			[]
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].building['village']['modifier']['resource'].append(modFishingVillage)
			add_value(player[self.index].tile['coast']['resource'], {'food' : 1, 'gold' : 1})
			self.finish_evaluate()
		reset()
class Irrigation(Tech):
	def __init__(self):
		super().__init__(
			'irrigation', 
			{'research' : 7}, 
			'farm produce one more food and housing', 
			'civic', 
			'classical',
			['organization'], 
			1, 
			[]
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			add_value(player[self.index].building['farm']['resource'], {'food' : 1})
			player[self.index].building['farm']['housing'] += 1
			self.finish_evaluate()
		reset()
class Mathematic(Tech):
	def __init__(self):
		super().__init__(
			'mathematic', 
			{'research' : 7}, 
			'gain one extra science per turn', 
			'civic', 
			'classical',
			['organization', 'flint'], 
			2, 
			[]
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			add_value(player[self.index].base_income, {'science' : 1})
			self.finish_evaluate()
		reset()
class Logging(Tech):
	def __init__(self):
		super().__init__(
			'logging', 
			{'research' : 7}, 
			'Wood tile produce one more food, lumber camp gain one hammer', 
			'civic', 
			'classical',
			['flint'], 
			1, 
			[]
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			add_value(player[self.index].tile['wood']['resource'], {'food' : 1})
			add_value(player[self.index].building['lumber camp']['resource'], {'hammer' : 1})
			self.finish_evaluate()
		reset()
class BronzeWorking(Tech):
	def __init__(self):
		super().__init__(
			'bronze working', 
			{'research' : 7}, 
			'land unit gain 5 attack', 
			'civic', 
			'classical',
			['flint', 'spear', 'chariot'], 
			1, 
			[]
    	)
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			player[self.index].unit['infantry']['attack'] += 5
			player[self.index].unit['cavalry']['attack'] += 5
			self.finish_evaluate()
		reset()