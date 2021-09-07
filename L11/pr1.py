class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address
	def show(self):
		print(self.id)
		print(self.name)
		print(self.address)

class Student(Person):
	def __init__(self,id,name,address,marks):
		super().__init__(id,name,address)
		self.marks=marks
	def show(self):
		super().show()
		print(self.marks)
s1=Student(10,"amit","mumbai",87)
s1.show()