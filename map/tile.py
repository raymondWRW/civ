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
		self.tile_type = 'plain'
		self.biulding_type = 'none'
		self.bonus = []
	def draw_tile(self, screen, pos):
		pygame.draw.polygon(screen, (152,251,152), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE])
		pygame.draw.polygon(screen, (255,255,255), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_highlight(self, screen, pos):
		pygame.draw.polygon(screen, (255,255,0), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_tile_edge(self, screen, pos, color):
		pygame.draw.polygon(screen, color, [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_pop(self, screen, pos):	
		self.pop.draw_pop(screen, pos)
	def total_resource(self, tile_resource, biudling_resource):
		temp = material.Material()
		temp.add_material(tile_resource[self.tile_type])
		temp.add_material(biudling_resource[self.biulding_type])
		temp.add_material(self.bonus)
		return temp.to_array()
	def draw_resource(self, pos, tile_resource, biulding_resource):
		map.tileExtra.draw_resource(pos, self.total_resource(tile_resource, biulding_resource))
	def draw_unit(self, screen, pos):	
		if self.unit == None:
			pass
		else:
			self.unit.draw_unit(screen, pos)