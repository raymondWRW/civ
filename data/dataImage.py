from coreFunction.surfaceExtended import *
#unit
UNIT_SIZE = 80
unit_image = {
	'infantry' : to_scale("render/image/unit/warrior.png", UNIT_SIZE, UNIT_SIZE),
	'cavalry' : to_scale("render/image/unit/cavalry.png", UNIT_SIZE, UNIT_SIZE),
	'ship' : to_scale("render/image/unit/ship.png", UNIT_SIZE, UNIT_SIZE)
}
#tile
CELL_SIZE = 10
TILE_EDGE = [(0, -8), (6, -4), (6, 4), (0, 8), (-6, 4), (-6, -4)]
BORDER_INDEX_EVEN   = [(-1, 1), (0, 1), (1, 1), (1,  0), (0, -1), (-1,  0)]
BORDER_INDEX_ODD  = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
RESOURCE_POS = [[],
                [(0,0)],
                [(-2,0),(2,0)], 
                [(0,2.5), (-2,-1.5), (2,-1.5)],
                [(1.5,1.5), (-1.5,1.5), (1.5,-1.5), (-1.5,-1.5)],
                [(-3, 1.5), (0, 1.5), (3, 1.5), (-1.5, -1.5), (1.5, -1.5)],
				[(-3, 1.5), (0, 1.5), (3, 1.5), (-3, -1.5), (0, -1.5), (3, -1.5)]
                ]
tile_resource_image = {
	'food' : to_scale("render/image/resource/food.png", CELL_SIZE * 2, CELL_SIZE * 2),
	'gold' : to_scale("render/image/resource/gold.png", CELL_SIZE * 2, CELL_SIZE * 2),
	'research' :  to_scale("render/image/resource/research.png", CELL_SIZE * 2, CELL_SIZE * 2),
	'hammer' : to_scale("render/image/resource/hammer.png", CELL_SIZE * 2, CELL_SIZE * 2),
	'horse' : to_scale("render/image/resource/horse.png", CELL_SIZE * 2, CELL_SIZE * 2),
	'empty population' :to_scale("render/image/resource/emptyPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3),
	'full population' : to_scale("render/image/resource/fullPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3)
}
tile_building_image = {
	'tower' : to_scale("render/image/building/tower.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'workshop' : to_scale("render/image/building/workshop.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'mine' : to_scale("render/image/building/mine.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'farm' : to_scale("render/image/building/farm.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'lumber camp' : to_scale("render/image/building/lumbercamp.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'black smith' : to_scale("render/image/building/blacksmith.png", CELL_SIZE * 4, CELL_SIZE * 4),
	'academy' :  to_scale("render/image/building/academy.png", CELL_SIZE * 4, CELL_SIZE * 4),
}
tile_image = {
	'none' : to_scale("render/image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'plain' : to_scale("render/image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'coast' : to_scale("render/image/tile/coast.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'ocean' : to_scale("render/image/tile/ocean.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'hill' : to_scale("render/image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'wood' : to_scale("render/image/tile/wood.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'mountain' : to_scale("render/image/tile/mountain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha()
}
#card
CARD_HEIGHT = 280
CARD_WIDTH = 200
CARD_TITLE_FONT = pygame.font.SysFont("montserrat", 20)
CARD_TEXT_FONT = pygame.font.SysFont("montserrat", 15)
HAND_HEIGHT = 1000
DICSOVER_HEIGHT = 300
CARD_RESOURCE_SIZE = 20
CARD_IMAGE = pygame.image.load("render/image/cardImage/card.png").convert_alpha()
CARD_RESOURCE_IMAGE = {
	'food' : to_scale("render/image/resource/food.png", CARD_RESOURCE_SIZE, CARD_RESOURCE_SIZE),
	'gold' : to_scale("render/image/resource/gold.png", CARD_RESOURCE_SIZE, CARD_RESOURCE_SIZE),
	'research' : to_scale("render/image/resource/research.png", CARD_RESOURCE_SIZE, CARD_RESOURCE_SIZE),
	'hammer' : to_scale("render/image/resource/hammer.png", CARD_RESOURCE_SIZE, CARD_RESOURCE_SIZE),
	'horse' : to_scale("render/image/resource/horse.png", CARD_RESOURCE_SIZE, CARD_RESOURCE_SIZE)
}
#other
HAND_HEIGHT = 1000
DICSOVER_HEIGHT = 300
RESOURCE_BACKGROUND_SIZE = 50
BUTTON_FONT_SIZE = pygame.font.SysFont("monospace", 50)
BUTTON_NEXT_TURN_POS = (0, 300)
BUTTON_DRAW_CARD_POS= (0, 400)
BUTTON_DELETE_CARD_POS = (0, 500)
RESOURCE_BACKGROUND = pygame.Surface((100,50))
RESOURCE_BACKGROUND.fill((255,255,255))	
RESOURCE_BACKGROUND_GOLD = to_scale("render/image/resource/gold.png", 50, 50).convert_alpha()
RESOURCE_BACKGROUND_FOOD = to_scale("render/image/resource/food.png", 50, 50).convert_alpha()
RESOURCE_BACKGROUND_RESEARCH = to_scale("render/image/resource/research.png", 50, 50).convert_alpha()
RESOURCE_BACKGROUND_HAMMER = to_scale("render/image/resource/hammer.png", 50, 50).convert_alpha()
RESOURCE_BACKGROUND_HORSE = to_scale("render/image/resource/horse.png", 50, 50).convert_alpha()
RESOURCE_FONT = pygame.font.SysFont("monospace", 50)
#buttons
BUTTON_FONT = pygame.font.SysFont("monospace", 20)
	#next turn
BUTTON_NEXT_TURN = to_scale("render/image/template/button template.png", 120, 50)
BUTTON_NEXT_TURN.blit(BUTTON_FONT.render(str("next turn"), 1, (0,0,0)), (5,15))
button_next_turn_pos = (0, 300)
	#draw card
BUTTON_DRAW_CARD = to_scale("render/image/template/button template.png", 120, 50)
BUTTON_DRAW_CARD.blit(BUTTON_FONT.render(str("draw card"), 1, (0,0,0)), (5,15))
button_draw_card_pos = (0, 400)
	#delete card
BUTTON_DELETE_CARD = to_scale("render/image/template/button template.png", 120, 50)
BUTTON_DELETE_CARD.blit(BUTTON_FONT.render(str("delete card"), 1, (0,0,0)), (5,15))
button_delete_card_pos = (0, 500)



ERROR_MESSAGE_FONT = pygame.font.SysFont("montserrat", 50)

MARKET_NAME_FONT = pygame.font.SysFont("montserrat", 50)
MARKET_IMAGE = to_scale("render/image/template/market.png", 1200, 750)
MARKET_PLAYER_NAME = pygame.surface.Surface((150, 70))
MARKET_PLAYER_NAME.fill((255,255,255))