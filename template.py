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
RESOURCE_FONT = pygame.font.SysFont("monospace", 50)#the showing player's resources
RESOURCE_FOOD_1 = to_scale("image/buttonImage/wheat.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_FOOD_2 = to_scale("image/buttonImage/wheat.png", 50, 50)
RESOURCE_GOLD_1 = to_scale("image/buttonImage/gold.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_GOLD_2 =  to_scale("image/buttonImage/gold.png", 50, 50)

#buttons
BUTTON_FONT = pygame.font.SysFont("monospace", 20)
	#next turn
BUTTON_NEXT_TURN = to_scale("image/buttonImage/button template.png", 120, 50)
BUTTON_NEXT_TURN.blit(BUTTON_FONT.render(str("next turn"), 1, (0,0,0)), (5,15))
	#draw card
BUTTON_DRAW_CARD = to_scale("image/buttonImage/button template.png", 120, 50)
BUTTON_DRAW_CARD.blit(BUTTON_FONT.render(str("draw card"), 1, (0,0,0)), (5,15))
	#delete card
BUTTON_DELETE_CARD = to_scale("image/buttonImage/button template.png", 120, 50)
BUTTON_DELETE_CARD.blit(BUTTON_FONT.render(str("delete card"), 1, (0,0,0)), (5,15))
#unit
UNIT_WARRIOR = to_scale("image/buttonImage/warrior.png", CELL_SIZE * 2, CELL_SIZE * 2)