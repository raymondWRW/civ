from coreFunction.surfaceExtended import to_scale
from game.variable import screen
CELL_SIZE = 10
TILE_EDGE = [(0, -8), (6, -4), (6, 4), (0, 8), (-6, 4), (-6, -4)]
BORDER_INDEX_EVEN   = [(-1, 1), (0, 1), (1, 1), (1,  0), (0, -1), (-1,  0)]
BORDER_INDEX_ODD  = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
RESOURCE_POS = [[],
                [(0,0)],
                [(-2,0),(2,0)], 
                [(0,2.5), (-2,-1.5), (2,-1.5)],
                [(1.5,1.5), (-1.5,1.5), (1.5,-1.5), (-1.5,-1.5)],
                [(-2, 1), (0, 1), (2, 1), (-1, -1), (1, -1)],
				[(-2, 1), (0, 1), (2, 1), (-2, -1), (0, -1), (2, -1)]
                ]
RESOURCE_FOOD_TILE = to_scale("image/resource/food.png", CELL_SIZE * 2, CELL_SIZE * 2).convert_alpha()
RESOURCE_GOLD_TILE = to_scale("image/resource/gold.png", CELL_SIZE * 2, CELL_SIZE * 2).convert_alpha()
RESOURCE_REASEARCHPOINT_TILE = to_scale("image/resource/research.png", CELL_SIZE * 2, CELL_SIZE * 2).convert_alpha()
RESOURCE_HAMMER_TILE = to_scale("image/resource/hammer.png", CELL_SIZE * 2, CELL_SIZE * 2).convert_alpha()
RESOURCE_HORSE_TILE = to_scale("image/resource/horse.png", CELL_SIZE * 2, CELL_SIZE * 2).convert_alpha()
RESOURCE_EMPTYPOPULATION_TILE = to_scale("image/resource/emptyPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3).convert_alpha()
RESOURCE_FULLPOPULATION_TILE = to_scale("image/resource/fullPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3).convert_alpha()
resource_image = {
	'food' : RESOURCE_FOOD_TILE,
	'gold' : RESOURCE_GOLD_TILE,
	'research' : RESOURCE_REASEARCHPOINT_TILE,
	'hammer' : RESOURCE_HAMMER_TILE,
	'horse' : RESOURCE_HORSE_TILE
}
tile_color = {
	'none' : (255,255,255),
	'plain' : (152,251,152),
	'coast' : (185, 230, 255),
	'wood' : (5,5,5),
	'ocean' : (29, 78, 137),
	'hill' : (230,170,104),
	'mountain' : (230,170,104)
}
tile_image = {
	'none' : to_scale("image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'plain' : to_scale("image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'coast' : to_scale("image/tile/coast.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'ocean' : to_scale("image/tile/ocean.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'hill' : to_scale("image/tile/plain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'wood' : to_scale("image/tile/wood.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha(),
	'mountain' : to_scale("image/tile/mountain.png", CELL_SIZE * 16, CELL_SIZE * 16).convert_alpha()
}
# base_tile_resource ={
# 	'none'  : {}, 
# 	'ocean' : {
# 		'resource' : {
# 			'food' : 2
# 		},
# 		'name' : 'ocean',
# 		'housing' : 0,
# 		'color' : (29, 78, 137)
# 	},
# 	'plain' : {
# 		'resource' : {
# 			'food' : 2
# 		},
# 		'name' : 'plain',
# 		'housing' : 2,
# 		'color' : (152,251,152)
# 	},
# 	'hill' : {
# 		'resource' : {
# 			'food' : 1
# 		},
# 		'name' : 'hill',
# 		'housing' : 2,
# 		'color' : (230,170,104)
# 	},
# 	'mountain' : {
# 		'resource' : {
# 			'food' : 1
# 		},
# 		'name' : 'mountain',
# 		'housing' : 1,
# 		'color' : (230,170,104)
# 	}
# }