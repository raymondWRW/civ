import pygame
from card.settingCard import *
from card.hand import Hand
from coreFunction.dictionaryExtended import *
from coreFunction.hexArray import *
from game.variable import *
from card.scienceTech import *
from civ.civ import Civ

class Mongolia(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (0,102,179))
		add_value(self.tile_resource['plain']['resource'], {'gold' : 1})

  