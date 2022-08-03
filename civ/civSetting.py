from card.scienceTech import *
from card.militaryTech import *
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
	},
	'wood' : {
		'resource' : {
			'food' : 2
		},
		'housing' : 1
	},
	'mountain' : {
		'resource' : {
			'hammer' : 1
		},
		'housing' : 1
	},
	'coast' : {
		'resource' : {
			'food' : 1
		},
		'housing' : 1
	},
	'ocean' : {
		'resource' : {
			'food' : 0
		},
		'housing' : 0
	}
}
civ_starting_material = {
    'food' : 10,
    'research' : 10,
    'hammer' : 10,
    'gold' : 10,
	'horse' : 0
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
			'gold' : 1
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
		'future tech' : ['animal husbandry', 'organization', 'flint', ],
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
    },
	'organization' : {
		'tech' : Organization(),
		'required' : {
			'tech' : ['classical science'],
			'amount' : 1
		},
		'future tech' : ['fishing', 'irrigation', 'mathematic'],
		'researched' : False
    },
	'fishing' : {
		'tech' : Fishing(),
		'required' : {
			'tech' : ['organization'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
	},
	'irrigation' : {
		'tech' : Irrigation(),
		'required' : {
			'tech' : ['organization'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
	},
	'mathematic' : {
		'tech' : Mathematic(),
		'required' : {
			'tech' : ['organization', 'flint'],
			'amount' : 2
		},
		'future tech' : [],
		'researched' : False
	},
	'flint' : {
		'tech' : Flint(),
		'required' : {
			'tech' : ['classical science'],
			'amount' : 1
		},
		'future tech' : ['mathematic', 'logging', 'bronze working'],
		'researched' : False
	},
	'logging' : {
		'tech' : Logging(),
		'required' : {
			'tech' : ['flint'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
	},
	'bronze working' : {
		'tech' : BronzeWorking(),
		'required' : {
			'tech' : ['flint'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
	},
#military
	'spear' : {
		'tech' : Spear(),
		'required' : {
			'tech' : [],
			'amount' : 0
		},
		'future tech' : ['military tradition'],
		'researched' : False
    },
	'military tradition' : {
		'tech' : MilitaryTradition(),
		'required' : {
			'tech' : ['spear'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
	},
	'standard uniform' : {
		'tech' : StandardUniform(),
		'required' : {
			'tech' : [],
			'amount' : 0
		},
		'future tech' : [],
		'researched' : False
    },
	'chariot' : {
		'tech' : Chariot(),
		'required' : {
			'tech' : [],
			'amount' : 0
		},
		'future tech' : ['horseback riding'],
		'researched' : False
    },
	'horseback riding' : {
		'tech' : HorsebackRiding(),
		'required' : {
			'tech' : ['chariot'],
			'amount' : 1
		},
		'future tech' : [],
		'researched' : False
    }
}
# class Fishing(ScienceTech):
# class Irrigation(ScienceTech):
# class Mathematic(ScienceTech):

# class Logging(ScienceTech):
# class BronzeWorking(ScienceTech):

# class Flint(ScienceTech):