'''	waoopp for class employee:
	IV: eid,ename and esalary
	PI: for eid,ename and esalary
	IM: show() for showing eid, ename and esalary
	       compute_tax() if esalary > 2 lakhs then 20%
		              else 10%
	create objects also
'''
class employee:
	def __init__(self, id, n, sal):
		self.eid = id
		self.ename = n
		self.esalary = sal
	def show(self):
		print("eid ", self.eid)
		print("ename ", self.ename)
		print("esalary ", self.esalary)
	def compute_tax(self):
		if self.esalary >= 200000:
			tax = self.esalary * 0.20
		else:
			tax = self.esalary * 0.10
		print("Tax ",tax)
id = int(input("Enter Eid "))
n = input("Enter name ")
sal = float(input("Enter salary "))
e = employee(id,n,sal)
e.show()
e.compute_tax()

			






	