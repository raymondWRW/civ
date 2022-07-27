from coreFunction.surfaceExtended import to_scale
CELL_SIZE = 10
TILE_EDGE = [(0, -8), (6, -4), (6, 4), (0, 8), (-6, 4), (-6, -4)]
BORDER_INDEX_EVEN   = [(-1, 1), (0, 1), (1, 1), (1,  0), (0, -1), (-1,  0)]
BORDER_INDEX_ODD  = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
RESOURCE_POS = [[],[(0,0)],[(-2,0),(2,0)], [(0,2.5),(-2,-1.5),(2,-1.5)],[(1.5,1.5),(-1.5,1.5),(1.5,-1.5),(-1.5,-1.5)]]
RESOURCE_FOOD_TILE = to_scale("image/resource/food.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_GOLD_TILE = to_scale("image/resource/gold.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_REASEARCHPOINT_TILE = to_scale("image/resource/research.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_HAMMER_TILE = to_scale("image/resource/hammer.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_HORSE_TILE = to_scale("image/resource/horse.png", CELL_SIZE * 2, CELL_SIZE * 2)
RESOURCE_EMPTYPOPULATION_TILE = to_scale("image/resource/emptyPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3)
RESOURCE_FULLPOPULATION_TILE = to_scale("image/resource/fullPopulation.png", CELL_SIZE * 3, CELL_SIZE * 3)
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
	'ocean' : (29, 78, 137),
	'hill' : (230,170,104),
	'mountain' : (230,170,104)
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