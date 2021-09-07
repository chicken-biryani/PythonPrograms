''' SV : count PI & IV : rm=no,name & marks
 SM: show count 
	IM : show info()
menu: 1-add 2-view 3-delete 4-exit'''

class student: 
	count = 0
	def __init__ (self,rno,name,marks):
		self.rno = rno
		self.name=name
		self.marks = marks
		student.count = student.count+1
	@staticmethod
	def show_count():
		print(student.count)
	def show_info(self):
		print(self.rno,' ',self.name," ",self.marks)

stu = []
while True:
	op = int(input("1-add,2-view students 3-view count 4-delete nd 5-exit"))

	if op == 1:
		rno = int(input("enter rno "))
		name = input("enter name ")
		marks = int(input("enter marks"))
		s = student(rno,name,marks)
		stu.append(s)

	elif op == 4:
		rollno = input("enter rollno to remove")
		if rollno in stu:
			s.remove(rollno)
		else:
			print("student doesnt exist ")
	elif op == 2:
		for s in stu:
			s.show_info()
	elif op == 5:
		break
	elif op == 3:
		print(student.show_count())
	else:
		print("invalid option ")