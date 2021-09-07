class circle:
	def __init__(self,l):
		self.radius=l
		
	def show(self):
		print(self.radius)
	def area(self):
		print(self.radius**2*3.14)

	def perimeter(self):
		print(2*(self.radius)*3.14)



a=circle(1)
a.show()
a.area()
a.perimeter()