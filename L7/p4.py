''' Create class Student with foll:-
	IV:-rno,name & marks
	PI:-rno,name & marks
	IM:- display_data() for rno,name & marks
	SV:-count for tracking on number of students
	SM:-for displaying count's value
'''
class Student :
	count = 0
	def __init__(self,rno,name,marks):
		self.rno = rno
		self.name = name
		self.marks = marks
		Student.count  = Student.count + 1
	def display_data(self):
		print("Rno ",self.rno)
		print("Name ",self.name)
		print("Marks ",self.marks)
	@staticmethod
	def display_count():
		print("No.of Students ",Student.count)

stu = []
while True:
	op = int(input("1.add 2.View 3.View count and 4,Exit "))
	

	if op == 1:
		rno = int(input("Enter Roll:no: "))
		name = input("Enter Name ")
		marks = float(input("Enter Marks "))
		s = Student(rno,name,marks)
		stu.append(s)
			
	elif op == 2:
		for s in stu:
			s.display_data()
			print("*" * 30)
	elif op == 3:
		Student.display_count()	
	elif op == 4:
		break
	else:
		print("Invalid Option ")











