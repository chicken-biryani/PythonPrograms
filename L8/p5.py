'''
create class Employee with IV:- id,name & salary (PI)
		          IM :-show()
write a menu driven python program
	1. add in a list
	2.view from list
	3.sort as per salary ascending order
	4.exit
'''
class Employee:
	def __init__(self, id, name, salary):
		self.id = id
		self.name = name
		self.salary = salary
	def show(self):
		print("id = ",self.id)
		print("name = ",self.name)
		print("salary = ",self.salary)
	def __lt__(self,other):
		ans = self.salary < other.salary
		return ans
emp = []
while True:
	op = int(input("1 add, 2 View, 3 Sort and 4 Exit "))
	if op == 1:
		id = int(input("Enter id "))
		name = input("Enter Name ")
		salary = float(input("Enter Salary "))
		e = Employee(id,name,salary)
		emp.append(e)
		print("Employee added ")
	elif op == 2:
		for e in emp:
			e.show()
			print("#" * 20)
	elif op == 3:
		emp.sort()
	elif op == 4:
		break
	else:
		print("Ivalid option") 