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
		self.tile_color = (152,251,152)
	def draw_tile(self, screen, pos):
		pygame.draw.polygon(screen, self.tile_color, [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE])
		pygame.draw.polygon(screen, (255,255,255), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
	def draw_shadow(self, screen, pos):
		temp = pygame.Surface((template.CELL_SIZE * 16, template.CELL_SIZE * 16)).convert_alpha()
		pygame.draw.polygon(temp, (50,50,50, 100), [(x * template.CELL_SIZE + template.CELL_SIZE * 8, y * template.CELL_SIZE + template.CELL_SIZE * 8) for x, y in template.TILE_EDGE])
		screen.blit(temp,(pos[0] - template.CELL_SIZE * 8, pos[1] - template.CELL_SIZE * 8))
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









# # a tile in the map
# #mainly about draw the tile in differnt times
# import pygame
# import template
# import map.tileExtra
# import material
# import random
# #the tile edge is the distance of the x,y pos from the edge to the center divided by the cell size
# # tile_color = {
# # 	'plain' : (152,251,152)
# # }
# # def draw_polygon_alpha(surface, color, points):
# #     lx, ly = zip(*points)
# #     min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
# #     target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
# #     shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
# #     pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
# #     surface.blit(shape_surf, target_rect)
# # def draw_resource(pos, resource):
# # 	total = 0
# # 	for i in resource:
# # 		total += i[1]
# # 	if total == 0:
# # 		return
# # 	index = 0
# # 	for i in resource:
# # 		res = template.cost_image[i[0]]	
# # 		for j in range(i[1]):
# # 			template.screen.blit(res,(pos[0] + (template.RESOURCE_POS[total][index][0] - 1) * template.CELL_SIZE, pos[1] + (template.RESOURCE_POS[total][index][1] - 1) * template.CELL_SIZE))
# # 			index += 1
# # def draw_player_tile(self, screen, screen_pos, players):
# # 		for i in range(len(self.map)):
# # 			for j in range(len(self.map[i])):
# # 				if self.map[i][j].player_index == -1:
# # 					continue
# # 				temp_pos = (j * template.CELL_SIZE * 12 + screen_pos[0] - template.CELL_SIZE * 6 * (i % 2), i * template.CELL_SIZE * 12 + screen_pos[1])
# # 				if not(self.withinscreen(temp_pos)):
# # 					continue	
# # 				border_index = []
# # 				if i % 2 == 1:
# # 					border_index = template.BORDER_INDEX_ODD
# # 				else:
# # 					border_index = template.BORDER_INDEX_EVEN
# # 				for k in range(len(border_index)):
# # 					if not(i + border_index[k][0] >= 0 and j + border_index[k][1] >= 0 and i + border_index[k][0] < len(self.map) and j + border_index[k][1] < len(self.map[i])):
# # 						pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)
# # 					elif not(self.map[i + border_index[k][0]][j + border_index[k][1]].player_index == self.map[i][j].player_index):
# # 						pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)  

# class Tile:
# 	def  __init__(self):
# 		self.pop = map.tileExtra.Population(2,0)
# 		self.max_pop = 2
# 		self.cur_pop = 0
# 		self.unit = None
# 		self.player_index = -1	
# 		self.tile_type = 'plain'
# 		self.biulding_type = 'none'
# 		self.bonus = []
# 		self.tile_color = (152,251,152, 255)	
# 	#, player_color, overlay, tokens, border
# 	def draw_tile(self, screen, pos):
# 		#drawing the tiles
# 		temp = pygame.Surface((template.CELL_SIZE * 16, template.CELL_SIZE * 16)).convert_alpha()
# 		pygame.draw.polygon(screen, self.tile_color, [(x * template.CELL_SIZE + template.CELL_SIZE * 16, y * template.CELL_SIZE + template.CELL_SIZE * 16) for x, y in template.TILE_EDGE])
# 		screen.blit(temp, (pos[0] - template.CELL_SIZE, pos[1] - template.CELL_SIZE))
# 		# if overlay[0] == 'shadow':
			
# 		# 	color = (self.tile_color[0] + self.tile_color[1] + self.tile_color[2])//3
# 		# 	pygame.draw.polygon(screen, (color,color,color), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE])
# 		# else:
# 		# 	t
			

# 		# 	border_index = []
# 		# 		if i % 2 == 1:
# 		# 			border_index = template.BORDER_INDEX_ODD
# 		# 		else:
# 		# 			border_index = template.BORDER_INDEX_EVEN
# 		# 		for k in range(len(border_index)):
# 		# 			if not(i + border_index[k][0] >= 0 and j + border_index[k][1] >= 0 and i + border_index[k][0] < len(self.map) and j + border_index[k][1] < len(self.map[i])):
# 		# 				pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)
# 		# 			elif not(self.map[i + border_index[k][0]][j + border_index[k][1]].player_index == self.map[i][j].player_index):
# 		# 				pygame.draw.line(screen, players[self.map[i][j].player_index].color, (temp_pos[0] + template.TILE_EDGE[k][0] * template.CELL_SIZE, temp_pos[1] - template.TILE_EDGE[k][1] * template.CELL_SIZE), (temp_pos[0] + template.TILE_EDGE[(k + 1) % len(border_index)][0] * template.CELL_SIZE , temp_pos[1] - template.TILE_EDGE[(k + 1) % len(border_index)][1] * template.CELL_SIZE),2)  
# 		# #border and highlight
# 		# if highlight:
# 		# 	pygame.draw.polygon(screen, (255,255,0), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 		# else:
# 		# 	pygame.draw.polygon(screen, player_color, [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 		# if other[0] == 'resource':
# 		# 	pass
# 		# if other[0] == 'unit':
# 		# 	if self.unit == None:
# 		# 		pass
# 		# 	else:
# 		# 		self.unit.draw_unit(screen, pos)
# 		# if other[0] == 'population':			
		
		
# # 		pygame.draw.polygon(screen, (255,255,255), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 	# def draw_tile(self, screen, pos):
# 	# 	pygame.draw.polygon(screen, (152,251,152), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE])
# 	# 	temp = pygame.Surface((640,480), pygame.SRCALPHA, 32)
# 	# 	pygame.draw.polygon(screen, (255,255,255), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 	def draw_highlight(self, screen, pos):
# 		pygame.draw.polygon(screen, (255,255,0), [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 	def draw_tile_edge(self, screen, pos, color):
# 		pygame.draw.polygon(screen, color, [(x * template.CELL_SIZE + pos[0], y * template.CELL_SIZE + pos[1]) for x, y in template.TILE_EDGE],2)
# 	def draw_pop(self, screen, pos):	
# 		self.pop.draw_pop(screen, pos)
# 	def total_resource(self, tile_resource, biudling_resource):
# 		temp = material.Material()
# 		temp.add_material(tile_resource[self.tile_type])
# 		temp.add_material(biudling_resource[self.biulding_type])
# 		temp.add_material(self.bonus)
# 		return temp.to_array()
# 	def draw_resource(self, pos, tile_resource, biulding_resource):
# 		map.tileExtra.draw_resource(pos, self.total_resource(tile_resource, biulding_resource))
# 	def draw_unit(self, screen, pos):	
# 		if self.unit == None:
# 			pass
# 		else:
# 			self.unit.draw_unit(screen, pos)