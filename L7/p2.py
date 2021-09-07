'''	waoopp for class circle:
	IV:	radius
	DI:	for radius
	IM:	showdata() for showing radius
		area() for area of circle
		circum() for circumference of circle
'''
class circle:
	def __init__(self):
		self.radius = 0.0
	def showdata(self):
		print("Radius = ",self.radius)
	def area(self):
		ans = 3.14159 * self.radius ** 2
		print("Area of circle ",ans)
	
	def circum(self):
		ans = 2 * 3.14159 * self.radius
		print("Circumference = ",ans)

rad = float(input("Enter radius "))
c = circle( )
c.radius = rad
c.showdata()
c.area()
c.circum() 