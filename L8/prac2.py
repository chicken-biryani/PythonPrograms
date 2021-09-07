#wap for multilevel inheritance

class Person:
	def __init__(self,id,name,addr): #parameterised inirtializer
		self.id=id   #instance variables
		self.name=name
		self.address=addr
	def show(self):
		print("id -", self.id)
		print("name -", self.name)
		print("add -", self.address)

class Teacher(Person): #jo hai upar woh hai super
	def __init__(self,id,name,addr,salary):
		super().__init__(id,name,addr)
		self.salary=salary
	def show(self):
		super().show()
		print("salary is ",self.salary)

class Hod(Teacher): #jo hai upar woh hai super
	def __init__(self,id,name,addr,salary,department):
		super().__init__(id,name,addr,salary)
		self.dept=department
	def show(self):
		super().show()
		print("department is ",self.dept)
	
t=Hod(10,"amit","mum",1000,"comps")
t.show()
		
