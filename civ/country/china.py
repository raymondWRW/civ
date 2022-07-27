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
				tile_to_add = []
				shadow = [[0 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
				#add neighbor tile
				for i in range(len(shadow)):
					for j in range(len(shadow[i])):
						if board[i][j].player_index == data['player_index']:
							border_index = get_border_index((i,j))
							for k in range(len(border_index)):
								border_tile = (border_index[k][0] + i, border_index[k][1] + j)
								if 0 <= border_tile[0] <= len(board) and 0 <= border_tile[1] <= len(board[i]):
									if board[border_tile[0]][border_tile[1]].player_index == 0:
										tile_to_add.append(border_tile)
				for i in tile_to_add:
					board[i[0]][i[1]].player_index = data['player_index']
				#extra income
				for i in range (len(board)):
					for j in range (len(board[i])):
						if board[i][j].player_index == self.player_index:
							add_value(current_player.material, board[i][j].tile_resource(), board[i][j].population)
			reset()

class China(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (255,178, 0))
		self.building_resource['farm']['resource']['food'] += 1
		self.tech['classical science']['tech'] = ChinaClassicalScience()

		