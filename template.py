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
BORDER_INDEX_EVEN   = [(-1, 1), (0, 1), (1, 1), (1,  0), (0, -1), (-1,  0)]
BORDER_INDEX_ODD  = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
RESOURCE_POS = [[],[(0,0)],[(-2,0),(2,0)], [(0,2.5),(-2,-1.5),(2,-1.5)],[(1.5,1.5),(-1.5,1.5),(1.5,-1.5),(-1.5,-1.5)]]
# the following will be for the art of the program
def to_scale(name, width, height):
	temp = pygame.image.load(str(name)).convert_alpha()
	return pygame.transform.smoothscale(temp,(width, height))

#card picture
CARD_CARD = to_scale("image/cardImage/card.png", CARD_WIDTH, CARD_HEIGHT)
CARD_POPULATIONGROWTH = ("image/cardImage/card.png", CARD_WIDTH, CARD_HEIGHT)
#resource and population
RESOURCE_FONT = pygame.font.SysFont("monospace", 50)#the showing player's resources
RESOURCE_FOOD_1 = to_scale("image/buttonImage/wheat.png", CELL_SIZE * 2, CELL_SIZE * 2)
pygame.draw.circle(RESOURCE_FOOD_1,(0,0,0),(CELL_SIZE, CELL_SIZE),CELL_SIZE, 1)
RESOURCE_FOOD_2 = to_scale("image/buttonImage/wheat.png", 50, 50)
RESOURCE_GOLD_1 = to_scale("image/buttonImage/gold.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_GOLD_2 =  to_scale("image/buttonImage/gold.png", 50, 50)
RESOURCE_SCIENCE_1 = to_scale("image/buttonImage/science.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_SCIENCE_2 =  to_scale("image/buttonImage/science.png", 50, 50)
RESOURCE_HAMMER_1 = to_scale("image/buttonImage/hammer.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_HAMMER_2 = to_scale("image/buttonImage/hammer.png", 50, 50)
cost_image = {
	'food' : RESOURCE_FOOD_1,
	'gold' : RESOURCE_GOLD_1,
	'science' : RESOURCE_SCIENCE_1,
	'hammer' : RESOURCE_HAMMER_1
}
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
UNIT_WARRIOR = to_scale("image/buttonImage/warrior.png", CELL_SIZE * 8, CELL_SIZE * 8)
pygame.draw.circle(UNIT_WARRIOR,(0,0,0),(CELL_SIZE * 4, CELL_SIZE * 4),CELL_SIZE * 4,5)