import pygame
from card.settingCard import *
from card.hand import Hand
from coreFunction.dictionaryExtended import *
from unit.unit import *
from unit.settingUnit import *
from game.variable import *
pygame.init()
#cost:	
class Card:
	def  __init__(self, name = 'card', cost = {}, description = "template"):
		self.name = name	
		self.cost = cost
		self.description = description
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			remove_value(player.material, self.cost)
		player.hand.hand.pop(data['order'][0][2])
		reset()
	def finish_evaluate(self):
		current_player = player[data['player_index']]
		remove_value(current_player.material, self.cost)
		current_player.deck.append(current_player.hand.hand.pop(data['order'][0][2]))
		reset()

class PopulationGrowth(Card):
	def  __init__(self):
		super().__init__('population growth', {'food': 5}, "give a friendly tile 1 population")
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].population < board[i][j].max_population():
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
				return
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_population(board[data['order'][1][2][0]][data['order'][1][2][1]]):
						self.finish_evaluate()

		reset()

class Warrior(Card):
	def  __init__(self):
		super().__init__('warrior', {'food' : 10 ,'hammer' : 1,'gold' : 5}, 'deploy a warrior on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].population != 0 and board[i][j].name != 'ocean' and board[i][j] != 'coast':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if board[data['order'][1][2][0]][data['order'][1][2][1]].name != 'ocean' and board[data['order'][1][2][0]][data['order'][1][2][1]].name != 'coast':
						if current_player.remove_population(board[data['order'][1][2][0]][data['order'][1][2][1]]):
							current_player.add_unit(board[data['order'][1][2][0]][data['order'][1][2][1]],  unitWarrior(data['player_index']))
							self.finish_evaluate()
				reset()
		else:
			reset()

class Farm(Card):
	def  __init__(self):
		super().__init__('farm', {'food' : 5,'hammer' : 1}, 'build a building on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].building == 'none':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_building(board[data['order'][1][2][0]][data['order'][1][2][1]], 'farm'):
						self.finish_evaluate()
				reset()
		else:
			reset()

class Workshop(Card):
	def  __init__(self):
		super().__init__('workshop', {'food' : 5,'hammer' : 1}, 'build a workshop on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)): 
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].building == 'none':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_building(board[data['order'][1][2][0]][data['order'][1][2][1]], 'workshop'):
						self.finish_evaluate()
				reset()
		else:
			reset()

class Mine(Card):
	def  __init__(self):
		super().__init__('mine', {'food' : 5,'hammer' : 1}, 'build a mine on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)): 
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].building == 'none':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_building(board[data['order'][1][2][0]][data['order'][1][2][1]], 'mine'):
						self.finish_evaluate()
				reset()
		else:
			reset()

class LumberCamp(Card):
	def  __init__(self):
		super().__init__('lumber camp', {'food' : 5,'hammer' : 1}, 'build a lumber camp on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)): 
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].building == 'none':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_building(board[data['order'][1][2][0]][data['order'][1][2][1]], 'lumber camp'):
						self.finish_evaluate()
				reset()
		else:
			reset() 

class ScientificAdvancement(Card):
	def __init__(self):
		super().__init__('scientific advancement', {}, "choose a scientific advancement to discover!")
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if len(data['order']) == 1:
			temp = Hand(300)
			for i in player[data['player_index']].current_science_tech:
				temp.hand.append(current_player.tech[i]['tech'])
			visible_screen['discover'] = temp
			shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['board']['tile_shadow'] = shadow
		else:
			if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'discover card':
				current_player.tech[current_player.current_science_tech[data['order'][1][2]]]['tech'].evaluate(board)
			else:
				reset()

class MilitaryAdvancement(Card):
	def __init__(self):
		super().__init__('military advancement', {}, "choose a military advancement to discover!")
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if len(data['order']) == 1:
			temp = Hand(300)
			for i in player[data['player_index']].current_military_tech:
				temp.hand.append(current_player.tech[i]['tech'])
			visible_screen['discover'] = temp
			shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['board']['tile_shadow'] = shadow
		else:
			if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'discover card':
				current_player.tech[current_player.current_military_tech[data['order'][1][2]]]['tech'].evaluate(board)
			else:
				reset()

class Village(Card):
	def __init__(self):
		super().__init__('scientific advancement', {}, "choose a scientific advancement to discover!")
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)): 
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].housing == 'none':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if current_player.add_housing(board[data['order'][1][2][0]][data['order'][1][2][1]], 'village'):
						self.finish_evaluate()
				reset()
		reset()

class Cavalry(Card):
	def  __init__(self):
		super().__init__('cavalry', {'food' : 10 ,'hammer' : 2, 'gold' : 5, 'horse' : 5}, 'deploy a cavalry on a friendly tile')
	def evaluate(self, board):
		current_player = player[data['player_index']]
		if greater(current_player.material, self.cost):
			if len(data['order']) == 1:
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index'] and board[i][j].population != 0 and board[i][j].name != 'ocean' and board[i][j] != 'coast':
							shadow[i][j] = -1
				visible_screen['board']['tile_shadow'] = shadow
				visible_screen['board']['tile_extra'] = 'population'
			else:
				if data['order'][1][0] == 'leftclick' and data['order'][1][1] == 'tile':
					if board[data['order'][1][2][0]][data['order'][1][2][1]].name != 'ocean' and board[data['order'][1][2][0]][data['order'][1][2][1]].name != 'coast':
						if current_player.remove_population(board[data['order'][1][2][0]][data['order'][1][2][1]]):
							current_player.add_unit(board[data['order'][1][2][0]][data['order'][1][2][1]],  unitCavalry(data['player_index']))
							self.finish_evaluate()
				reset()
		else:
			reset()

# technology
"""
military
	1. units are 10% cheaper
	2. every 5 tile added to your country increase research point by one
	3. killing unit reward 2 research point
"""
"""
Science	
	1.whenever population grows draw one card
	2.gain one research point every 5/3/1 turn
	3.
"""