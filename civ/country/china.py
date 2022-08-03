import pygame
from card.settingCard import *
from card.hand import Hand
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from game.variable import *
from card.scienceTech import *
from civ.civ import Civ
class ChinaClassicalScience(ScienceTech):
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
			shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['board']['tile_shadow'] = shadow
			visible_screen['discover'] = self.discover	
		if len(data['order']) == 3:
			if data['order'][2][0] == 'leftclick' and data['order'][2][1] == 'discover card':
				self.discover.hand[data['order'][2][2]].evaluate()
				tile_to_add = []
				#add neighbor tile
				for i in range(len(board)):
					for j in range(len(board[i])):
						if board[i][j].player_index == data['player_index']:
							border_index = get_border_index((i,j))
							for k in border_index:
								if 0 <= k[0] <= len(board) and 0 <= k[1] <= len(board[k[0]]):
									if board[k[0]][k[1]].player_index == 0:
										tile_to_add.append(k)
				for i in tile_to_add:
					current_player.add_tile(board[i[0]][i[1]])
					# board[i[0]][i[1]].player_index = data['player_index']
				#extra income
				for i in range (len(board)):
					for j in range (len(board[i])):
						if board[i][j].player_index == current_player.player_index:
							add_value(current_player.material, board[i][j].tile_resource(), board[i][j].population)
				
				self.finish_evaluate()		
			reset()

class China(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (255,178, 0))
		self.building_resource['farm']['resource']['food'] += 1
		self.tech['classical science']['tech'] = ChinaClassicalScience()

		