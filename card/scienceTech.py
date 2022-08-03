from card.card import *
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
	def finish_evaluate(self):
		# current_player = player[data['player_index']]
		# remove_value(current_player.material, self.cost)
		# current_player.hand.hand.pop(data['order'][0][2])
		# current_player.current_science_tech.remove(self.name)
		# self.update_tech()
		# reset()
		current_player = player[data['player_index']]
		current_player.hand.hand.pop(data['order'][0][2])
		current_player.current_science_tech.remove(self.name)
		remove_value(current_player.material, self.cost)
		self.update_tech()
		reset()

class Administration(Card):
	def __init__(self):
		super().__init__('administration', {}, 'draw a card after you played population growth')
	def evaluate(self):
		player[data['player_index']].modifier.append('administration')

class Exploration(Card):
	def __init__(self):
		super().__init__('exploration', {}, 'gain one science for every 3 tile added to your country')
	def evaluate(self):
		player[data['player_index']].modifier.append('exploration')

class Insight(Card):
	def __init__(self):
		super().__init__('insight', {}, 'gain one gold when destroying a card')
	def evaluate(self):
		player[data['player_index']].modifier.append('insight')

class ClassicalScience(ScienceTech):
	def __init__(self):
		super().__init__('classical science', {'research' : 5}, 'discover a classical science technology')
		self.discover = Hand(300)
		self.discover.hand.append(Administration())
		self.discover.hand.append(Exploration())
		self.discover.hand.append(Insight())
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if not greater(current_player.material, self.cost):
			reset()
		if len(data['order']) == 2:
			visible_screen['discover'] = self.discover	
		if len(data['order']) == 3:
			if data['order'][2][0] == 'leftclick' and data['order'][2][1] == 'discover card':
				self.discover.hand[data['order'][2][2]].evaluate()
				self.finish_evaluate()
			reset()

class AnimalHusbandry(ScienceTech):
	def __init__(self):
		super().__init__('animal husbandry', {'research' : 5}, 'grassland tile produce one extra food')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.tile_resource['plain']['resource']['food'] += 1
			self.finish_evaluate()
		reset()

class Pasture(ScienceTech):
	def __init__(self):
		super().__init__('pasture', {'research' : 7}, 'grassland tile produce one extra horse')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			add_value(current_player.tile_resource['plain']['resource'], {'horse' : 1})
			# current_player.tile_resource['plain']['resource']['hourse'] += 1
			self.finish_evaluate()
		reset()

class Organization(ScienceTech):
	def __init__(self):
		super().__init__('organization', {'research' : 5}, 'add 3 village card to your deck')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.deck.append(Village())
			current_player.deck.append(Village())
			current_player.deck.append(Village())
			self.finish_evaluate()
		reset()

class Fishing(ScienceTech):
	def __init__(self):
		super().__init__('fishing', {'research' : 7}, 'Coastal tile produce 1  extra food and gold')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.building_resource['village']['modifier'].append('fishing')
			add_value(current_player.tile_resource['coast']['resource'], {'food' : 1, 'gold' : 1})
			self.finish_evaluate()
		reset()
  
class Irrigation(ScienceTech):
	def __init__(self):
		super().__init__('irrigation', {'research' : 7}, 'farm produce one more food and one more housing')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.building_resource['farm']['resource']['food'] += 1
			current_player.building_resource['farm']['housing'] += 1
			self.finish_evaluate()
		reset()

class Mathematic(ScienceTech):
	def __init__(self):
		super().__init__('mathematic', {'research' : 7}, 'gain one science per turn')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			add_value(current_player.base_income, {'science' : 1})
			self.finish_evaluate()
		reset()

class Flint(ScienceTech):
	def __init__(self):
		super().__init__('flint', {'research' : 5}, 'Mine, lumber camp gain one hammer')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			add_value(current_player.building_resource['mine']['resource'], {'hammer' : 1})
			add_value(current_player.building_resource['lumber camp']['resource'], {'hammer' : 1})
			self.finish_evaluate()
		reset()
  
class Logging(ScienceTech):
	def __init__(self):
		super().__init__('logging', {'research' : 5}, 'Wood tile produce one more food, lumber camp gain one hammer')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			add_value(current_player.tile_resource['wood']['resource'], {'food' : 1})
			add_value(current_player.building_resource['lumber camp']['resource'], {'hammer' : 1})
			self.finish_evaluate()
		reset()
  
class BronzeWorking(ScienceTech):
	def __init__(self):
		super().__init__('bronze working', {'research' : 5}, 'land unit gain 5 attack')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			current_player.unit_stat['warrior']['attack'] += 5
			current_player.unit_stat['cavalry']['attack'] += 5
			self.finish_evaluate()
		reset()

# class Fishing(ScienceTech):
# class Irrigation(ScienceTech):
# class Mathematic(ScienceTech):
# class Flint(ScienceTech):
# class Logging(ScienceTech):
# class BronzeWorking(ScienceTech):
