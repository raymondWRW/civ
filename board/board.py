import pygame, sys, queue, random
from board.tile import Tile
from pygame.locals import *
from board.settingTile import CELL_SIZE, tile_color, TILE_EDGE
from coreFunction.surfaceExtended import within_surface
from game.settingGame import *
from coreFunction.hexArray import *
from game.variable import *

pygame.init()
class Board():
	def __init__(self):
		self.board = [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha()
	def update(self):
		self.display.fill((255,255,255,0))
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				tile_center_pos = (j * CELL_SIZE * 12 + data['screen_pos'][0] - CELL_SIZE * 6 * (i % 2), i * CELL_SIZE * 12 + data['screen_pos'][1])
				if within_surface(tile_center_pos, self.display, (0,0), CELL_SIZE * 8):
					tile = self.board[i][j]
					tile.display.fill((0,0,0,0))
					tile.draw_tile()
					#draw shadow
					# -1 = no shadow
					# 0 = shadow
					if visible_screen['board']['tile_shadow'][i][j] == 0:
						tile.draw_shadow((50, 50, 50, 200))
					elif visible_screen['board']['player_shadow'] == True and tile.player_index != 0:
						pc = player[tile.player_index].color # player color
						tile.draw_shadow((pc[0],pc[1],pc[2], 100))
					# tile extra
					if pygame.key.get_pressed()[pygame.K_1] == True:
						tile.draw_pop()
					elif pygame.key.get_pressed()[pygame.K_2] == True:
						tile.draw_resource()
					elif pygame.key.get_pressed()[pygame.K_3] == True:
						tile.draw_unit()	
					elif visible_screen['board']['tile_extra'] == 'unit':
						tile.draw_unit()
					elif visible_screen['board']['tile_extra'] == 'population':
						self.board[i][j].draw_pop()
					elif visible_screen['board']['tile_extra'] == 'resource':
						self.board[i][j].draw_resource()
					self.display.blit(self.board[i][j].display, (tile_center_pos[0] - CELL_SIZE * 8, tile_center_pos[1] - CELL_SIZE * 8))
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				tile_center_pos = (j * CELL_SIZE * 12 + data['screen_pos'][0] - CELL_SIZE * 6 * (i % 2), i * CELL_SIZE * 12 + data['screen_pos'][1])
				if within_surface(tile_center_pos, self.display, (0,0), CELL_SIZE * 5):	
					if visible_screen['board']['tile_edge'] and self.board[i][j].player_index != 0:
						pc = player[self.board[i][j].player_index].color # player color
						edge = get_border_index((i,j))
						for k in range (len(edge)):
							border_tile = (edge[k][0], edge[k][1])
							s_pos = (TILE_EDGE[k][0] * CELL_SIZE + tile_center_pos[0], TILE_EDGE[k][1] * CELL_SIZE + tile_center_pos[1])
							t_pos = (TILE_EDGE[(k + 1) % 6][0]) * CELL_SIZE + tile_center_pos[0], (TILE_EDGE[(k + 1) % 6][1] * CELL_SIZE + tile_center_pos[1])
							if 0 <= border_tile[0] <= len(self.board) and 0 <= border_tile[1] <= len(self.board[border_tile[0]]):
								if self.board[border_tile[0]][border_tile[1]].player_index != self.board[i][j].player_index:
									pygame.draw.line(self.display, pc, s_pos, t_pos, 5)
							else:
								pygame.draw.line(self.display, pc, s_pos, t_pos, 5)
		#draw highlight
		index = get_tile_index((last_mouse_info['pos'][0] - data['screen_pos'][0], last_mouse_info['pos'][1] - data['screen_pos'][1]), CELL_SIZE)
		index_pos = (index[1] * CELL_SIZE * 12 + data['screen_pos'][0] - CELL_SIZE * 6 * (index[0] % 2), index[0] * CELL_SIZE * 12 + data['screen_pos'][1])
		pygame.draw.polygon(self.display, (255,255,0), [(x * CELL_SIZE + index_pos[0], y * CELL_SIZE + index_pos[1]) for x, y in TILE_EDGE],2)
					# if within_surface(last_mouse_info['pos'], self.board[i][j].display, (tile_center_pos[0] - CELL_SIZE * 8, tile_center_pos[1] - CELL_SIZE * 8), CELL_SIZE * 5):
					# 	pygame.draw.polygon(self.display, (255,255,0), [(x * CELL_SIZE + CELL_SIZE * 8 + tile_center_pos[0], y * CELL_SIZE + CELL_SIZE * 8 + tile_center_pos[1]) for x, y in TILE_EDGE],2)
				# 	shadow = 0
				# if  visible_screen['board']['tile_shadow'] != None:
				# 	shadow = visible_screen['board']['tile_shadow'][i][j]
				# self.board[i][j].update(visible_screen['board']['tile'], shadow, visible_screen['board']['tile_extra'], edge, visible_screen['board']['tile_highlight'], player[self.board[i][j].player_index])
				# self.display.blit(self.board[i][j].display, (tile_center_pos - CELL_SIZE * 8, tile_center_pos - CELL_SIZE * 8))	
	def tileGeneration(self):
		# choose the center of plates
		landnocean = [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		center_tile_player = []
		for i in range(2):
			center = (random.randint(BOARD_ROW//4, BOARD_ROW//4 * 3), random.randint(BOARD_COL//4, BOARD_COL//4 * 3))
			index = [center]
			center_tile_player.append(center)
			count = 0
			while count < 100:
				if len(index) == 0:
					break
				temp_pos = index.pop(random.randint(0, len(index) - 1))
				if 0 <= temp_pos[0] < len(landnocean) and 0 <= temp_pos[1] < len(landnocean[temp_pos[0]]):
					if landnocean[temp_pos[0]][temp_pos[1]] == -1:
						landnocean[temp_pos[0]][temp_pos[1]] = 0
						edge = get_border_index(temp_pos)
						for k in edge:
							index.append(k)
						count += 1
		self.board = [[Tile('ocean', tile_color['ocean']) for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		#convet to tiles
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if landnocean[i][j] == 0:
					rnd = random.randint(1, 10)
					if rnd < 2:
						self.board[i][j] = Tile('wood', tile_color['wood'])
					elif rnd > 9:
						self.board[i][j] = Tile('mountain', tile_color['mountain'])
					else:
						self.board[i][j] = Tile('plain', tile_color['plain'])
		#coast
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if landnocean[i][j] == -1:
					# if self.board[i][j].name ==
					# self.board[i][j] = Tile('plain', tile_color['plain'])
					edge = get_border_index((i,j))
					for k in edge:
						if 0 <= k[0] < len(landnocean) and 0 <= k[1] < len(landnocean[k[0]]):
							if landnocean[k[0]][k[1]] == 0:
								self.board[i][j] = Tile('coast', tile_color['coast'])
		self.board[center_tile_player[0][0]][center_tile_player[0][1]].player_index = 1
		player[1].screen_pos = (600 - center_tile_player[0][1] * CELL_SIZE * 12 - CELL_SIZE * 6 * (i % 2), 325 - center_tile_player[0][0] * CELL_SIZE * 12)
		data['screen_pos'] = player[1].screen_pos 
		self.board[center_tile_player[1][0]][center_tile_player[1][1]].player_index = 2
		player[2].screen_pos = (600 - center_tile_player[1][1] * CELL_SIZE * 12 - CELL_SIZE * 6 * (i % 2), 325 - center_tile_player[1][0] * CELL_SIZE * 12)
