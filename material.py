class Material():
	def  __init__(self, food = 0, hammer = 0, science = 0):
		self.gold = 0
		self.food = food
		self.hammer = hammer 
		self.science = science
	def add_material(self, res):
		self.gold += res.gold
		self.food += res.food
		self.hammer += res.hammer
		self.hammer += res.hammer
	def remove_material(self, res):
		self.gold -= res.gold
		self.food -= res.food
		self.hammer -= res.hammer
		self.hammer -= res.hammer