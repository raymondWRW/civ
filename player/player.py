#what a player is in this game
# a player needs recources
#tile
#color 
import material, card.card, card.deck, card.hand
class Player:
	def  __init__(self, color, index):
		#for identification
		self.color = color
		self.index = index
		#resources & income
		self.capital = material.Material()
		self.income = material.Material()
		#territory and borders
		self.tile = []
		#cards
		self.hand = card.hand.Hand((50, 600), 120,(100, 280))
		self.deck = []
		#army

		#initialize	
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
		self.hand.add_card(card.card.PopulationGrowth())
	def evaluate_hand(self, board, players, visible_screen, order):
		self.hand.hand[order[0][2]].evaluate(board, players, visible_screen, order, self.index)