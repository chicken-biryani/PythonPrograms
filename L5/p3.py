# waPF to overload area() and find 
#	1.area of Rectangle
#	2.area of circle

def area(a = None , b = None):
	if a is not None and b is not None:
		ans = a * b
		print("Area of rectangle ",ans)
	elif a is not None and b is None:
		ans = 3.14159 * a ** 2
		print("Area of circle ",ans)
area(3.45)
area(10 , 20)
		













