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
		self.screen_pos = (0,0)
		#resources & income
		self.material = material.Material([('food', 10),('science', 10),('hammer', 10),('gold', 10)])
		self.income = material.Material([('food', 1),('science', 1),('hammer', 1),('gold', 1)])
		self.tile_resource = {
			'none'  : [],
			'plain' : [('food', 2)]
		}
		self.biulding_resource = {
			'none'  : [],
			'farm' : [('food', 1)]
		}
		#territory and borders
		self.tile = set()
		self.unit_pos = set()
		#cards
		self.hand = card.hand.Hand((50, 600), 120,(100, 280))
		self.deck = card.deck.Deck()
		#army
		self.unit = []
		self.unit_stat = unit.unit_stat
		#initialize	
		self.start_game()
	def start_game(self):
		for i in range(20):
			self.deck.add_card(card.card.PopulationGrowth())
		for i in range(5):
			self.deck.add_card(card.card.Warrior())
		for i in range(5):
			self.deck.add_card(card.card.Farm())
		self.deck.shuffle()
		for i in range(7):
			self.hand.add_card(self.deck.draw())
	def evaluate_hand(self, board, players, visible_screen, order):
		self.hand.hand[order[0][2]].evaluate(board, players, visible_screen, order, self.player_index)
	def evaluate_tile(self, board, players, visible_screen, order):
		if board[order[0][2][0]][order[0][2][1]].unit == None or board[order[0][2][0]][order[0][2][1]].unit.player_index != self.player_index:
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
						board[target_pos[0]][target_pos[1]].unit.movement -= dis
						self.unit.remove(start_pos)
						self.unit.append(target_pos)
				elif target_pos != start_pos: # unit attacking another unit
					if dis <= board[start_pos[0]][start_pos[1]].unit.attackrange:
						board[target_pos[0]][target_pos[1]].unit.health -= board[start_pos[0]][start_pos[1]].unit.attack(board, start_pos, target_pos)
						if board[target_pos[0]][target_pos[1]].unit.health <= 0:#killed unit
							players[board[target_pos[0]][target_pos[1]].unit.player_index].unit.remove(target_pos)
							board[target_pos[0]][target_pos[1]].unit = None
						else:	
							board[start_pos[0]][start_pos[1]].unit.health -= board[target_pos[0]][target_pos[1]].unit.counterattack(board, start_pos, target_pos)
							if board[start_pos[0]][start_pos[1]].unit.health <= 0:#died on the back swing
								players[board[start_pos[0]][start_pos[1]].unit.player_index].unit.remove(target_pos)
								board[start_pos[0]][start_pos[1]].unit = None
					board[start_pos[0]][start_pos[1]].unit.attack(board, start_pos, target_pos)
			visible_screen['tile_extra'] = 'unit'
			order.clear()
   
	#turn
	def end_turn(self, board, players):
		for i in self.unit:
			board[i[0]][i[1]].unit.nextturn(board, i, players)
	def start_turn(self):
		self.material.add_material(self.income.to_array())

	#change in tile and income
	def add_tile(self, pos, board):
		if board[pos[0]][pos[1]].player_index != self.player_index:
			self.tile.add(pos)
			board[pos[0]][pos[1]].player_index = self.player_index	
			self.income.multiple_add_material(board[pos[0]][pos[1]].total_resource(self.tile_resource, self.biulding_resource), board[pos[0]][pos[1]].pop.cur_pop)
			return True		
		return False
	def remove_tile(self, pos, board):
		if board[pos[0]][pos[1]].player_index == self.player_index:
			self.tile.remove(pos)
			board[pos[0]][pos[1]].player_index = None
			self.income.multiple_remove_material(board[pos[0]][pos[1]].total_resource(self.tile_resource, self.biulding_resource), board[pos[0]][pos[1]].pop.cur_pop)
			return True		
		return False
	def add_population(self, board, pos):
		if board[pos[0]][pos[1]].pop.max_pop > board[pos[0]][pos[1]].pop.cur_pop and board[pos[0]][pos[1]].player_index == self.player_index:
			board[pos[0]][pos[1]].pop.cur_pop += 1
			self.income.add_material(board[pos[0]][pos[1]].total_resource(self.tile_resource, self.biulding_resource))
			return True
		return False
	def remove_population(self, board, pos):
		if board[pos[0]][pos[1]].pop.cur_pop > 0 and board[pos[0]][pos[1]].player_index == self.player_index:
			board[pos[0]][pos[1]].pop.cur_pop -= 1
			self.income.remove_material(board[pos[0]][pos[1]].total_resource(self.tile_resource, self.biulding_resource))
			return True
		return False 
	def add_biulding(self, board, pos, biulding_type):
		if board[pos[0]][pos[1]].player_index == self.player_index and board[pos[0]][pos[1]].biulding_type == 'none':
			board[pos[0]][pos[1]].biulding_type = biulding_type
			self.income.multiple_add_material(self.biulding_resource[biulding_type], board[pos[0]][pos[1]].pop.cur_pop)
			return True
		return False
	# def remove_biudling(self, board, pos, biulding_type):	
	# 	board[pos[0]][pos[1]].pop.cur_pop += 1
	# 	self.income.add_material(board[pos[0]][pos[1]])
	# def recaculate_tile(self, board, pos):
	# 	pass
