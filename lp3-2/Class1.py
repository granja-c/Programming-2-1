
class Class1:
	def __init__(self, diam):
		self.diam = diam
		self.RENT = 1
		self.LABOR = 0.75
		self.mat = 0
		self.cost = 0
		
		def calc(self):
			self.mat = 0.05 * self.diam ** 2
			self.cost = self.mat + self.RENT + self.LABOR
		
		def getCost(self):
			return self.cost
		pass
