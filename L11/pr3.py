class Person:
	def __init__(self, id, name, address):
		self.id = id
		self.name = name
		self.address = address
	def show(self):
		print("id = ", self.id)
		print("name = ",  self.name)
		print("address = ", self.address)
class Student(Person):
	def __init__(self, id, name, address, marks):
		super().__init__(id, name, address)
		self.marks = marks
	def show(self):
		super().show()
		print("marks = ", self.marks)
class Sport:
	def __init__(self, medals):
		self.medals = medals
	def show(self):
		print("medals = ", self.medals)
class Result(Student, Sport):
	def __init__(self,id,name,address,marks,medals,day,month,year):
		Student.__init__(self,id,name,address,marks)
		Sport.__init__(self,medals)
		self.db=self.DOB(day,month,year)
	def show(self):
		Student.show(self)
		Sport.show(self)
		self.db.showdate()
	
	class DOB:
		def __init__(self,day,month,year):
			self.day=day
			self.month=month
			self.year=year
		def showdate(self):
			print(self.day,'/',self.month,'/',self.year)

r = Result(10, "Amit", "Thane", 88, 2,20,1,1990)
r.show()	