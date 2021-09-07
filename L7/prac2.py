'''OOP for class for class circel: 
	IV:radius 
	PI: radius
	IM: area() --> show area of rect
	IM: circumf() --> show peri of cir
do test the above by creating object '''


class circle:
	def __init__(self,a):  #self is address of object
		
		self.radius = a

	def display(self):   #non-static methods have self word in them like woh obj se related hai
		print("length is ",self.radius)
		

	def area(self):
		ans=self.radius*self.radius*3.142
		print("area = ",round(ans,2))
	def circumf(self):
		ans = 2 *self.radius*3.142
		print("circumf = ",round(ans,3))

a = float(input("enter radius"))

r=circle(a)
r.area()
r.circumf()



