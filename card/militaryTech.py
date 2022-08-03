from card.card import *
from game.variable import *
from card.hand import *
from coreFunction.dictionaryExtended import *
class MilitaryTech(Card):
	def __init__(self, name, cost, description):
		super().__init__(name, cost, description)
	def evaluate(self, board):
		return True
	def avalible(self):
		current_player = player[data['player_index']]
		required = current_player.tech[self.name]['required']['amount']
		for i in current_player.tech[self.name]['required']['tech']:
			if current_player.tech[i]['researched']:
				required -= 1
		return required <= 0
	def update_tech(self):
		current_player = player[data['player_index']]
		current_player.tech[self.name]['researched'] = True
		for i in current_player.tech[self.name]['future tech']:
			if current_player.tech[i]['researched'] == False:
				if not i in current_player.current_military_tech:
					if current_player.tech[i]['tech'].avalible():
						current_player.current_military_tech.append(i)
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			self.finish_evaluate()
		reset()
	def finish_evaluate(self):
		current_player = player[data['player_index']]
		current_player.hand.hand.pop(data['order'][0][2])
		current_player.current_military_tech.remove(self.name)
		remove_value(current_player.material, self.cost)
		self.update_tech()
		reset()

class StandardUniform(MilitaryTech):
	def __init__(self):
		super().__init__('standard uniform', {'research' : 5}, 'warrior gain 10 max hp')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.unit_stat['warrior']['max health'] += 10
			self.finish_evaluate()
		reset()

class MilitaryTradition(MilitaryTech):
	def __init__(self):
		super().__init__('military tradition', {'research' : 5}, 'Gain one science for every unit killed')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.modifier.append('military tradition')
			self.finish_evaluate()
		reset()
class Spear(MilitaryTech):
	def __init__(self):
		super().__init__('spear', {'research' : 5}, 'warrior gain 5 attack')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.unit_stat['warrior']['damage'] += 5
			self.finish_evaluate()
		reset()
# class Wall(Card):
class Chariot(MilitaryTech):
	def __init__(self):
		super().__init__('chariot', {'research' : 5}, 'add 3 cavalry to your deck')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.deck.append(Cavalry())
			current_player.deck.append(Cavalry())
			current_player.deck.append(Cavalry())
			self.finish_evaluate()
		reset()
class HorsebackRiding(MilitaryTech):
	def __init__(self):
		super().__init__('horseback riding', {'research' : 7}, 'cavalry gain one speed')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.unit_stat['cavalry']['max movement'] += 1
			self.finish_evaluate()
		reset()
