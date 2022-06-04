# thing involves player cards, decks etc
import card.card
import card.deck
import card.hand
import pygame
class PlayerCard:
	def  __init__(self):
		self.hand = card.hand.Hand((50, 600), 120,(100, 280))
		self.deck = []
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
	def evaluate(self, board, players, visible_screen, order, index):
		self.hand.hand[order[0][2].evaluate(board, players, visible_screen, order, index)]