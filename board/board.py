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
				if within_surface(tile_center_pos, self.display, (0,0), CELL_SIZE * 5):
					self.board[i][j].display.fill((0,0,0,0))
					self.board[i][j].draw_tile()
					#draw shadow
					# -1 = no shadow
					# 0 = shadow
					if visible_screen['board']['tile_shadow'][i][j] == 0:
						self.board[i][j].draw_shadow((50, 50, 50, 200))
					elif visible_screen['board']['player_shadow'] == True and self.board[i][j].player_index != 0:
						pc = player[self.board[i][j].player_index].color # player color
						self.board[i][j].draw_shadow((pc[0],pc[1],pc[2], 100))
					# tile extra
					if pygame.key.get_pressed()[pygame.K_1] == True:
						self.board[i][j].draw_pop()
					elif pygame.key.get_pressed()[pygame.K_2] == True:
						self.board[i][j].draw_resource()
					elif pygame.key.get_pressed()[pygame.K_3] == True:
						self.board[i][j].draw_unit()	
					elif visible_screen['board']['tile_extra'] == 'unit':
						self.board[i][j].draw_unit()
					elif visible_screen['board']['tile_extra'] == 'population':
						self.board[i][j].draw_pop()
					elif visible_screen['board']['tile_extra'] == 'resource':
						self.board[i][j].draw_resource()
					self.display.blit(self.board[i][j].display, (tile_center_pos[0] - CELL_SIZE * 8, tile_center_pos[1] - CELL_SIZE * 8))
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				tile_center_pos = (j * CELL_SIZE * 12 + data['screen_pos'][0] - CELL_SIZE * 6 * (i % 2), i * CELL_SIZE * 12 + data['screen_pos'][1])
				if within_surface(tile_center_pos, self.display, (0,0), CELL_SIZE * 5):
					edge = get_border_index((i,j))	
					if visible_screen['board']['tile_edge'] and self.board[i][j].player_index != 0:
						pc = player[self.board[i][j].player_index].color # player color
						for k in range (len(edge)):
							border_tile = (edge[k][0] + i, edge[k][1] + j)
							s_pos = (TILE_EDGE[k][0] * CELL_SIZE + tile_center_pos[0], TILE_EDGE[k][1] * CELL_SIZE + tile_center_pos[1])
							t_pos = (TILE_EDGE[(k + 1) % 6][0]) * CELL_SIZE + tile_center_pos[0], (TILE_EDGE[(k + 1) % 6][1] * CELL_SIZE + tile_center_pos[1])
							if 0 <= border_tile[0] <= len(self.board) and 0 <= border_tile[1] <= len(self.board[i]):
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
		center = (BOARD_ROW // 2, BOARD_COL // 2)
		set_index = [center]
		for i in range(225):
			temp_pos = random.choice(set_index)
			edge = get_border_index(temp_pos)
			for j in range (len(edge)):
				border_tile = (edge[j][0] + temp_pos[0], edge[j][1] + temp_pos[1])
				if 0 <= border_tile[0] < len(self.board) and 0 <= border_tile[1] < len(self.board[border_tile[0]]):
					if landnocean[border_tile[0]][border_tile[1]] == -1:
						landnocean[border_tile[0]][border_tile[1]] = 0
						set_index.append(border_tile)
		self.board = [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		#convet to tiles
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				self.board[i][j] = Tile('plain', tile_color['plain'])