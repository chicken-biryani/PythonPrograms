'''create class Mech with IV :- nop(no.of.pages)
               class Bee with IV:-pages
                m = Mech(200)
                b = Bee(100)
                r1 = m + b = 300
                r2 = m - b = 100 
                r3 = b - m = -100 
'''
class Mech:
	def __init__(self, nop):
		self.nop = nop
	def __add__(self, other):
		ans = self.nop + other.pages
		return ans
	def __sub__(self, other):
		ans = self.nop - other.pages
		return ans

class Bee:	
	def __init__(self, pages):
		self.pages = pages
	def __sub__(self, other):
		ans = self.pages - other.nop
		return ans
m = Mech(200)
b = Bee(100)

r1 = m + b 
print(r1)

r2 = m - b 
print(r2)

r3 = b - m 
print(r3)
