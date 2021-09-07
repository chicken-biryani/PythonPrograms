class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address
	def show(self):
		print(self.id)
		print(self.name)
		print(self.address)

class Teacher(Person):
	def __init__(self,id,name,address,salary):
		super().__init__(id,name,address)
		self.salary=salary
	def show(self):
		super().show()
		print(self.salary)
class Hod(Teacher):
	def __init__(self,id,name,address,salary,dept):
		super().__init__(id,name,address,salary)
		self.dept=dept
	def show(self):
		super().show()
		print(self.dept)

h=Hod(10,"amit","mum",5600,"comps")
h.show()

