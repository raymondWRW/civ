from logic.tech.tech import Tech
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from data.dataGame import *
from logic.civ.civ import Civ
from logic.discover import Administration, Exploration, Insight
class ChinaClassicalScience(Tech):
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
			visible_screen['shadow'] = [[True for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
			visible_screen['discover'] = self.discover	
		if len(order) == 3:
			if order[2][0] == 'leftclick' and order[2][1] == 'discover card':
				self.discover[order[2][2]].evaluate()
				array_valid_index = []
				#add neighbor tile
				for i in range(len(board)):
					for j in range(len(board[i])):
						if board[i][j].player_index == self.index:
							border_index = get_border_index((i,j))
							for k in border_index:
								if 0 <= k[0] <= len(board) and 0 <= k[1] <= len(board[k[0]]):
									if board[k[0]][k[1]].player_index == 0:
										array_valid_index.append(k)
				for i in array_valid_index:
					player[self.index].add_tile(board[i[0]][i[1]])
				#extra income
				for i in range (len(board)):
					for j in range (len(board[i])):
						if board[i][j].player_index == player[self.index].player_index:
							add_value(player[self.index].material, board[i][j].tile_resource(), board[i][j].population)
				self.finish_evaluate()
			reset()
class China(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (255,178, 0))
		self.name = 'China'
	def start_game(self):
		super().start_game()
		self.building['workshop']['resource']['gold'] += 1
		self.tech['classical civic'] = ChinaClassicalScience()