from logic.card import Card
from data.dataGame import *
class Administration(Card):
	def __init__(self):
		super().__init__('administration', {}, 'draw a card after you played a biulding')
	def evaluate(self):
		player[self.index].modifier.append('administration')

class Exploration(Card):
	def __init__(self):
		super().__init__('exploration', {}, 'gain one science for every 3 tile added to your country')
	def evaluate(self):
		player[self.index].modifier.append('exploration3')

class Insight(Card):
	def __init__(self):
		super().__init__('insight', {}, 'gain one gold when destroying a card')
	def evaluate(self):
		player[self.index].modifier.append('insight')