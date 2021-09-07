''' create class Employee with IV:- id,name & pds (per day salary)
     Create class Attendance with IV:- nodp (no.of days present)
      e = Employee(10,"Amit",500)
       a = Attendance(20)
       salary = e * a
                 = 10000
'''

class Employee:
	def __init__(self, id, name, pds):
		self.id = id
		self.name = name
		self.pds = pds
	def __mul__(self, other):
		jawab = self.pds * other.nodp
		return jawab
class Attendance:
	def __init__(self, nodp):
		self.nodp = nodp

e = Employee(10, "Amit",500)
a = Attendance(20)

salary = e * a
print(salary)






