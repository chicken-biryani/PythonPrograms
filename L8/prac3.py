class Pcm:
	def __init__(self,p,c,m):
		self.p=p
		self.c=c
		self.m=m
	def show(self):
		print("phy = ",self.p)
		print("chem = ",self.c)
		print("math = ",self.m)

class Nonpcm:
	def __init__(self,e,b):
		self.e=e
		self.b=b
		
	def show(self):
		print("eng = ",self.e)
		print("bio = ",self.b)
	
class Marks(Pcm,Nonpcm):
	def __init__(self,p,c,m,e,b):
		Pcm.__init__(self,p,c,m)
		Nonpcm.__init__(self,e,b)
	def show(self):
		Pcm.show(self)
		Nonpcm.show(self)
m=Marks(99,88,66,77,10)
m.show()