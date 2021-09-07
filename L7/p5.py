# wapp for single inheritance person <-- student
class person:
	def __init__(self,id,name,address):
		self.id = id
		self.name = name
		self.address = address
	def show(self):
		print("id = ",self.id)
		print("name = ",self.name)
		print("address = ",self.address)
class student(person):
	def __init__(self,id,name,address,marks):
		super().__init__(id,name,address)
		self.marks = marks
	def show(self):
		super().show()
		print("Marks = ",self.marks)
s1 = student(10, "amit","mumbai",99)
s1.show()






