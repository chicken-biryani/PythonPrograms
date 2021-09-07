'''Create class Toy with IV:- price
	t1 = Toy(100)
	t2 = Toy(300)
	t3 = Toy(200)
total_bill = t1 + t2 + t3
print(total_bill) = 600
'''
class Toy:
	def __init__(self, price):
		self.price = price
	def __add__(self, other):
		ans = self.price + other.price
		return Toy(ans)
	def __str__(self):
		return str(self.price) 

t1 = Toy(100)
t2 = Toy(300)
t3 = Toy(200)

total_bill = t1 + t2 + t3
print(total_bill)
