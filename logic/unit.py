from coreFunction.surfaceExtended import *
from coreFunction.hexArray import *
from data.dataGame import *
class Unit():
	def __init__(self, name, player_index):
		self.name = name
		self.player_index = player_index
		self.health = player[self.player_index].unit[self.name]['max health']
		self.movement = player[self.player_index].unit[self.name]['max movement']
	def attack(self):
		return player[self.player_index].unit[self.name]['damage'] * self.health // player[self.player_index].unit[self.name]['max health']

	def damage_taken(self, damage, pos):
		self.health -= damage * player[self.player_index].tile[board[pos[0]][pos[1]].name]['defensivness']
		if self.health <= 0:
			board[pos[0]][pos[1]].unit = None
		pass

	def attack_of_opportunity(self):
		return player[self.player_index].unit[self.name]['damage'] // 2

	def zone_of_control(self, pos):
		edge = get_border_index((pos[0],pos[1]))
		for i in edge:
			if board[i[0]][i[1]].unit != None and board[i[0]][i[1]].unit.player_index != self.player_index:
				self.damage_taken(board[i[0]][i[1]].unit.attack_of_opportunity(), pos)
		
	def move(self):
		distance = get_distance(order[0][2], order[1][2])
		start_tile = board[order[0][2][0]][order[0][2][1]]
		target_tile = board[order[1][2][0]][order[1][2][1]]
		if target_tile.name != 'ocean':
			if target_tile.unit == None:
				if distance <= self.movement: # move
					self.zone_of_control(order[0][2])
					self.movement -= distance
					target_tile.unit = start_tile.unit
					start_tile.unit = None
			elif target_tile.unit.player_index != self.player_index and distance <= player[self.player_index].unit[self.name]['attack range'] and self.movement != 0:
				target_tile.unit.damage_taken(self.attack(), order[1][2])
				self.movement = 0

	def next_turn(self, pos):
		if board[pos[0]][pos[1]].player_index == self.player_index:
			if self.movement > 0 :
				self.health = min(current_player().unit[self.name]['max health'], self.health + current_player().unit[self.name]['max health']//10)
		else:
			player[player_index.value].add_tile(board[pos[0]][pos[1]])
		self.movement = current_player().unit[self.name]['max movement']

class unitInfantry(Unit):
	def __init__(self, player_index):
		super().__init__('infantry', player_index)

class unitCavalry(Unit):
	def __init__(self, player_index):
		super().__init__('cavalry', player_index)

class unitShip(Unit):
	def __init__(self, player_index):
		super().__init__('boat', player_index)
  