#wapp for demonstrating operator overloading
class Book:
	def __init__(self, pages):
		self.pages = pages
	def __add__(self, other):
		ans = self.pages + other.pages
		return ans
	def __sub__(ajay, vijay):
		ans = ajay.pages - vijay.pages
		return ans
b1 = Book(100)
b2 = Book(200)

r1 = b1 + b2
print("Result 1 = ", r1)
r2 = b1 - b2
print("Result 2 = ", r2)







