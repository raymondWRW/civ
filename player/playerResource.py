class PlayerResource:
	def  __init__(self):
		self.resource = {
			'food' : 0,
			'hammer' : 0,
			'gold' : 0
		}
		self.income = {
			'food' : 0,
			'hammer' : 0,
			'gold' : 0
		}
	def new_turn(self):
		for key,value in self.income.items():
			self.resource[key] += value