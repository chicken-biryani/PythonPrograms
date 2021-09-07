import pickle
import os.path
class Student:
	def __init__(self,rno,name):
		self.rno = rno
		self.name = name
	def show(self):
		print("rno = ",self.rno," name = ", self.name)
filename = "student_ka_data.ser"
stu = []
if os.path.exists(filename):
	f = open(filename,"rb")
	stu = pickle.load(f)
	f.close()
while True:
	op = int(input("1 add, 2 view, 3 remove and 4 exit "))
	if op == 1:
		rno = int(input("Enter rno "))
		name = input("Enter name ")
		s = Student(rno, name)
		stu.append(s)
		print("Record added ")
	elif op ==2:
		for s in stu:
			s.show()
	elif op == 3:
		rno = int(input("Enter rno to be deleted "))
		for s in stu:
			if s.rno == rno:
				stu.remove(s)
				break
	elif op == 4:
		f = open(filename, "wb")
		pickle.dump(stu, f)
		f.close()
		break
	else:
		print("Invalid option 5")