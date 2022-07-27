import pygame
from board.settingTile import CELL_SIZE
from coreFunction.surfaceExtended import *
from unit.settingUnit import *
from game.variable import *
class Unit():
	def __init__(self, image, name, player_index):
		self.image = image
		self.name = name
		self.player_index = player_index
		self.health = player[self.player_index].unit_stat[self.name]['max health']
		self.movement = player[self.player_index].unit_stat[self.name]['max movement']
	def attack(self, board, start_pos, target_pos):
		bonus = 0
		# board[target_pos[0]][target_pos[1]].unit.health -= (self.damage + bonus) * self.health // self.maxhealth
		self.movement = 0
		return (self.damage + bonus) * self.health // self.maxhealth
		# if board[target_pos[0]][target_pos[1]].unit.health <= 0:
		# 	board[target_pos[0]][target_pos[1]].unit = None
		# else:
		# 	board[target_pos[0]][target_pos[1]].unit.counterattack(board, target_pos, start_pos)
		# return
	def counterattack(self, board, start_pos, target_pos):
		bonus = 0
		return (self.damage + bonus) * self.health // self.maxhealth
		# bonus = 0
		# board[target_pos[0]][target_pos[1]].unit.health -= (self.damage + bonus)* self.health // self.maxhealth
		# if board[target_pos[0]][target_pos[1]].unit.health <= 0:
		# 	board[target_pos[0]][target_pos[1]].unit = None
	def nextturn(self, board, pos, players):
		if self.movement != 0:
			if board[pos[0]][pos[1]].player_index == self.player_index:#it is in it own tile
				self.health = max(self.maxhealth, self.health + self.maxhealth//10)	
			else:
				if board[pos[0]][pos[1]].player_index != -1:
					players[board[pos[0]][pos[1]].player_index].remove_tile(pos, board)
				board[pos[0]][pos[1]].player_index = self.player_index
				players[self.player_index].add_tile(pos, board)
		self.movement = self.maxmovement
  
class unitWarrior(Unit):
	def __init__(self, player_index):
		super().__init__(UNIT_WARRIOR, 'warrior', player_index)