#wap to perform addition of two book objects

class Book(object):#object is everyone's papa and is inherited by default
	def __init__(self,nop):
		self.nop=nop
	def __add__(self,other):
		ans = self.nop+other.nop
		return ans

b1=Book(100)
b2=Book(200)

res=b1+b2
print("res = ",res)

#operator overloading by overriding method 