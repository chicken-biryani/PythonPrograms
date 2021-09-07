#wap for single inheritance

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

t=Teacher(10,"amit","mum",1000)
t.show()
		
