import copy, random
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from data.dataGame import *
from data.dataCiv import *
from data.dataImage import CELL_SIZE
from logic.card import *
#technology
from logic.tech.classicalCivic import *
from logic.tech.classicalMilitary import *
# from card.tech.classicalCivic import *
# from card.tech.classicalCivic import *
# from card.tech.classicalCivic import *
# from card.tech.classicalCivic import *
#unit
class Civ():
	def  __init__(self, player_index, color):
		self.name = 'Civ'
		self.color = color
		self.player_index = player_index
		self.screen_pos = [0,0]
		#resources & income
		self.material = {
			'food' : 10,
			'research' : 10,
			'hammer' : 10,
			'gold' : 10,
			'horse' : 0
		}
		self.income = {
    		'food' : 1,
    		'research' : 2,
    		'hammer' : 1,
    		'gold' : 1
        }
		self.tile = None
		self.building = None
		self.unit = None
		self.tech = None
		self.modifier = []
	# 	#cards
		self.hand = []
		self.deck = []
		self.hand_size = 8
		self.draw_card_cost = {'gold' : 2}
	# 	#technology
		self.civic_tech = ['classical civic']
		self.military_tech = ['spear', 'standard uniform', 'chariot','celestial navigation']
	def valid_starting_tile(self, start_pos):
		if board[start_pos[0]][start_pos[1]].name != 'plain':
			return False
		for i in start_civ_placement:
			if get_distance(start_pos, i) < 7:
				return False	
		return True
	def start_tile(self):
		array_valid_index = []
		for i in range(1, len(board) - 1):
			for j in range(1, len(board[i]) - 1):
				if self.valid_starting_tile((i,j)):
					array_valid_index.append((i,j))
		if len(array_valid_index) != 0:
			start_tile = random.choice(array_valid_index)
			start_civ_placement.append(start_tile)
			board[start_tile[0]][start_tile[1]].player_index = self.player_index
			edge = get_border_index(start_tile)
			for k in edge:
				board[k[0]][k[1]].player_index = self.player_index
			self.screen_pos = [600 - start_tile[1] * CELL_SIZE * 12 - CELL_SIZE * 6 * (i % 2), 325 - start_tile[0] * CELL_SIZE * 12]
			return True
		return False
	def start_game(self):
		#tile
		self.start_tile()
		#initialize dictionary
		self.tile = copy.deepcopy(civTile)
		self.building = copy.deepcopy(civBuilding)
		self.unit = copy.deepcopy(civUnit)
		self.tech = {	
            #classical science
			'classical civic' : ClassicalCivic(),
			'animal husbandry' : AnimalHusbandry(),
			'organization' : Organization(),
			'flint' : Flint(),
			'pasture' : Pasture(),
			'fishing' : Fishing(),
			'irrigation' : Irrigation(),
			'mathematic' : Mathematic(),
			'logging' : Logging(),
			'irrigation' : Irrigation(),
			'bronze working' : BronzeWorking(),
			#classical military
			'spear' : Spear(),
			'celestial navigation' : CelestialNavigation(),
			'standard uniform' : StandardUniform(),
			'chariot' : Chariot(),
			'horseback riding' : HorsebackRiding(),
			'early defense' : EarlyDefense(),
			'military tradition' : MilitaryTradition(),
			'greek fire' : greekFire(),
			'young will serve' : youngWillServe()
		}
		#deck
		for i in range(17):
			self.deck.append(PopulationGrowth())
		for i in range(3):
			self.deck.append(Warrior())
		for i in range(2):
			self.deck.append(CivicAdvancement())
		for i in range(2):
			self.deck.append(MilitaryAdvancement())
		for i in range(2):
			self.deck.append(Farm())
		for i in range(2):
			self.deck.append(Mine())
		for i in range(2):
			self.deck.append(Workshop())
		for i in range(2):
			self.deck.append(LumberCamp())
		random.shuffle(self.deck)
		self.hand.append(CivicAdvancement())
		self.hand.append(MilitaryAdvancement())
		self.hand.append(PopulationGrowth())
		self.hand.append(PopulationGrowth())
		self.hand.append(PopulationGrowth())
	#evaluation
	def evaluate(self):
		if len(order) == 0:
			return
		if order[0][0] == 'leftclick':
			#delete card
			if order[0][1] == 'delete card':
				self.evaluate_delete_card()
				return
			#draw card
			if order[0][1] == 'draw card':
				self.evaluate_draw_card()
				return
			if order[0][1] == 'hand':
				self.evaluate_hand()
				return
			if order[0][1] == 'tile':
				self.evaluate_tile()
				return
	def evaluate_delete_card(self):
		if len(order) == 1:
			visible_screen['shadow'] = [[True for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['tile extra'] = 'unit'
		if len(order) == 2:
			if order[1][0] == 'leftclick' and order[1][1] == 'hand':
				self.hand.pop(order[1][2])
				if self.modifier['insight']:
					add_value(self.material, {'gold' : 1})
				add_value(self.material, {'hammer' : 1})
			reset()
	def evaluate_draw_card(self):
		if greater(self.material, self.draw_card_cost):
			if self.draw_card():
				remove_value(self.material, self.draw_card_cost)
				self.draw_card_cost['gold'] += 1
		reset()
	def evaluate_hand(self):
		self.hand[order[0][2]].evaluate()
	def evaluate_tile(self):#unit movement
		start_tile = board[order[0][2][0]][order[0][2][1]]
		if start_tile.unit != None and start_tile.unit.player_index == self.player_index:
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						dis = get_distance(order[0][2], (i,j))
						if board[i][j].unit == None:
							if dis <= start_tile.unit.movement:
								visible_screen['shadow'][i][j] = False
							else:
								visible_screen['shadow'][i][j] = True
						elif board[i][j].unit.player_index != self.player_index:
							if 0 < dis <= self.unit[start_tile.unit.name]['attack range'] and start_tile.unit.movement != 0:
								visible_screen['shadow'][i][j] = False
							else:
								visible_screen['shadow'][i][j] = True
						else:
							visible_screen['shadow'][i][j] = True
				return
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					start_tile.unit.move()
					# target_tile = board[order[1][2][0]][order[1][2][1]]
					# distance = get_distance(order[0][2], order[1][2])
					# if distance == 0:
					# 	pass
					# elif target_tile.unit == None:
					# 	if distance <= start_tile.unit.movement:
					# 		start_tile.unit.movement -= distance
					# 		target_tile.unit = start_tile.unit
					# 		start_tile.unit = None
					# elif target_tile.unit.player_index != self.player_index:
					# 	if distance <= self.unit[start_tile.unit.name]['attack range'] and start_tile.movement != 0:
					# 		target_tile.unit.health -= self.unit_stat[start_tile.unit.name]['damage'] * start_tile.unit.health // self.unit_stat[start_tile.unit.name]['max health']
					# 		if target_tile.unit.health <= 0:
					# 			target_tile.unit = None
					# 		start_tile.unit.movement = 0
		reset()

	#start and end turns
	def end_turn(self):
		for i in range (len(board)):
			for j in range (len(board[i])):
				if board[i][j].unit != None and board[i][j].unit.player_index == self.player_index:
					board[i][j].unit.next_turn((i,j))				
	def start_turn(self):
		self.draw_card()
		self.draw_card()
		self.draw_card_cost = {'gold' : 1}
		add_value(self.material, self.income)
		for i in range (len(board)):
			for j in range (len(board[i])):
				if board[i][j].player_index == self.player_index:
					add_value(self.material, board[i][j].tile_resource(), board[i][j].population)
	#function
	def draw_card(self):
		if len(self.hand) <= self.hand_size:
			if len(self.deck) == 0:
				self.hand.append(PopulationGrowth())
			else:
				self.hand.append(self.deck.pop(0))
			return True
		return False
	def add_population(self, tile, time = 1):
		if tile.player_index != self.player_index:
			return False
		if tile.population + time <= tile.max_population():
			tile.population += time
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
			if tile.player_index == 0:
				if 'exploration3' in self.modifier:
					self.modifier.remove('exploration3')	
					self.modifier.append('exploration2')
				elif 'exploration2' in self.modifier:
					self.modifier.remove('exploration2')	
					self.modifier.append('exploration1')
				elif 'exploration1' in self.modifier:
					add_value(self.material, {'research' : 1})
					self.modifier.remove('exploration1')	
					self.modifier.append('exploration3')
			tile.player_index = self.player_index
			return True
		return False
	def remove_tile(self, tile):
		if tile.player_index == self.player_index:
			tile.player_index = 0
			return True
		return False
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
			if 'administration' in self.modifier:
				self.draw_card()
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