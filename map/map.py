import map.hexArray
import pygame
import template
class Board(map.hexArray.HexArray):
	def  __init__(self, array):
		super().__init__(array)
	def draw_map(self, screen, screen_pos): #pos is the top right pos of the screen
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_tile(screen, temp_pos)
	def highlight_tile(self, screen, screen_pos, index):#highlight a tile
		temp_pos = (index[1] * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (index[0] % 2), index[0] * template.CELL_SIZE * 12 + screen_pos[1])
		self.map[index[0]][index[1]].draw_highlight(screen, temp_pos)
	def draw_population(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_pop(screen, temp_pos)
	def draw_resource(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_pop(screen, temp_pos)
	def draw_unit(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_pop(screen, temp_pos)
	def draw_biulding(self, screen, screen_pos):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
				if temp_pos[0] > - template.CELL_SIZE * 5 and temp_pos[0] < int(pygame.Surface.get_width(screen)) + template.CELL_SIZE * 5 and temp_pos[1] > - template.CELL_SIZE * 5 and temp_pos[1] < int(pygame.Surface.get_height(screen)) + template.CELL_SIZE * 5:
					self.map[i][j].draw_pop(screen, temp_pos)
	def get_tile_index(self, mouse_pos, screen_pos):
		return super().get_tile_index((mouse_pos[0] - screen_pos[0], mouse_pos[1] - screen_pos[1]), template.CELL_SIZE)