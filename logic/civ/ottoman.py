from logic.civ.civ import Civ
from logic.card import Card
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from data.dataGame import player, order, board, visible_screen, reset
class SapTrap(Card):
	def  __init__(self):
		super().__init__('sap trap', {}, "add a bordering tile to your country")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				return False
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_tile(board[order[1][2][0]][order[1][2][1]])
						self.finish_evaluate()
						return True
		reset()
		return False
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index != self.index:
			border_index = get_border_index(pos)
			for k in border_index:
				if board[k[0]][k[1]].player_index == self.index:
					return True
		return False
class Ottoman(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (255,32, 65))
		self.name = 'Ottoman'
	def start_game(self):
		super().start_game()
		self.hand.append(SapTrap())
		self.hand.append(SapTrap())
		self.hand.append(SapTrap())
