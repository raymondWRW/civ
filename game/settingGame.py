from lib2to3.pytree import convert
from coreFunction.surfaceExtended import to_scale
import pygame
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 750
FPS = 30
RESOURCE_BACKGROUND = pygame.Surface((100,50))
RESOURCE_BACKGROUND.fill((255,255,255))	
RESOURCE_BACKGROUND_GOLD = to_scale("image/resource/gold.png", 50, 50)
RESOURCE_BACKGROUND_FOOD = to_scale("image/resource/food.png", 50, 50)
RESOURCE_BACKGROUND_RESEARCH = to_scale("image/resource/research.png", 50, 50)
RESOURCE_BACKGROUND_HAMMER = to_scale("image/resource/hammer.png", 50, 50)
RESOURCE_BACKGROUND_HORSE = to_scale("image/resource/horse.png", 50, 50)
RESOURCE_FONT = pygame.font.SysFont("monospace", 50)
BOARD_ROW = 15
BOARD_COL  = 30
#buttons
BUTTON_FONT = pygame.font.SysFont("monospace", 20)
	#next turn
BUTTON_NEXT_TURN = to_scale("image/template/button template.png", 120, 50)
BUTTON_NEXT_TURN.blit(BUTTON_FONT.render(str("next turn"), 1, (0,0,0)), (5,15))
button_next_turn_pos = (0, 300)
	#draw card
BUTTON_DRAW_CARD = to_scale("image/template/button template.png", 120, 50)
BUTTON_DRAW_CARD.blit(BUTTON_FONT.render(str("draw card"), 1, (0,0,0)), (5,15))
button_draw_card_pos = (0, 400)
	#delete card
BUTTON_DELETE_CARD = to_scale("image/template/button template.png", 120, 50)
BUTTON_DELETE_CARD.blit(BUTTON_FONT.render(str("delete card"), 1, (0,0,0)), (5,15))
button_delete_card_pos = (0, 500)