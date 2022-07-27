import pygame, random
class Deck():
	def  __init__(self):
		self.deck = []
	def add_card(self, card):
		self.deck.append(card)
	def draw(self):
		temp = self.deck[0]	
		del self.deck[0]
		return temp	
	def shuffle(self):
		random.shuffle(self.deck)