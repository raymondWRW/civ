import pygame
from pygame.locals import *
from coreFunction.surfaceExtended import to_scale
#card
CARD_HEIGHT = 280
CARD_WIDTH = 200
CARD_TITLE_FONT = pygame.font.SysFont("montserrat", 20)
CARD_TEXT_FONT = pygame.font.SysFont("montserrat", 15)
CARD_FOOD = to_scale("image/resource/food.png", 20, 20)
CARD_GOLD = to_scale("image/resource/gold.png", 20, 20)
CARD_REASEARCHPOINT = to_scale("image/resource/research.png", 20, 20)
CARD_HAMMER = to_scale("image/resource/hammer.png", 20, 20)
CARD_HORSE = to_scale("image/resource/horse.png", 20, 20)
HAND_HEIGHT = 1000
DICSOVER_HEIGHT = 300
card_resource_size = 20
card_resource_image = {
	'food' : CARD_FOOD,
	'gold' : CARD_GOLD,
	'research' : CARD_REASEARCHPOINT,
	'hammer' : CARD_HAMMER,
	'horse' : CARD_HORSE
}