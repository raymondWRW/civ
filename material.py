class Material():
	def  __init__(self, res = []):
		self.material = {
			'food' : 0,	
			'hammer' : 0,
			'science' : 0,
			'gold' : 0
		}
		self.special_material = {
			'horse' : 0,	
			'wood' : 0,
			'coal' : 0,
			'gunpowder' : 0,
			'oil' : 0
		}
		self.extra = {
			'maxpopulation' : 0,
			'population' : 0,
			'tilecolor' : (0,0,0)
		}
		for i in res:
			if i[0] in self.material:
				self.material[i[0]] += i[1]
			if i[0] in self.special_material:
				self.special_material[i[0]] += i[1]
	def add_material(self, res):
		for i in res:
			if i[0] in self.material:
				self.material[i[0]] += i[1]
			if i[0] in self.special_material:
				self.special_material[i[0]] += i[1]
	def remove_material(self, res):
		for i in res:
			if i[0] in self.material:
				self.material[i[0]] -= i[1]
			if i[0] in self.special_material:
				self.special_material[i[0]] -= i[1]
	def multiple_add_material(self, res, time):
		for i in res:
			if i[0] in self.material:
				self.material[i[0]] += i[1] * time
			if i[0] in self.special_material:
				self.special_material[i[0]] += i[1] * time
	def multiple_remove_material(self, res, time):
		for i in res:
			if i[0] in self.material:
				self.material[i[0]] -= i[1] * time
			if i[0] in self.special_material:
				self.special_material[i[0]] -= i[1] * time
	def total_material(self):
		total = 0
		for i, j in self.material.items():
			total += j
		for i, j in self.special_material.items():
			total += j
		return total	
	def to_array(self):
		arr = []
		for i,j in self.material.items():
			if j != 0:
				arr.append((i,j))
		for i,j in self.special_material.items():
			if j != 0:
				arr.append((i,j))
		return arr
	def greater(self, res):
		for i in res:
			if i[0] in self.material:
				if self.material[i[0]] < i[1]:
					return False
			if i[0] in self.special_material:
				if self.material[i[0]] < i[1]:
					return False
		return True