#what a player is in this game
# a player needs recources
#tile
#color 
import material, card.card, card.deck, card.hand, unit, map.hexArray
class Player:
	def  __init__(self, color, player_index):
		#for identification
		self.color = color
		self.player_index = player_index
		#resources & income
		self.material = material.Material()
		self.income = material.Material()
		#territory and borders
		self.tile = set()
		self.unit_pos = set()
		#cards
		self.hand = card.hand.Hand((50, 600), 120,(100, 280))
		self.deck = []
		#army
		self.unit = []
		self.unit_stat = unit.unit_stat
		#initialize	
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.Warrior())
	def evaluate_hand(self, board, players, visible_screen, order):
		self.hand.hand[order[0][2]].evaluate(board, players, visible_screen, order, self.player_index)
	def evaluate_tile(self, board, players, visible_screen, order):
		if board[order[0][2][0]][order[0][2][1]].unit == None:
			visible_screen['tile_extra'] = 'unit'
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'unit'
			return
		else:
			start_pos = order[0][2]
			target_pos = order[1][2]
			if order[1][0] == 'leftclick' and order[1][1] == 'tile':
				dis = map.hexArray.HexArray.get_distance(start_pos, target_pos)
				if board[target_pos[0]][target_pos[1]].unit == None:#moving unit to the tile
					if dis <= board[start_pos[0]][start_pos[1]].unit.movement:
						board[target_pos[0]][target_pos[1]].unit = board[start_pos[0]][start_pos[1]].unit
						board[start_pos[0]][start_pos[1]].unit = None
						board[target_pos[0]][target_pos[1]].unit.movement -= 1
						self.unit.remove(start_pos)
						self.unit.append(target_pos)
				elif target_pos != start_pos: # unit attacking another unit
					board[start_pos[0]][start_pos[1]].unit.attack(board, start_pos, target_pos)
			visible_screen['tile_extra'] = 'unit'
			order.clear()
	def add_tile(self, pos, board):
		self.tile.add(pos)
		board[pos[0]][pos[1]].player_index = self.player_index
		self.income.add_material(board[pos[0]][pos[1]].resource)
	def remove_tile(self, pos, board):
		self.tile.remove(pos)
		board[pos[0]][pos[1]].player_index = None
		self.income.remove_material(board[pos[0][pos[1]].resource])
	def add_income(self):
		self.material.add_material(self.income)
	def end_turn(self, board, players):
		for i in self.unit:
			board[i[0]][i[1]].unit.nextturn(board, i, players)
			print(i)
	def start_turn(self):
		self.add_income()