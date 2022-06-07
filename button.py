#similar to card but for the buttons
#nextturn button
#draw card button
#sell card button
import pygame
import template
class Button():
	def  __init__(self, image, name = 'button'):
		self.name = name
		self.mask = pygame.mask.from_surface(image)
		self.image = image
	def draw_Button(self, screen, pos):
		screen.blit(self.image, pos)
	def within_boundary(self, pos, mouse_pos):
		temp_pos = (mouse_pos[0] - pos[0],mouse_pos[1] - pos[1])
		if temp_pos[0] > 0 and temp_pos[1] > 0 and temp_pos[0] < self.mask.get_size()[0] and temp_pos[1] < self.mask.get_size()[1]:
			return True
		# if mouse_pos[0] - pos[0] < self.mask.get_size()[0] and mouse_pos[1] - pos[1] <  self.mask.get_size()[1]:
		# 	return self.mask.get_at((mouse_pos[0] - pos[0], mouse_pos[1] - pos[1]))
