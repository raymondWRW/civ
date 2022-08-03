import copy, random
from civ.civSetting import *
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from game.variable import *
from unit.settingUnit import unit_stat
from card.deck import Deck
from card.hand import Hand
from unit.unit import *
from card.card import *
from card.scienceTech import *
class Civ():
	def  __init__(self, player_index, color):
		self.color = color
		self.player_index = player_index
		self.screen_pos = (0,0)
		#resources & income
		self.material = copy.deepcopy(civ_starting_material)
		self.base_income = copy.deepcopy(civ_starting_income)
		self.tile_resource = copy.deepcopy(civ_tile_resource)
		self.building_resource = copy.deepcopy(civ_building_income)
		#cards
		self.hand = Hand(600)
		self.deck = []
		self.draw_card_cost = {'gold' : 1}
		#army
		self.unit_stat = copy.copy(unit_stat)
		#technology
		self.tech = copy.deepcopy(tech)
		self.current_science_tech = ['classical science']
		self.current_military_tech = ['standard uniform', 'spear', 'chariot']
		self.modifier = []
		#initialize
		self.start_game()
		self.exploration_counter = 0
	def start_game(self):
		for i in range(7):
			self.deck.append(PopulationGrowth())
		for i in range(3):
			self.deck.append(Warrior())
		for i in range(1):
			self.deck.append(Farm())
		for i in range(2):
			self.deck.append(ScientificAdvancement())
		for i in range(2):
			self.deck.append(MilitaryAdvancement())
		for i in range(1):
			self.deck.append(LumberCamp())
		for i in range(1):
			self.deck.append(Mine())
		for i in range(1):
			self.deck.append(Workshop())
		random.shuffle(self.deck)
		self.hand.hand.append(ScientificAdvancement())
		self.hand.hand.append(MilitaryAdvancement())
		self.hand.hand.append(PopulationGrowth())
		self.hand.hand.append(PopulationGrowth())
		self.hand.hand.append(PopulationGrowth())
		self.hand.hand.append(PopulationGrowth())
	#evaluation
	def evaluate(self, board):
		if len(data['order']) == 0:
			return
		if data['order'][0][0] == 'leftclick':
			#delete card
			if data['order'][0][1] == 'delete card':
				self.evaluate_delete_card()
				return
			#draw card
			if data['order'][0][1] == 'draw card':
				self.evaluate_draw_card()
				return
			if data['order'][0][1] == 'hand':
				self.evaluate_hand(board)
				return
			if data['order'][0][1] == 'tile':
				self.evaluate_tile(board)
				return
	def evaluate_delete_card(self):
		if len(data['order']) == 1:
			shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['board']['tile_shadow'] = shadow
			visible_screen['board']['tile_extra'] = 'unit'
		if len(data['order']) == 2:
			if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'hand':
				self.hand.hand.pop(data['order'][1][2])
				add_value(self.material, {'science' : 1})
				if 'insight' in self.modifier:
					add_value(self.material, {'gold' : 1})
			reset()
	def evaluate_draw_card(self):
		if greater(self.material, self.draw_card_cost):
			if self.draw_card():
				remove_value(self.material, self.draw_card_cost)
				self.draw_card_cost['gold'] += 1
		reset()
	def evaluate_hand(self, board):
		self.hand.hand[data['order'][0][2]].evaluate(board)
	def evaluate_tile(self, board):#unit movement
		start_tile = board[data['order'][0][2][0]][data['order'][0][2][1]]
		if start_tile.unit != None and start_tile.unit.player_index == self.player_index:
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].unit == None:
							if get_distance(data['order'][0][2], (i,j)) <= start_tile.unit.movement:
								shadow[i][j] = -1
						elif board[i][j].unit.player_index != self.player_index:
							if get_distance(data['order'][0][2], (i,j)) <= self.unit_stat[start_tile.unit.name]['attack range'] and start_tile.unit.movement != 0:
								shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'unit'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					target_tile = board[data['order'][1][2][0]][data['order'][1][2][1]]
					distance = get_distance(data['order'][0][2], data['order'][1][2])
					if distance == 0:
						pass
					elif target_tile.unit == None:
						start_tile.unit.move(start_tile, target_tile, get_distance(data['order'][0][2], data['order'][1][2]))
					elif target_tile.unit.player_index != self.player_index:
						if distance <= self.unit_stat[start_tile.unit.name]['attack range']:
							target_tile.unit.health -= self.unit_stat[start_tile.unit.name]['damage'] * start_tile.unit.health // self.unit_stat[start_tile.unit.name]['max health']
							if target_tile.unit.health <= 0:
								target_tile.unit = None
							start_tile.unit.movement = 0
				reset()
				return
		else:
			reset()
			return
	#start and end turns
	def end_turn(self, board):
		for i in range (len(board)):
			for j in range (len(board[i])):
				if board[i][j].unit != None and board[i][j].unit.player_index == self.player_index:
					if board[i][j].unit.player_index == self.player_index:
						if board[i][j].unit.movement != 0:
							if board[i][j].player_index == self.player_index:
								board[i][j].unit.health = min(self.unit_stat[board[i][j].unit.name]['max health'], self.unit_stat[board[i][j].unit.name]['max health'] // 5 + board[i][j].unit.health)
							else:
								board[i][j].player_index = self.player_index
						board[i][j].unit.movement = self.unit_stat[board[i][j].unit.name]['max movement']
						
	def start_turn(self, board):
		self.draw_card()
		self.draw_card_cost = {'gold' : 1}
		add_value(self.material, self.base_income)
		for i in range (len(board)):
			for j in range (len(board[i])):
				if board[i][j].player_index == self.player_index:
					add_value(self.material, board[i][j].tile_resource(), board[i][j].population)
	#function
	def draw_card(self):
		if len(self.hand.hand) <= MAX_HAND_SIZE:
			self.hand.hand.append(self.deck.pop(0))
			random.shuffle(self.deck)
			return True
		return False
	def add_population(self, tile, time = 1):
		if tile.player_index != self.player_index:
			return False
		if tile.population + time <= tile.max_population():
			tile.population += time
			if 'administration' in self.modifier:
				self.draw_card()
			return True
		return False
	def remove_population(self, tile, time = 1):
		if tile.player_index != self.player_index:
			return False
		if tile.population >= time:
			tile.population -= time
			return True
		return False
	def add_tile(self, tile):
		if tile.player_index != self.player_index:
			if tile.player_index != 0:
				player[tile.player_index].remove_tile(tile)
			tile.player_index = self.player_index
			if 'exploration' in self.modifier:
				self.exploration_counter += 1
				if self.exploration_counter > 2:
					self.exploration_counter -= 3
					add_value(self.material, {'research' : 1})
			return True
		return False
	def remove_tile(self, tile):
		if tile.player_index == self.player_index:
			tile.player_index = 0
			return True
		return False
	#current_player.add_unit(data['order'][1][2],  Warrior(data['player_index']))
	def add_unit(self, tile, unit):
		if tile.unit == None and tile.player_index == self.player_index:
			tile.unit = unit
			return True
		return False
	def remove_unit(self, tile):
		if tile.unit != None and tile.unit.player_index == self.player_index:
			tile.unit = None
			return True
		return False
	def add_building(self, tile, building):
		if tile.building == 'none' and tile.player_index == self.player_index:
			tile.building = building
			return True
		return False
	def remove_building(self, tile):
		if tile.buidling != 'none' and tile.player_index == self.player_index:
			tile.building = 'none'
			return True
		return False	
	def add_housing(self, tile, housing):
		if tile.housing == 'none' and tile.player_index == self.player_index:
			tile.housing = housing
			return True
		return False
	def remove_housing(self, tile):
		if tile.housing != 'none' and tile.player_index == self.player_index:
			tile.housing = 'none'
			return True
		return False