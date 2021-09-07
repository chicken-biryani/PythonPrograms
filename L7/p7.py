class A:
	def __init__(self, p, c, m):
		self.p = p
		self.c = c
		self.m = m
	def show(self):
		print("p = ",self.p, "c = ",self.c, "m = ", self.m)
class B:
	def __init__(self, e, b):
		self.e = e
		self.b = b
		
	def show(self):
		print("e = ",self.e, "b = ",self.b)
class C (A,B):
	def __init__(self, p, c, m,e,b):
		A.__init__(self, p, c, m)
		B.__init__(self,e, b)
		self.total = p + c + m + e + b
	def show(self):
		A.show(self)
		B.show(self)
		print("total = ",self.total)
c = C(99, 88, 98, 77, 89)
c.show()
	












