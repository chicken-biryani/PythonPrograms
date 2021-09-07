class rectangle:
	def __init__(self,l,width):
		self.length=l
		self.width=width
	def show(self):
		print(self.length,self.width)
	def area(self):
		print(self.length*self.width)

	def perimeter(self):
		print(2*(self.length+self.width))

a=rectangle(1,2)
a.show()
a.area()
a.perimeter()

