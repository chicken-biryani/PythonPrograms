class student:
	prof="kamal sir"
	def __init__(self,rno,name,marks):
		self.rno=rno
		self.name=name
		self.marks=marks

	def talk(self):
		print(self.rno,self.name)
	def find_grade(self):
		if self.marks>80:
			c="A"
		else:
			c="B"
		print(c)
	@staticmethod
	def get_prof_name():
		print(student.prof)

a=student(12,"shloka",50)
a.get_prof_name()
a.find_grade()
a.talk()

		
		
		