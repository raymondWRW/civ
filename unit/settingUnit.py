import pygame
from coreFunction.surfaceExtended import to_scale
from board.settingTile import CELL_SIZE
UNIT_WARRIOR = to_scale("image/unit/warrior.png", CELL_SIZE * 8, CELL_SIZE * 8)
UNIT_CAVALRY = to_scale("image/unit/cavalry.png", CELL_SIZE * 8, CELL_SIZE * 8)
unit_image = {
	'warrior' : UNIT_WARRIOR,
	'cavalry' : UNIT_CAVALRY,
}
unit_stat = {
	'warrior' : {
		'max health' : 100,
		'damage' : 20,
		'attack range' : 1,
		'max movement' : 1
	},
	'cavalary' : {
		'max health' : 100,
		'damage' : 10,
		'attack range' : 1,
		'movement' : 2
	},
	'seigemachine' : {
		'max health' : 100,
		'damage' : 10,
		'attackrange' : 1,
		'movement' : 2
	},
	'pikeandshot' : {
		'max health' : 100,
		'damage' : 10,
		'attack range' : 1,
		'movement' : 2
	},
	'artillery' : {
		'max health' : 100,
		'damage' : 10,
		'attack range' : 1,
		'movement' : 2
	},
	'tank' : {
		'max health' : 100,
		'damage' : 10,
		'attack range' : 1,
		'movement' : 2
	}
}