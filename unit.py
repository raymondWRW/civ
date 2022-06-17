import pygame, template, map.hexArray
from math import sin,cos,radians
def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr,color,center, 
        (center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))),2)
        theta+=0.01
unit_stat = {
	'warrior' : {
		'maxhealth' : 100,
		'damage' : 200,
		'attackrange' : 1,
		'movement' : 1
	},
	'cavalary' : {
		'maxhealth' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	},
	'seigemachine' : {
		'maxhealth' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	},
	'pikeandshot' : {
		'maxhealth' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	},
	'artillery' : {
		'maxhealth' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	},
	'tank' : {
		'maxhealth' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	}
}

class Unit():
	def __init__(self, image, name, player_index, stat, color):
		self.image = image
		self.name = name
		self.color = color
		self.player_index = player_index
		self.maxhealth = stat['maxhealth']
		self.health = stat['maxhealth']
		self.maxmovement = stat['movement']
		self.movement = self.maxmovement
		self.damage = stat['damage']
		self.attackrange = stat['attackrange']
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
	def draw_unit(self, screen, pos):
		pygame.draw.circle(screen, self.color, pos, template.CELL_SIZE * 4)
		screen.blit(self.image, (pos[0] - template.CELL_SIZE * 4, pos[1] - template.CELL_SIZE * 4))
