''' waoopp for class rectangle:
	IV : length and width
	PI : for length and width
	IM : area() and perimeter()
'''
class rectangle:
	def __init__(self, length,width):
		self.length = length
		self.width = width
	def area(self):
		ans = self.length * self.width
		print("area = ",ans)
	def perimeter(self):
		ans = 2 * (self.length + self.width)
		print("Perimeter = ",ans)

len = float(input("Enter the length "))
wid =float(input("Enter the width "))
r1 = rectangle(len,wid)
r1.area()
r1.perimeter()