import map.hexArray
import pygame
import template
class Board(map.hexArray.HexArray):
	def  __init__(self, array):
		super().__init__(array)
	def withinscreen(self, temp_pos):
		return temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(template.screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(template.screen)) + template.CELL_SIZE * 5
	def highlight_tile(self, screen, screen_pos, index):#highlight a tile
		temp_pos = (index[1] * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (index[0] % 2), index[0] * template.CELL_SIZE * 12 + screen_pos[1])
		if index[0] < 15 and index[1] < 30:
			self.map[index[0]][index[1]].draw_tile_edge(screen, temp_pos, (255, 255, 0))
	def draw_edge_tile(self, screen, screen_pos, index, color):
		temp_pos = (index[1] * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (index[0] % 2), index[0] * template.CELL_SIZE * 12 + screen_pos[1])
		if self.withinscreen(temp_pos):
			self.map[index[0]][index[1]].draw_tile_edge(screen, temp_pos, color)
	def draw_map(self, screen, screen_pos): #pos is the top right pos of the screen
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if self.withinscreen(temp_pos):
					self.map[i][j].draw_tile(screen, temp_pos)				
	def draw_player_tile(self, screen, screen_pos, players):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if self.map[i][j].player_index == -1:
					continue
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if not(self.withinscreen(temp_pos)):
					continue	
				border_index = []
				if i % 2 == 1:
					border_index = template.BORDER_INDEX_ODD
				else:
					border_index = template.BORDER_INDEX_EVEN
				for k in range(len(border_index)):
					if not(i + border_index[k][0] >= 0 and j + border_index[k][1] >= 0 and i + border_index[k][0] < len(self.map) and j + border_index[k][1] < len(self.map[i])):
						pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)
					elif not(self.map[i + border_index[k][0]][j + border_index[k][1]].player_index == self.map[i][j].player_index):
						pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)   
	def draw_population(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_pop(screen, temp_pos)
	def draw_resource(self, screen, screen_pos, player):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_resource(temp_pos, player.tile_resource, player.biulding_resource)
	def draw_unit(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_unit(screen, temp_pos)
	def draw_biulding(self, screen, screen_pos):#work in progress
		pass
	def get_tile_index(self, mouse_pos, screen_pos):
		return super().get_tile_index((mouse_pos[0] - screen_pos[0], mouse_pos[1] - screen_pos[1]), template.CELL_SIZE)