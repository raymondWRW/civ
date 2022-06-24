#the tile_extra is control for showing the population on a tile and the resource on a tile
import button
import pygame
import template

class Population():
	def __init__(self, max_pop, cur_pop):
		self.max_pop = max_pop
		self.cur_pop = cur_pop
	def draw_pop(self, screen, pos):
		if(self.max_pop % 2 == 1):
			for i in range(self.max_pop):
				pygame.draw.circle(screen, (0, 0, 0), (pos[0] + (i - self.max_pop // 2) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2,2)
				if i < self.cur_pop:
					pygame.draw.circle(screen, (255, 255, 255), (pos[0] + (i - self.max_pop // 2) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2 - 2)	
				else:
					pygame.draw.circle(screen, (152, 251, 152), (pos[0] + (i - self.max_pop // 2) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2 - 2)
		else:
			for i in range(self.max_pop):
				pygame.draw.circle(screen, (0, 0, 0), (pos[0] + (i - self.max_pop // 2 + 0.5) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2, 2)
				if i < self.cur_pop:
					pygame.draw.circle(screen, (255, 255, 255), (pos[0] + (i - self.max_pop // 2 + 0.5) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2 - 2)	
				else:
					pygame.draw.circle(screen, (152, 251, 152), (pos[0] + (i - self.max_pop // 2 + 0.5) * template.CELL_SIZE * 8 / self.max_pop, pos[1]), template.CELL_SIZE * 2 - 2)	
def draw_resource(pos, resource):
	total = 0
	for i in resource:
		total += i[1]
	if total == 0:
		return
	index = 0
	for i in resource:
		res = template.cost_image[i[0]]	
		for j in range(i[1]):
			template.screen.blit(res,(pos[0] + (template.RESOURCE_POS[total][index][0] - 1) * template.CELL_SIZE, pos[1] + (template.RESOURCE_POS[total][index][1] - 1) * template.CELL_SIZE))
			index += 1