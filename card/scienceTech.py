from card.card import Card
from game.variable import *
from card.hand import *
from coreFunction.dictionaryExtended import *
class ScienceTech(Card):
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
				if not i in current_player.current_science_tech:
					if current_player.tech[i]['tech'].avalible():
						current_player.current_science_tech.append(i)
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			remove_value(current_player.material, self.cost)
			self.update_tech()
			current_player.deck.append(current_player.hand.hand.pop(data['order'][0][2]))
			current_player.current_science_tech.remove(self.name)
		reset()

class Administration(Card):
	def __init__(self):
		super().__init__('administration', {}, 'draw a card after you played population growth')
	def evaluate(self):
		player[data['player_index']].modifier.append('administration')

class EfficiantProduction(Card):
	def __init__(self):
		super().__init__('efficiant production', {}, 'efficiant production')
	def evaluate(self):
		player[data['player_index']].modifier.append('scientific conversation')

class Insight(Card):
	def __init__(self):
		super().__init__('insight', {}, 'insight')
	def evaluate(self):
		player[data['player_index']].modifier.append('insight')

class ClassicalScience(ScienceTech):
	def __init__(self):
		super().__init__('classical science', {'research' : 5}, 'discover a classical science technology')
		self.discover = Hand(300)
		self.discover.hand.append(Administration())
		self.discover.hand.append(EfficiantProduction())
		self.discover.hand.append(Insight())
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if not greater(current_player.material, self.cost):
			reset()
		if len(data['order']) == 2:
			shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['board']['tile_shadow'] = shadow
			visible_screen['discover'] = self.discover	
		if len(data['order']) == 3:
			if data['order'][2][0] == 'leftclick' and data['order'][2][1] == 'discover card':
				self.discover.hand[data['order'][2][2]].evaluate()
				remove_value(current_player.material, self.cost)
				self.update_tech()
				current_player.deck.add_card(current_player.hand.hand.pop(data['order'][0][2]))
				current_player.current_science_tech.remove(self.name)
			reset()

class AnimalHusbandry(ScienceTech):
	def __init__(self):
		super().__init__('animal husbandry', {'research' : 5}, 'grassland tile produce one extra food')
		self.future_tech = ['pasture']
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			remove_value(current_player.material, self.cost)
			current_player.tile_resource['plain']['resource']['food'] += 1
			self.update_tech()
			current_player.deck.add_card(current_player.hand.hand.pop(data['order'][0][2]))
			current_player.current_science_tech.remove(self.name)
		reset()

class Pasture(ScienceTech):
	def __init__(self):
		super().__init__('pasture', {'research' : 7}, 'grassland tile produce one extra horse')
		self.future_tech = []
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			remove_value(current_player.material, self.cost)
			current_player.tile_resource['plain']['resource']['hourse'] += 1
			self.update_tech()
			current_player.deck.add_card(current_player.hand.hand.pop(data['order'][0][2]))
			current_player.current_science_tech.remove(self.name)
		reset()
class Organization(ScienceTech):
	def __init__(self):
		super().__init__('organization', {'research' : 5}, 'add 3 village card to your deck')
		self.future_tech = []
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			remove_value(current_player.material, self.cost)
			self.self.deck[0]
			self.update_tech()
			current_player.deck.add_card(current_player.hand.hand.pop(data['order'][0][2]))
			current_player.current_science_tech.remove(self.name)
		reset()