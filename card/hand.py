from lib2to3.pytree import convert
import pygame
from coreFunction.surfaceExtended import within_dimesion
from card.settingCard import CARD_WIDTH, CARD_HEIGHT
class Hand:
	def  __init__(self, HEIGHT):
		self.hand = []
		self.HEIGHT = HEIGHT
	def pos_to_index(self, mouse_pos):
		for i in range(len(self.hand) - 1, - 1,-1):
			if within_dimesion(mouse_pos, (CARD_WIDTH, CARD_HEIGHT), (i * 120, self.HEIGHT)):
				return i
		return -1