class Material():
	def  __init__(self, food = 0, hammer = 0, powerpoint = 0):
		self.gold = 0
		self.food = food
		self.hammer = hammer 
		self.powerpoint = powerpoint
	def add_material(self, res):
		self.gold += res.gold
		self.food += res.food
		self.hammer += res.hammer
		self.hammer += res.hammer