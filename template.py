import pygame, sys
from pygame.locals import *
pygame.init()
#screen
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 750
pygame.display.set_caption("modernity")
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#card
CARD_HEIGHT = 280
CARD_WIDTH = 100
CARD_TITLE_FONT = pygame.font.SysFont("monospace", 15)
CARD_TEXT_FONT = pygame.font.SysFont("monospace", 10)

#tile
CELL_SIZE = 10
TILE_EDGE = [(0,8), (6,4), (6, -4), (0,-8), (-6, -4), (-6, 4)]

# the following will be for the art of the program
def to_scale(name, width, height):
	temp = pygame.image.load(str(name)).convert_alpha()
	return pygame.transform.scale(temp,(width, height))
    
#card picture
CARD_CARD = to_scale("image/cardImage/card.png", CARD_WIDTH, CARD_HEIGHT)
CARD_POPULATIONGROWTH = ("image/cardImage/card.png", CARD_WIDTH, CARD_HEIGHT)
#resource and population
RESOURCE_FOOD = to_scale("image/buttonImage/wheat.png", CELL_SIZE * 2, CELL_SIZE * 2)

#buttons

#unit