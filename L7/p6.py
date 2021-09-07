# wapp for multi-level inheritance person <-- teacher <--hod
class person:
	def __init__(self, id, name, address):
		self.id = id
		self.name = name
		self.address = address
	def show(self):
		print("id = ",self.id)
		print("name = ",self.name)
		print("address = ",self.address)
class teacher(person):
	def __init__(self, id, name, address, salary):
		super().__init__(id,name,address)
		self.salary = salary
	def show(self):
		super().show()
		print("salary = ",self.salary)
class hod(teacher):
	def __init__(self, id, name, address, salary, dept):
		super().__init__(id,name,address,salary)
		self.dept = dept
	def show(self):
		super().show()
		print("Dept ",self.dept)
h = hod(10, "amit", "mumbai", 10000, "comp")
h.show()




