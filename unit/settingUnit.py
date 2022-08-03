import pygame
from coreFunction.surfaceExtended import to_scale
from board.settingTile import CELL_SIZE
UNIT_WARRIOR = to_scale("image/unit/warrior.png", CELL_SIZE * 8, CELL_SIZE * 8).convert_alpha()
UNIT_CAVALRY = to_scale("image/unit/cavalry.png", CELL_SIZE * 8, CELL_SIZE * 8).convert_alpha()
unit_image = {
	'warrior' : UNIT_WARRIOR,
	'cavalry' : UNIT_CAVALRY,
}
unit_stat = {
	'warrior' : {
		'max health' : 50,
		'damage' : 10,
		'attack range' : 1,
		'max movement' : 1
	},
	'cavalry' : {
		'max health' : 60,
		'damage' : 12,
		'attack range' : 1,
		'max movement' : 1
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