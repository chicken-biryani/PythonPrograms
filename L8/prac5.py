class Mech:
	def __init__(self,price):
		self.price = price
	def __add__(self,other):
		ans = self.price+other.cost
		return ans
	def __sub__(self,other):
		ans = self.price-other.cost
		return ans

class Bee:
	def __init__(self,cost):
		self.cost = cost
	def __add__(self,other):
		ans = self.cost+other.price
		return ans
	
#trick: jo iske pehle likha hai in error uske pehle jaake karnay
m=Mech(700)
b=Bee(300)
r1=m+b
r2=m-b
r3=b+m

print(r1)
print(r2)
print(r3)