'''OOP for class for class rectangle: 
	IV: length and width
	PI: for length and width
	IM: area() --> show area of rect
	IM: perimeter --> show peri of rect
do test the above by creating object '''


class rectangle:
	def __init__(self,le,wi):  #self is address of object
		self.length = le
		self.width = wi

	def show(self):   #non-static methods have self word in them like woh obj se related hai
		print("length is ",self.length)
		print("width is ",self.width)

	def area(self):
		ans=self.length*self.width
		print("area = ",round(ans,2))
	def perimeter(self):
		ans = 2 * (self.length+self.width)
		print("perimeter = ",round(ans,3)


le = float(input("enter length"))
wi = float(input("enter width"))
rect1 = rectangle(le,wi)
rect1.show()
rect1.area()
rect1.perimeter()



