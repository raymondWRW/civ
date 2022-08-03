from cmath import pi
import pygame
from board.settingTile import *
from game.variable import *
from coreFunction.dictionaryExtended import *
from coreFunction.surfaceExtended import *
from unit.settingUnit import *
# visible_screen = {
# 	'board' : {
# 		'tile' : True,
# 		'player_shadow' : True,
# 		'tile_shadow' : [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
# 		'tile_extra' : 'unit',
# 		'tile_edge' : True,
# 		'tile_highlight' : True
# 	},
# 	'resource' : True,
# 	'button' : True,
# 	'hand' : True,
# 	'discover' : None
# }
# data = {
# 	'screen_pos' : (0,0),
# 	'player_index' : 1,
# 	'order' : [],
# }
# last_mouse_info = {
# 	'type' : 'none',
# 	'pos' : (0,0),
# 	'dragging' : False
# }
# screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
# player = [None,(),()]
class Tile:
	def  __init__(self, name, color):
		self.name = name
		self.color = color
		self.building = 'none'
		self.housing = 'none'
		self.player_index = 0
		self.population = 0
		self.unit = None
		self.display = pygame.Surface((CELL_SIZE * 16, CELL_SIZE * 16)).convert_alpha()
	#draw
	def update(self):
		pass

	def draw_tile(self):
		self.display.blit(tile_image[self.name], (0, 0))
		# pygame.draw.polygon(self.display, self.color, [(x * CELL_SIZE + CELL_SIZE * 8, y * CELL_SIZE + CELL_SIZE * 8) for x, y in TILE_EDGE])
		# pygame.draw.polygon(self.display, (255,255,255), [(x * CELL_SIZE + CELL_SIZE * 8, y * CELL_SIZE + CELL_SIZE * 8) for x, y in TILE_EDGE],2)

	def draw_shadow(self, color):
		temp = pygame.Surface((CELL_SIZE * 16, CELL_SIZE * 16)).convert_alpha()
		pygame.draw.polygon(temp, color, [(x * CELL_SIZE + CELL_SIZE * 8, y * CELL_SIZE + CELL_SIZE * 8) for x, y in TILE_EDGE])
		self.display.blit(temp,(0,0))
		# pygame.draw.polygon(self.display, (color), [((x+8) * CELL_SIZE, (y + 8) * CELL_SIZE) for x, y in TILE_EDGE])
	# def draw_highlight(self, screen, pos):
	# 	pygame.draw.polygon(screen, (255,255,0), [(x * CELL_SIZE + pos[0], y * CELL_SIZE + pos[1]) for x, y in TILE_EDGE],2)
	# def draw_tile_edge(self, screen, pos, color):
	# 	pygame.draw.polygon(screen, color, [(x * CELL_SIZE + pos[0], y * CELL_SIZE + pos[1]) for x, y in TILE_EDGE],2)
	def draw_unit(self):
		if self.unit != None:
			# self.display.blit(UnitUI(self.unit), (0,0))
			# self.unit.update()
			# self.display.blit(self.unit.display, (0,0))
			current_player = player[self.unit.player_index]
			# pie(self.display, (255,255,255), (CELL_SIZE * 8 , CELL_SIZE * 8), CELL_SIZE * 5, -90, (360 * self.unit.health)//current_player.unit_stat[self.unit.name]['max health'] - 90)
			health_percentage = self.unit.health/current_player.unit_stat[self.unit.name]['max health']
			# print(health_percentage)
			pygame.draw.arc(self.display, (255,255,255), Rect(CELL_SIZE * 4 - 5, CELL_SIZE * 4 - 5, CELL_SIZE * 9, CELL_SIZE * 9), pi/2, pi * 2 * health_percentage + pi/2, 5)
			pygame.draw.circle(self.display, current_player.color, (CELL_SIZE * 8, CELL_SIZE * 8), CELL_SIZE * 4)
			self.display.blit(unit_image[self.unit.name], (CELL_SIZE * 4 , CELL_SIZE * 4))
			
                #    (360 * self.unit.health)//current_player.unit_stat[self.unit.name]['max health'] - 90, 5)
	def draw_pop(self):
		for i in range(self.max_population()):
			pos = (RESOURCE_POS[self.max_population()][i][0] * CELL_SIZE + CELL_SIZE * 6.5, RESOURCE_POS[self.max_population()][i][1] * CELL_SIZE + CELL_SIZE * 6.5)
			if i < self.population:
				self.display.blit(RESOURCE_FULLPOPULATION_TILE, pos)
			else:
				self.display.blit(RESOURCE_EMPTYPOPULATION_TILE, pos)

	def draw_resource(self):
		total = total_count(self.tile_resource())
		index = 0
		for i,j in self.tile_resource().items():
			for k in range(j):
				pos = (RESOURCE_POS[total][index][0] * CELL_SIZE + CELL_SIZE * 7, RESOURCE_POS[total][index][1] * CELL_SIZE + CELL_SIZE * 7)
				self.display.blit(resource_image[i], pos)
				index += 1
	# for i in resource:
	# 	total += i[1]
	# if total == 0:
	# 	return
	# index = 0
	# for i in resource:
	# 	res = template.resource_image[i[0]]	
	# 	for j in range(i[1]):
	# 		template.screen.blit(res,(pos[0] + (template.RESOURCE_POS[total][index][0] - 1) * template.CELL_SIZE, pos[1] + (template.RESOURCE_POS[total][index][1] - 1) * template.CELL_SIZE))
	# 		index += 1
	# def draw_pop(self, screen, pos):	
	# 	self.pop.draw_pop(screen, pos)
	# def draw_resource(self, pos, tile_resource, building_resource):
	# 	map.tileExtra.draw_resource(pos, self.total_resource(tile_resource, building_resource))
	# def draw_unit(self, screen, pos):	
	# 	if self.unit == None:
	# 		pass
	# 	else:
	# 		self.unit.draw_unit(screen, pos)
	# resource
	def tile_resource(self):
		current_player = player[self.player_index]
		temp = {}
		add_value(temp, current_player.tile_resource[self.name]['resource'])
		add_value(temp, current_player.building_resource[self.building]['resource'])
		return temp

	# populaation
	def max_population(self):
		current_player = player[self.player_index]
		pop = 0
		pop += current_player.tile_resource[self.name]['housing']
		pop += current_player.building_resource[self.building]['housing']
		return pop