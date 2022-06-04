import pygame
from card.card import Card
class Hand:
	def  __init__(self, START_POS, DISPLACEMENT, CARD_SIZE):
		self.hand = []
		self.START_POS = START_POS
		self.DISPLACEMENT = DISPLACEMENT
		self.CARD_SIZE = CARD_SIZE
	def add_card(self, card):
		self.hand.append(card)
	def remove_card(self, index):
		self.hand.pop(index)
	def draw_hand(self, screen):
		for index,i in enumerate(self.hand):
			i.draw_pos(screen, (index * self.DISPLACEMENT + self.START_POS[0], self.START_POS[1]))	
	def mouse_over_card(self, mouse_pos):
		if mouse_pos[1] > self.START_POS[1]:
			index = (mouse_pos[0] - self.START_POS[0])//self.DISPLACEMENT	
			if index < len(self.hand) and index >= 0:
				return index
		return -1
	def draw_hovered_card(self, screen, mouse_pos):
		index = self.mouse_over_card(mouse_pos)
		if index != -1:
			self.hand[index].draw_pos(screen, (index * self.DISPLACEMENT + self.START_POS[0], pygame.Surface.get_height(screen) - self.CARD_SIZE[1]))