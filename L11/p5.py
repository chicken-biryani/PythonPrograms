'''to find age in terms of year'''
from datetime import *
def age(day,month,year):
	try:
		dob=date(year,month,day)
		today=datetime.now().date()
	
		print(dob) 
		print(today)
		print((today-dob).days/365)
	except ValueError as e:
		print("dob issue")
	