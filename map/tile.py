# a tile in the map
#mainly about draw the tile in differnt times
import pygame
import template
import map.tileExtra
import material
#the tile edge is the distance of the x,y pos from the edge to the center divided by the cell size
class Tile:
	def  __init__(self):
		self.pop = map.tileExtra.Population(2,0)
		self.unit = None
		self.player_index = -1
		self.resource = material.Material(2)
	def draw_tile(self, screen, pos):	
		pygame.draw.polygon(screen, (152,251,152), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE])
		pygame.draw.polygon(screen, (255,255,255), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_highlight(self, screen, pos):
		pygame.draw.polygon(screen, (255,255,0), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_tile_edge(self, screen, pos, color):
		pygame.draw.polygon(screen, color, [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_pop(self, screen, pos):	
		self.pop.draw_pop(screen, pos)
	def draw_resource(self, screen, pos):# still need to update
		self.pop.draw_resource(screen, pos)
	def draw_unit(self, screen, pos):	
		if self.unit == None:
			pass
		else:
			self.unit.draw_unit(screen, pos)