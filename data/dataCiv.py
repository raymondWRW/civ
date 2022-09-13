from logic.tech.classicalCivic import *
from logic.tech.classicalMilitary import *
civBuilding = { 
	'none' : {
		'resource' : {},
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'hold' : {
		'resource' : {},
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'farm' : {
		'resource' : {
			'food' : 2
		},
		'housing' : 1,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'workshop' : {
		'resource' : {
			'gold' : 1
		},	
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'mine' : {
		'resource' : {
			'hammer' : 1
		},	
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'lumber camp' : {
		'resource' : {
			'hammer' : 1
		},
		'housing' : 1,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'mill' : {
		'resource' : {
			'hammer' : 3
		},
		'housing' : 1,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'village' : {
		'resource' : {},
		'housing' : 2,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'black smith' : {
		'resource' : {'explosive' : 2},
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'town' : {
		'resource' : {
			'gold' : 1
		},
		'housing' : 2,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'academy' : {
		'resource' : {'research' : 1},
		'housing' : 0,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
}
civUnit = {
	'infantry' :{
		'max health' : 50,
		'damage' : 10,
		'attack range' : 1,
		'max movement' : 2
	},
	'cavalry' : {
		'max health' : 80,
		'damage' : 15,
		'attack range' : 1,
		'max movement' : 1
	},
	'ship' : {
		'max health' : 50,
		'damage' : 5,
		'attack range' : 1,
		'movement' : 5
	}
}
civTile = {
	'none' : {
		'color' : (255, 255, 255),
		'resource' : {},
		'housing' : 0,
		'move cost' : 0,
		'defensivness' : 1,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'plain' : {
		'color' : (152,251,152),
		'resource' : {'food' : 2},
		'housing' : 2,
		'move cost' : 1,
		'defensivness' : 1,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'coast' : {
		'color' : (185, 230, 255),
		'resource' : {'food' : 1},
		'housing' : 1,
		'move cost' : 1,
		'defensivness' : 2,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'ocean' : {
		'color' : (29, 78, 137),
		'resource' : {},
		'housing' : 0,
		'move cost' : 1,
		'defensivness' : 2,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},	
	'wood' : {
		'color' : (4, 71, 28),
		'resource' : {'food' : 1},
		'housing' : 1,
		'move cost' : 2,
		'defensivness' : 0.9,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	},
	'mountain' : {
		'color' : (230,170,104),
		'resource' : {'hammer' : 1},
		'housing' : 1,
		'move cost' : 2,
		'defensivness' : 0.8,
		'modifier' : {
			'resource' : [],
			'other' : []
		}
	}
}
start_civ_placement = []