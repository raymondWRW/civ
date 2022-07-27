from card.scienceTech import *
color = {
	'basic' : (153, 102, 204)
}
civ_tile_resource = {
	'none'  : {
		'resource' : {},
		'housing' : 0
    },
	'plain' : {
		'resource' : {
			'food' : 2
		},
		'housing' : 2
	}
}
civ_starting_material = {
    'food' : 100,
    'research' : 10,
    'hammer' : 10,
    'gold' : 10
}
civ_starting_income = {
    'food' : 1,
    'research' : 1,
    'hammer' : 1,
    'gold' : 1
}
civ_building_income = {
	'none' : {
		'resource' : {},
		'housing' : 0,
		'modifier' : []
    },
	'farm' : {
		'resource' : {
			'food' : 2
		},
		'housing' : 1,
		'modifier' : []
	},
	'workshop' : {
		'resource' : {
			'hammer' : 1
		},	
		'housing' : 0,
		'modifier' : []
	},
	'mine' : {
		'resource' : {
			'hammer' : 1
		},	
		'housing' : 0,
		'modifier' : []
	},
	'lumber camp' : {
		'resource' : {
			'hammer' : 1
		},
		'housing' : 1,
		'modifier' : []
	},
	'mill' : {
		'resource' : {
			'hammer' : 3
		},
		'housing' : 1,
		'modifier' : []
	},
	'village' : {
		'resource' : {},
		'housing' : 2,
		'modifier' : []
	},
	'town' : {
		'resource' : {
			'gold' : 1
		},
		'housing' : 2,
		'modifier' : []
	},
	'wall' : {
		'resource' : {
			'gold' : 1
		},
		'housing' : 2,
		'modifier' : []
	}
}
MAX_HAND_SIZE = 7
tech = {
	'classical science' : {
		'tech' : ClassicalScience(),
		'required' : {
			'tech' : [],
			'amount' : 0
		},
		'future tech' : ['animal husbandry'],
		'researched' : False
    },
	'animal husbandry' : {
		'tech' : AnimalHusbandry(),
		'required' : {
			'tech' : ['classical science'],
			'amount' : 1
		},
		'future tech' : ['pasture'],
		'researched' : False
    },
	'pasture' : {
		'tech' : Pasture(),
		'required' : {
			'tech' : ['animal husbandry'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
    }
}